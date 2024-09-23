#!/bin/bash

# Atualiza o Termux
echo "Atualizando o Termux..."
pkg update && pkg upgrade -y

# Instala o Python se não estiver instalado
echo "Instalando Python..."
pkg install python -y

# Instala pip se não estiver instalado
echo "Instalando pip..."
pkg install python-pip -y

# Instala as dependências do Python
echo "Instalando dependências do Python..."
pip install requests
pip install beautifulsoup4
pip install lxml  # Opcional para melhorar o parsing HTML

# Finalização
echo "Instalação completa!"
