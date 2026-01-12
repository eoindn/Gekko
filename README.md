# 🦎 Gekko - Malware Analysis Pipeline

> Automated file detection, quarantine, and analysis system

Gekko is an integrated malware analysis pipeline that automatically detects suspicious files, quarantines them safely, and performs static analysis to determine malicious behavior. Built by second-year Computer Science students as a practical security engineering project.

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Roadmap](#roadmap)
- [Team](#team)
- [License](#license)

---

## 🎯 Overview

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

---

## 🏗️ Architecture

### System Components

**1. File Detector (Blue Team)**
- Real-time file system monitoring
- Automatic quarantine of suspicious files
- SHA256 hash calculation
- Event logging

**2. File Analyzer (Red Team)**
- Metadata extraction
- String analysis
- Disassembly engine
- Maliciousness scoring
- Report generation

### Data Flow
```
┌─────────────────────┐
│  Monitored Folders  │
│  (Downloads, /tmp)  │
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│  File Detector      │
│  - Watch for new    │
│  - Calculate hash   │
│  - Apply rules      │
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│  Quarantine Zone    │
│  (Isolated Storage) │
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│  File Analyzer      │
│  - Extract metadata │
│  - Find strings     │
│  - Disassemble      │
│  - Score threat     │
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│  Analysis Report    │
│  (HTML/JSON)        │
└─────────────────────┘
```

---

## ✨ Features

### Current (Week 1-3)

**Detector:**
- [x] Real-time file monitoring
- [x] Automatic quarantine
- [x] File hashing (SHA256)
- [x] JSON event logging
- [x] CLI interface

**Analyzer:**
- [x] Metadata extraction
- [x] String extraction
- [x] File type identification
- [x] Basic analysis reports
- [x] CLI interface

### Planned

**Detector:**
- [ ] Smart detection rules
- [ ] File type filtering
- [ ] Whitelist support
- [ ] Email alerts

**Analyzer:**
- [ ] Disassembly (ELF/PE)
- [ ] Entropy calculation
- [ ] Suspicious pattern detection
- [ ] HTML report generation
- [ ] Maliciousness scoring

---

## 🚀 Installation

### Prerequisites

- Python 3.8+
- Linux/WSL2/macOS (Windows support limited)
- `file` command (usually pre-installed)
- `strings` command (usually pre-installed)

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

## 💻 Usage

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

[14:32:15] 🚨 New file detected: suspicious.exe
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

**Output:**
```
🔬 Gekko File Analyzer v0.1
Analyzing: suspicious.exe

📊 Metadata:
├─ Type: ELF 64-bit executable
├─ Size: 18432 bytes
├─ SHA256: a3f5e2d4c1b7...

🔤 Suspicious Strings:
├─ "/bin/sh"
├─ "192.168.1.100:4444"
├─ "password"

⚠️  Threat Score: 7/10 (HIGH)
└─ Recommendation: Do not execute

✓ Report saved: /reports/suspicious_report.json
```

---

## 📁 Project Structure
```
gekko/
├── README.md
├── requirements.txt
├── LICENSE
│
├── detector/                  # File detection & quarantine
│   ├── file_watcher.py       # Main monitoring script
│   ├── quarantine_manager.py # Quarantine logic
│   └── rules.json            # Detection rules
│
├── analyzer/                  # File analysis
│   ├── file_analyzer.py      # Main analysis script
│   ├── metadata_extractor.py # Metadata extraction
│   ├── string_extractor.py   # String extraction
│   ├── disassembler.py       # Disassembly (coming soon)
│   └── report_generator.py   # Report creation
│
├── quarantine/                # Isolated file storage
│   └── .gitkeep
│
├── reports/                   # Analysis reports
│   └── .gitkeep
│
└── logs/                      # Event logs
    ├── quarantine_log.json
    └── analysis_log.json
```

---

## 🗓️ Roadmap

### Week 1: Foundation ✅
- [x] Basic file monitoring
- [x] Quarantine functionality
- [x] Metadata extraction
- [x] String extraction
- [x] Integration between components

### Week 2: Enhanced Analysis 🚧
- [ ] File type-specific handling (ELF, PE, scripts)
- [ ] Disassembly capability
- [ ] Suspicious pattern detection
- [ ] Entropy calculation
- [ ] Improved detection rules

### Week 3: Production Ready 📋
- [ ] CLI improvements
- [ ] HTML report generation
- [ ] Maliciousness scoring system
- [ ] Testing with real samples
- [ ] Complete documentation

---

## 👥 Team

**Joseph Ulasi** - File Detection & Quarantine (Blue Team)
- 2nd Year Computer Science, St Mary's University Twickenham
- Focus: Defensive security, file monitoring, threat detection

**Eoin Donnelly** - File Analysis & Reverse Engineering (Red Team)
- 2nd Year Computer Science, St Mary's University Twickenham
- Focus: Malware analysis, disassembly, pattern recognition

---

## 🔒 Security Notice

**⚠️ WARNING: This tool is for educational purposes only.**

- Never execute files from the quarantine directory
- Use in isolated environments (VMs) when testing with real malware
- This is a learning project, not production security software
- Always follow responsible disclosure practices

---

## 🤝 Contributing

This is an educational project, but feedback and suggestions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📚 Learning Resources

Resources we used while building Gekko:

- [Python watchdog documentation](https://pythonhosted.org/watchdog/)
- [Practical Malware Analysis](https://nostarch.com/malware)
- [OSDev Wiki - ELF Format](https://wiki.osdev.org/ELF)
- [VirusTotal API Documentation](https://developers.virustotal.com/reference/overview)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- St Mary's University Twickenham Computer Science Department
- Python watchdog library maintainers
- The open-source security community

---

## 📞 Contact

Questions or feedback? Reach out:

- Joseph: [GitHub Profile]
- Eoin: [GitHub Profile]

---

<div align="center">

**Built with 🦎 by Computer Science students learning security**

[⬆ Back to Top](#-gekko---malware-analysis-pipeline)

</div>