# 🦎 Gekko - Malware Analysis Pipeline

> Automated file detection, quarantine, and analysis system

Gekko is an integrated malware analysis pipeline that automatically detects suspicious files, quarantines them safely, and performs static analysis to determine malicious behavior. Built by second-year Computer Science students as a practical security engineering project.

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---


---

## Overview

Gekko provides a complete malware analysis workflow:
```
New File Detected → Quarantine → Analysis → Report
    (Detector)      (Detector)   (Analyzer) (Analyzer)
```

**Use Cases:**
- Automated monitoring of download directories
- Safe isolation of suspicious executables
- Static analysis of potential malware
- Educational tool for understanding malware behavior
ally pre-installed)

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/gekko.git
cd gekko

# Install dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p quarantine reports logs

# Verify installation
python detector/file_watcher.py --help
python analyzer/file_analyzer.py --help
```

### Dependencies
```
watchdog>=3.0.0
psutil>=5.9.0
```

---

## Usage

### Starting the Detector
```bash
# Monitor /tmp directory
python detector/file_watcher.py --path /tmp

# Monitor Downloads folder
python detector/file_watcher.py --path ~/Downloads

# Monitor multiple directories
python detector/file_watcher.py --path /tmp --path ~/Downloads
```

**Output:**
```
🦎 Gekko File Detector v0.1
Monitoring: /tmp

[14:32:15]  New file detected: suspicious.exe
[14:32:15] ✓ Quarantined: /quarantine/suspicious.exe
[14:32:15] ✓ SHA256: a3f5e2d4c1b7...
```

### Running the Analyzer
```bash
# Analyze a single file
python analyzer/file_analyzer.py --file /quarantine/suspicious.exe

# Analyze all quarantined files
python analyzer/file_analyzer.py --analyze-all

# Generate HTML report
python analyzer/file_analyzer.py --file /quarantine/suspicious.exe --report html
```

*

---



## 🔒 Security Notice

**⚠️ WARNING: This tool is for educational purposes only.**

- Never execute files from the quarantine directory
- Use in isolated environments (VMs) when testing with real malware
- This is a learning project, not production security software
- Always follow responsible disclosure practices

---

## Contributing

This is an educational project, but feedback and suggestions are welcome!

**Built with 🦎 by Computer Science students learning security**

[⬆ Back to Top](#-gekko---malware-analysis-pipeline)

</div>
