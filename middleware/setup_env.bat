@echo off
echo Configurando o ambiente virtual...

:: Verifica se o Python está instalado
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python não está instalado. Por favor, instale o Python antes de continuar.
    exit /b 1
)

:: Cria o ambiente virtual
python -m venv env

:: Ativa o ambiente virtual
call env\Scripts\activate

:: Instala as dependências
pip install --upgrade pip
pip install -r requirements.txt

echo Ambiente virtual configurado com sucesso!
echo Use "env\Scripts\activate" para ativar o ambiente.
