
<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/python-3.8+-green" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Termux-Compatible-brightgreen" alt="Termux">
  <img src="https://img.shields.io/github/stars/GYRO-XD/gyro-secure" alt="Stars">
  <img src="https://img.shields.io/github/issues/GYRO-XD/gyro-secure" alt="Issues">
  <img src="https://img.shields.io/github/last-commit/GYRO-XD/gyro-secure" alt="Last Commit">
</p>

---

## 📋 Table of Contents
- [⚠️ Disclaimer](#️-disclaimer)
- [📸 Screenshots](#-screenshots)
- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [🎯 Usage Examples](#-usage-examples)
- [📁 Project Structure](#-project-structure)
- [🔄 Wordlist System](#-wordlist-system)
- [🤝 Contributing](#-contributing)
- [📊 Statistics](#-statistics)
- [🛡️ Legal Notice](#️-legal-notice)
- [📝 License](#-license)
- [👨‍💻 Author](#-author)
- [⭐ Support](#-support)
- [📚 Resources](#-resources)

---

## ⚠️ DISCLAIMER
> **⚠️ IMPORTANT: This tool is for educational purposes and authorized security testing only.**
> 
> - Only use on systems you own or have explicit permission to test
> - The author (GYRO-XD) is not responsible for any misuse
> - Always obtain proper authorization before testing
> - Unauthorized access is illegal in most jurisdictions
> - Use this tool responsibly and ethically

---

## 📸 Screenshots

### 🎯 Main Menu Interface
![Main Menu](https://raw.githubusercontent.com/GYRO-XD/gyro-secure/main/screenshots/main_menu.png)
*Beautiful CLI interface powered by the Rich library with an intuitive menu system*

### 🔍 Subdomain Enumeration in Action
![Subdomain Enumeration](https://raw.githubusercontent.com/GYRO-XD/gyro-secure/main/screenshots/subdomain_scan.png)
*Real-time progress tracking with visual feedback and color-coded results*

### 💉 SQL Injection Scanner
![SQL Injection Scanner](https://raw.githubusercontent.com/GYRO-XD/gyro-secure/main/screenshots/sqli_scanner.png)
*Automated vulnerability detection with detailed output and payload logging*

### 🔌 Port Scanner
![Port Scanner](https://raw.githubusercontent.com/GYRO-XD/gyro-secure/main/screenshots/port_scanner.png)
*Multi-threaded port scanning with progress tracking*

### 📊 Report Generation
![Report Generation](https://raw.githubusercontent.com/GYRO-XD/gyro-secure/main/screenshots/report_generator.png)
*Professional JSON reports for documentation and analysis*

### 🔑 Hash Cracker
![Hash Cracker](https://raw.githubusercontent.com/GYRO-XD/gyro-secure/main/screenshots/hash_cracker.png)
*Fast hash cracking with MD5, SHA1, and SHA256 support*

---

## ✨ Features

### 🔧 Core Security Tools
| Tool | Description | Status |
|------|-------------|--------|
| **Subdomain Enumeration** | Discover subdomains using dynamic wordlists | ✅ Active |
| **Port Scanner** | Multi-threaded port scanning | ✅ Active |
| **Directory Brute Force** | Find hidden directories | ✅ Active |
| **SQL Injection Scanner** | Detect SQL injection vulnerabilities | ✅ Active |
| **XSS Scanner** | Find cross-site scripting vulnerabilities | ✅ Active |
| **HTTP Headers Analyzer** | Analyze security headers | ✅ Active |
| **WHOIS Lookup** | Domain information gathering | ✅ Active |
| **DNS Enumeration** | Complete DNS record enumeration | ✅ Active |
| **Hash Cracker** | Crack MD5, SHA1, SHA256 hashes | ✅ Active |
| **Automated Report Generation** | JSON format reports | ✅ Active |

### 🚀 Advanced Features
- **Dynamic Wordlist System** - Auto-updates from GitHub
- **Multi-threading** - Lightning-fast scanning with ThreadPoolExecutor
- **Rich UI** - Beautiful terminal interface with progress bars
- **Progress Tracking** - Real-time scan progress with visual indicators
- **Error Handling** - Robust error management and recovery
- **Modular Design** - Easy to extend and customize
- **Local Caching** - Wordlists cached for offline use
- **Cross-Platform** - Works on Termux, Linux, macOS, and Windows (WSL)

---

## 📦 Installation

### For Termux
```bash
# Clone the repository
git clone https://github.com/GYRO-XD/gyro-secure
cd gyro-secure

# Make setup script executable
chmod +x setup_termux.sh

# Run setup
./setup_termux.sh

# Launch the framework
python gyro_secure.py
```
