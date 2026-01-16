import os
import subprocess
import colorama
from colorama import Back, Fore, Style
import math
from collections import Counter
import re
import pefile
import sys
from rich.text import Text
from rich import print
import hashlib



# if len(sys.argv) < 2:
#     print("Usage: python main.py <filename>")
#     sys.exit()

# filename = sys.argv[1]
# if not os.path.exists(filename):
#     print(f"Error: {filename} not found")
#     sys.exit()

# size = os.path.getsize(filename)
# print(f"Size: {size} bytes")





RED_FLAGS = [
    "http", "https", ".onion",
    "cmd.exe", "powershell", "pwsh",
    "rundll32", "regsvr32", "mshta",
    "virtualalloc", "writeprocessmemory",
    "createremotethread",
    "isdebuggerpresent", "vmware", "vbox",
    "keylog", "getasynckeystate",
    "runonce", "currentversion\\run","__imp_fputwc","imp"
]




def calculate_entropy(data):
    if not data:
        return 0
    
    byte_counts  = Counter(data)
    total_bytes = len(data)

    entropy = 0
    for count in byte_counts.values():
        probability = count / total_bytes
        entropy -= probability * math.log2(probability)
    return entropy

def hash_file(filepath):
    with open(filepath, 'rb') as f:
        file_data = f.read()
        sha256_hash = hashlib.sha256(file_data).hexdigest()
        return sha256_hash

#basic anaylsis, need to put run entropy calculation via its own function
def anaylse_file(filepath):
    
    print(f"Analysing file path: {filepath}")


    file_size = os.path.getsize(filepath)
    print(f"Size: {file_size} bytes")

    FILE_TYPE = subprocess.run(["file",filepath],capture_output=True,text=True)

    with open(filepath, 'rb') as f:
        file_bytes = f.read()
        file_entropy = calculate_entropy(file_bytes)

    print(f"{Fore.RED if file_entropy > 7.5 else Fore.WHITE}{file_entropy} + {Style.RESET_ALL}")
    if file_entropy > 7.5:
        print(Fore.RED + "High Entropy Detected - Possibly packed or encrypted" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Normal entropy" + Style.RESET_ALL)

    print(f"Type: {FILE_TYPE.stdout.strip()}")




# extracts strings from given file 
def string_dump(filepath):
    global STRINGS 
    STRINGS = subprocess.run(["strings",filepath],capture_output=True,text=True).stdout.splitlines()

    print(f"Extracted Strings: \n")
    for s in STRINGS[:10]:
        s_lower = s.lower()

        bad_string = any(flag in s_lower for flag in RED_FLAGS)
        if bad_string:
            print(Fore.RED + s + Style.RESET_ALL)
        else:
            print(Fore.WHITE + s + Style.RESET_ALL)


def analyse_sections(filepath):
    pe = pefile.PE(filepath)
    print(f"Sections in {filepath}:")
    for section in pe.sections:
        entropy =  section.get_entropy()
        print(f"[bold green]Name:[/bold green] {section.Name.decode().rstrip('\\x00')}, Virtual Size: {section.Misc_VirtualSize}, Raw Size: {section.SizeOfRawData}, {"[green]" if entropy < 7 else "[red]"}Entropy: {entropy}[/]")
        
        







    


if __name__ == "__main__":
    
    print(hash_file("mingw64.exe"))





