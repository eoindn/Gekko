import os
import subprocess
import colorama
from colorama import Back, Fore, Style
import math
from collections import Counter
from scipy.stats import entropy as en
import pandas as pd



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




def anaylse_file(filepath):
    
    print(f"Analysing file path: {filepath}")


    file_size = os.path.getsize(filepath)
    print(f"Size: {file_size} bytes")

    FILE_TYPE = subprocess.run(["file",filepath],capture_output=True,text=True)

    print(f"Type: {FILE_TYPE.stdout.strip()}")

    global STRINGS 
    STRINGS = subprocess.run(["strings",filepath],capture_output=True,text=True).stdout.splitlines()

    print(f"Extracted Strings: \n")
    for s in STRINGS:
        s_lower = s.lower()

        bad_string = any(flag in s_lower for flag in RED_FLAGS)
        if bad_string:
            print(Fore.RED + s)
        else:
            print(Fore.WHITE + s)

    # calculate entropy - indicates packing/obfuscation
    print("\n") 
    STRINGS = pd.Series(STRINGS)
    
    print(en(STRINGS.value_counts()))

        



    


anaylse_file("mingw64.exe")





