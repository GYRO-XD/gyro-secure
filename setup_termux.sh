#!/bin/bash
# GYRO-Secure Framework - Termux Setup Script

echo "╔═══════════════════════════════════════╗"
echo "║     GYRO-Secure Framework Setup      ║"
echo "║     For Termux - GYRO-XD            ║"
echo "╚═══════════════════════════════════════╝"

# Update and upgrade
echo "[*] Updating Termux..."
pkg update -y && pkg upgrade -y

# Install Python and necessary packages
echo "[*] Installing Python and dependencies..."
pkg install python -y
pkg install python-pip -y
pkg install git -y
pkg install openssl-tool -y
pkg install nmap -y
pkg install whois -y

# Install Python modules
echo "[*] Installing Python modules..."
pip install --upgrade pip
pip install requests beautifulsoup4 rich python-whois dnspython urllib3

# Create wordlists directory
echo "[*] Creating wordlists directory..."
mkdir -p wordlists

echo "[*] Setup complete!"
echo "[*] To update wordlists from GitHub, run: python gyro_secure.py and select option 10"
echo "[*] Run: python gyro_secure.py"