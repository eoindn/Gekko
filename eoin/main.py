import os
import subprocess
import colorama
from colorama import Back, Fore, Style
import math
from collections import Counter
import re
import pefile
import sys
import hashlib
from DANGEROUS_API import DANGEROUS_APIS;
from rich.text import Text
from rich import print
from rich.console import Console


console = Console()

dangerous_dictionary = DANGEROUS_APIS # imported dictionary of dangerous windows functions


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

#import hashlib

def calculate_hashes(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
        result = hashlib.md5(data).hexdigest()
        return "file hash: " + result

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


def analyse_sections(filepath, verbose = False):
    sections = []
    entropy_per_section = {}
    pe = pefile.PE(filepath)
    if verbose:
        print(f"Sections in {filepath}:")
    for section in pe.sections:
        entropy =  section.get_entropy()
        entropy_per_section[section.Name.decode().rstrip('\\x00')] = entropy
        if verbose:
            print(f"[bold green]Name:[/bold green] {section.Name.decode().rstrip('\\x00')}, Virtual Size: {section.Misc_VirtualSize}, Raw Size: {section.SizeOfRawData}, {"[green]" if entropy < 7 else "[red]"}Entropy: {entropy}[/]")
        sections.append(section)
    return entropy_per_section




# extracts strings from given file 
def string_dump(filepath, verbose = True):
    strings = []
    global STRINGS 
    STRINGS = subprocess.run(["strings",filepath],capture_output=True,text=True).stdout.splitlines()


   
    for s in STRINGS:
        s_lower = s.lower()
        strings.append(s)

        bad_string = any(flag in s_lower for flag in RED_FLAGS)
        if bad_string:
            if verbose:
                print(Fore.RED + s + Style.RESET_ALL)
        else:
            if verbose:
                print(Fore.WHITE + s + Style.RESET_ALL)

    return strings



def import_check(filepath, verbose = True):

  
    import_dict = {}


    # dlls and import names are set to strs for manipulation using a translation table
    # can just do dll_name = entry.dll.decode('utf-8', errors='ignore') tho
    
    pe = pefile.PE(filepath)
    translation_table = dict.fromkeys(map(ord, 'b'), None) 
    dangerous_found = []
    
    pe.parse_data_directories()
    if not hasattr(pe,'DIRECTORY_ENTRY_IMPORT'):
        print("[yellow]no Imports Found (packed/stripped?)[/yellow]")
        return
    
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        dll_name = str(entry.dll)
        if dll_name[0] == 'b':
            dll_name = dll_name.translate(translation_table)


        dll_dangerous = []

        
        
        



        for imp in entry.imports:  #imp refers to the function imported by the dll
            
            import_name = imp.name.decode('utf-8', errors='ignore')
            address = imp.address
            
        
            if import_name in dangerous_dictionary:
                dangerous_found.append(import_name)
                dll_dangerous.append(import_name)
            # print(f"\t {str(import_name)} at adress: {hex(address)}")

        if dll_dangerous:
            if verbose:
                console.print(f"[yellow]Potentially dangerous import found in [bold yellow]{dll_name}[/bold yellow][/yellow]")
            for function in dll_dangerous:
                info = dangerous_dictionary[function]
                if verbose:
                    console.print(f"  [bold red]{function}[/bold red] - {info['reason']}")

    return dangerous_found





def calculate_risk(filepath):
    

    risk = 0
    dangerous_apis = import_check(filepath,verbose=False)
    strings = string_dump(filepath,verbose=False)
    entropy = analyse_sections(filepath)
    if len(dangerous_apis) < 3 and len(dangerous_apis) > 1:
        risk += 20
    if len(dangerous_apis) > 3 and len(dangerous_apis) < 5:
        risk += 40
    elif len(dangerous_apis) > 5:
        risk += 50 #quite a lot of dangerous imports

    for s in strings:
        if s == "keylog" or s == "keylogger":
            risk += 100
        if s in RED_FLAGS:
            risk += 5

    for entr in entropy.values():
        if entr >= 6:
            risk += 20

    print(entropy)   
        


    print(risk)
                

                




  
        
        










    


if __name__ == "__main__":
    
 
    calculate_risk("mingw64.exe")






