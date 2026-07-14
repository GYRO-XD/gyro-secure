cat > setup_termux.sh << 'EOF'
#!/bin/bash

echo "╔═══════════════════════════════════════╗"
echo "║     GYRO-Secure Framework Setup      ║"
echo "║     For Termux - GYRO-XD            ║"
echo "╚═══════════════════════════════════════╝"

echo "[*] Updating Termux..."
pkg update -y && pkg upgrade -y

echo "[*] Installing dependencies..."
pkg install python python-pip git openssl-tool nmap whois dos2unix -y

echo "[*] Installing Python modules..."
pip install --upgrade pip
pip install requests beautifulsoup4 rich python-whois dnspython urllib3

echo "[*] Creating wordlists directory..."
mkdir -p wordlists

echo "[*] Fixing file permissions and line endings..."
find . -name "*.py" -exec dos2unix {} \; 2>/dev/null
find . -name "*.sh" -exec dos2unix {} \; 2>/dev/null
chmod +x *.py *.sh 2>/dev/null

echo "[*] Setting up main file..."
MAIN_FILE=""
if [ -f "gyro_secure.py" ]; then
    MAIN_FILE="gyro_secure.py"
elif [ -f "gyro-secure.py" ]; then
    MAIN_FILE="gyro-secure.py"
elif [ -f "gyro-secure" ]; then
    MAIN_FILE="gyro-secure"
elif [ -f "gyro-sec.py" ]; then
    MAIN_FILE="gyro-sec.py"
fi

if [ -n "$MAIN_FILE" ]; then
    echo "[✓] Main file found: $MAIN_FILE"
    # Create symlink for convenience
    ln -sf "$MAIN_FILE" gyro_secure.py 2>/dev/null
else
    echo "[!] Warning: No main Python file found!"
fi

echo ""
echo "╔═══════════════════════════════════════╗"
echo "║     Setup Complete!                  ║"
echo "║                                       ║"
if [ -n "$MAIN_FILE" ]; then
    echo "║  Run: python $MAIN_FILE           ║"
else
    echo "║  Run: python gyro_secure.py       ║"
fi
echo "║  Or: python gyro_secure.py           ║"
echo "╚═══════════════════════════════════════╝"
EOF

chmod +x setup_termux.sh
./setup_termux.sh
