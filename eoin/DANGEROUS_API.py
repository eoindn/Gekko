DANGEROUS_APIS = {




    
    # Process Injection & Memory Manipulation
    'VirtualAllocEx': {
        'category': 'Process Injection',
        'score': 8,
        'reason': 'Allocates memory in another process - classic injection technique'
    },
    'WriteProcessMemory': {
        'category': 'Process Injection',
        'score': 9,
        'reason': 'Writes to another process memory - code injection'
    },
    'CreateRemoteThread': {
        'category': 'Process Injection',
        'score': 9,
        'reason': 'Creates thread in another process - remote code execution'
    },
    'OpenProcess': {
        'category': 'Process Injection',
        'score': 6,
        'reason': 'Opens handle to another process - required for injection'
    },
    'VirtualProtect': {
        'category': 'Process Injection',
        'score': 7,
        'reason': 'Changes memory protection - often used by packers/shellcode'
    },
    'VirtualProtectEx': {
        'category': 'Process Injection',
        'score': 8,
        'reason': 'Changes memory protection in another process'
    },
    'QueueUserAPC': {
        'category': 'Process Injection',
        'score': 8,
        'reason': 'APC injection technique'
    },
    'SetThreadContext': {
        'category': 'Process Injection',
        'score': 9,
        'reason': 'Process hollowing technique'
    },
    'ResumeThread': {
        'category': 'Process Injection',
        'score': 5,
        'reason': 'Resumes suspended thread - used in hollowing'
    },
    'NtMapViewOfSection': {
        'category': 'Process Injection',
        'score': 9,
        'reason': 'Advanced injection via section mapping'
    },
    
    # Anti-Debug & Anti-Analysis
    'IsDebuggerPresent': {
        'category': 'Anti-Debug',
        'score': 8,
        'reason': 'Detects debugger presence'
    },
    'CheckRemoteDebuggerPresent': {
        'category': 'Anti-Debug',
        'score': 8,
        'reason': 'Checks if remote debugger attached'
    },
    'OutputDebugString': {
        'category': 'Anti-Debug',
        'score': 6,
        'reason': 'Can be used for anti-debug tricks'
    },
    'GetTickCount': {
        'category': 'Anti-Debug',
        'score': 4,
        'reason': 'Timing checks to detect debugging/sandboxing'
    },
    'QueryPerformanceCounter': {
        'category': 'Anti-Debug',
        'score': 4,
        'reason': 'High-precision timing for anti-debug'
    },
    'NtQueryInformationProcess': {
        'category': 'Anti-Debug',
        'score': 7,
        'reason': 'Queries process info - used for anti-debug'
    },
    'ZwSetInformationThread': {
        'category': 'Anti-Debug',
        'score': 8,
        'reason': 'Hides threads from debugger'
    },
    
    # Persistence
    'RegSetValueEx': {
        'category': 'Persistence',
        'score': 7,
        'reason': 'Modifies registry - common persistence mechanism'
    },
    'RegCreateKeyEx': {
        'category': 'Persistence',
        'score': 6,
        'reason': 'Creates registry keys - often for autostart'
    },
    'CreateService': {
        'category': 'Persistence',
        'score': 8,
        'reason': 'Creates Windows service for persistence'
    },
    'OpenSCManager': {
        'category': 'Persistence',
        'score': 6,
        'reason': 'Accesses service control manager'
    },
    'StartService': {
        'category': 'Persistence',
        'score': 7,
        'reason': 'Starts Windows service'
    },
    'SetWindowsHookEx': {
        'category': 'Persistence/Keylogging',
        'score': 8,
        'reason': 'Installs hook - keylogging or persistence'
    },
    
    # Keylogging & Input Capture
    'GetAsyncKeyState': {
        'category': 'Keylogging',
        'score': 9,
        'reason': 'Captures keyboard input - keylogger'
    },
    'GetForegroundWindow': {
        'category': 'Keylogging',
        'score': 5,
        'reason': 'Gets active window - used with keyloggers'
    },
    'GetWindowText': {
        'category': 'Keylogging',
        'score': 4,
        'reason': 'Captures window titles - spyware behavior'
    },
    'SetWindowsHookExA': {
        'category': 'Keylogging',
        'score': 8,
        'reason': 'Keyboard hook for keylogging'
    },
    
    # Network Operations
    'InternetOpen': {
        'category': 'Network',
        'score': 5,
        'reason': 'Initializes internet connection'
    },
    'InternetOpenUrl': {
        'category': 'Network',
        'score': 6,
        'reason': 'Opens URL - potential C2 or download'
    },
    'InternetReadFile': {
        'category': 'Network',
        'score': 6,
        'reason': 'Downloads data from internet'
    },
    'URLDownloadToFile': {
        'category': 'Network',
        'score': 8,
        'reason': 'Downloads file from URL - dropper behavior'
    },
    'HttpOpenRequest': {
        'category': 'Network',
        'score': 5,
        'reason': 'Creates HTTP request'
    },
    'HttpSendRequest': {
        'category': 'Network',
        'score': 5,
        'reason': 'Sends HTTP request - C2 communication'
    },
    'send': {
        'category': 'Network',
        'score': 4,
        'reason': 'Socket send - network communication'
    },
    'recv': {
        'category': 'Network',
        'score': 4,
        'reason': 'Socket receive - network communication'
    },
    'WSAStartup': {
        'category': 'Network',
        'score': 3,
        'reason': 'Initializes Winsock'
    },
    'socket': {
        'category': 'Network',
        'score': 4,
        'reason': 'Creates socket'
    },
    'connect': {
        'category': 'Network',
        'score': 5,
        'reason': 'Connects to remote host'
    },
    'GetAddrInfo': {
        'category': 'Network',
        'score': 4,
        'reason': 'DNS resolution'
    },
    
    # Code Execution
    'WinExec': {
        'category': 'Execution',
        'score': 7,
        'reason': 'Executes command - deprecated but used by malware'
    },
    'ShellExecute': {
        'category': 'Execution',
        'score': 6,
        'reason': 'Executes file or command'
    },
    'CreateProcess': {
        'category': 'Execution',
        'score': 5,
        'reason': 'Creates new process'
    },
    'CreateProcessA': {
        'category': 'Execution',
        'score': 5,
        'reason': 'Creates new process (ASCII)'
    },
    'CreateProcessW': {
        'category': 'Execution',
        'score': 5,
        'reason': 'Creates new process (Unicode)'
    },
    'system': {
        'category': 'Execution',
        'score': 7,
        'reason': 'Executes shell command'
    },
    
    # Cryptography (Ransomware Indicators)
    'CryptAcquireContext': {
        'category': 'Cryptography',
        'score': 6,
        'reason': 'Accesses crypto provider - potential ransomware'
    },
    'CryptEncrypt': {
        'category': 'Cryptography',
        'score': 7,
        'reason': 'Encrypts data - ransomware indicator'
    },
    'CryptDecrypt': {
        'category': 'Cryptography',
        'score': 6,
        'reason': 'Decrypts data'
    },
    'CryptCreateHash': {
        'category': 'Cryptography',
        'score': 5,
        'reason': 'Creates hash - often legitimate but watch for combos'
    },
    'CryptHashData': {
        'category': 'Cryptography',
        'score': 5,
        'reason': 'Hashes data'
    },
    
    # File Operations (Suspicious)
    'DeleteFile': {
        'category': 'File Operations',
        'score': 5,
        'reason': 'Deletes files - wipers/cleanup'
    },
    'FindFirstFile': {
        'category': 'File Operations',
        'score': 4,
        'reason': 'Enumerates files - ransomware/info stealer'
    },
    'FindNextFile': {
        'category': 'File Operations',
        'score': 4,
        'reason': 'Enumerates files'
    },
    'CopyFile': {
        'category': 'File Operations',
        'score': 4,
        'reason': 'Copies files - spreader behavior'
    },
    'MoveFile': {
        'category': 'File Operations',
        'score': 4,
        'reason': 'Moves/renames files'
    },
    'GetTempPath': {
        'category': 'File Operations',
        'score': 5,
        'reason': 'Gets temp directory - droppers use this'
    },
    
    # Privilege Escalation
    'AdjustTokenPrivileges': {
        'category': 'Privilege Escalation',
        'score': 8,
        'reason': 'Modifies process privileges - often SeDebugPrivilege'
    },
    'OpenProcessToken': {
        'category': 'Privilege Escalation',
        'score': 6,
        'reason': 'Opens process token for manipulation'
    },
    'LookupPrivilegeValue': {
        'category': 'Privilege Escalation',
        'score': 6,
        'reason': 'Looks up privilege for escalation'
    },
    
    # DLL/Module Manipulation
    'LoadLibrary': {
        'category': 'DLL Manipulation',
        'score': 5,
        'reason': 'Loads DLL - can load malicious libraries'
    },
    'LoadLibraryEx': {
        'category': 'DLL Manipulation',
        'score': 5,
        'reason': 'Loads DLL with options'
    },
    'GetProcAddress': {
        'category': 'DLL Manipulation',
        'score': 6,
        'reason': 'Gets function address - dynamic API resolution to hide calls'
    },
    'FreeLibrary': {
        'category': 'DLL Manipulation',
        'score': 3,
        'reason': 'Unloads DLL'
    },
    
    # Mutex (Often for single-instance checks)
    'CreateMutex': {
        'category': 'Synchronization',
        'score': 4,
        'reason': 'Creates mutex - malware uses for single-instance'
    },
    'OpenMutex': {
        'category': 'Synchronization',
        'score': 4,
        'reason': 'Opens existing mutex'
    },
}