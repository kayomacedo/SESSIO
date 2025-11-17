import os
import subprocess
import sys
import venv

VENV_DIR = "venv"
REQ_FILE = "requirements.txt"

def create_venv():
    print("📦 Criando ambiente virtual...")
    builder = venv.EnvBuilder(with_pip=True)
    builder.create(VENV_DIR)
    print("✔ venv criada com sucesso!\n")

def get_python():
    return (
        os.path.join(VENV_DIR, "Scripts", "python.exe") 
        if os.name == "nt" 
        else os.path.join(VENV_DIR, "bin", "python")
    )

def install_requirements():
    python = get_python()
    if not os.path.exists(REQ_FILE):
        print(f"⚠ O arquivo {REQ_FILE} não existe, pulando requirimentos.\n")
        return
    
    print("📥 Instalando dependências do requirements.txt...")
    subprocess.check_call([python, "-m", "pip", "install", "-r", REQ_FILE])
    print("✔ requirements instalados!\n")

def install_playwright():
    python = get_python()

    print("📥 Instalando Playwright...")
    subprocess.check_call([python, "-m", "pip", "install", "playwright"])

    print("🌐 Instalando navegadores do Playwright (chromium, webkit, firefox)...")
    subprocess.check_call([python, "-m", "playwright", "install"])

    print("✔ Playwright e navegadores instalados!\n")

def main():
    if not os.path.exists(VENV_DIR):
        create_venv()
    else:
        print("⚠ venv já existe, pulando criação.\n")

    install_requirements()
    install_playwright()

    print("🎉 Ambiente configurado com sucesso!")

if __name__ == "__main__":
    main()
