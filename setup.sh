#!/bin/bash

echo "Setting up Pentesting Proxy Tool..."

# Install required system packages
sudo apt update
sudo apt install -y python3 python3-pip tor

# Configure Tor
TOR_CONFIG="/etc/tor/torrc"
if ! grep -q "ControlPort 9051" "$TOR_CONFIG"; then
    echo "ControlPort 9051" | sudo tee -a "$TOR_CONFIG"
    echo "HashedControlPassword $(tor --hash-password 'your_password')" | sudo tee -a "$TOR_CONFIG"
fi
sudo systemctl restart tor

# Install Python dependencies
pip3 install PyQt5 stem requests

# Launch the tool
python3 proxy_tool.py
