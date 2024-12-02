#!/bin/bash

echo "Configurando o ambiente virtual..."

# Verifica se o Python está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python3 não está instalado. Por favor, instale o Python3 antes de continuar."
    exit 1
fi

# Cria o ambiente virtual
python3 -m venv env

# Ativa o ambiente virtual
source env/bin/activate

# Instala as dependências
pip install --upgrade pip
pip install -r requirements.txt

source env/bin/activate

echo "Ambiente virtual configurado com sucesso!"
echo "Use 'source env/bin/activate' para ativar o ambiente."
