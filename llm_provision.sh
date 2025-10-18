#!/bin/bash

# Mise à jour système
echo "############################################"
echo "System update in progress..."
echo "############################################"
echo ""
apt update # && apt upgrade -y
echo ""

# Installer curl si absent
echo "############################################"
echo "Installing needed packages ..."
echo "############################################"
echo ""
apt install -y curl
echo ""

# Installer Ollama
echo "############################################"
echo "Installing Ollama LLM ..."
echo "############################################"
echo ""
curl -fsSL https://ollama.com/install.sh | sh
echo ""

# Redémarrer le service Ollama
echo "############################################"
echo "Restarting Ollama service ..."
echo "############################################"
echo ""
systemctl restart ollama
echo ""

# Message de fin
echo "############################################"
echo "[✓] Ollama installed and ready to use."
echo "############################################"
