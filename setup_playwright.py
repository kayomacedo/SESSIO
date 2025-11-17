import os
import subprocess
import venv

VENV_DIR = "venv"
REQ_FILE = "requirements.txt"
ENV_FILE = ".env"

DEFAULT_ENV_CONTENT = """EMAIL=
PASSWORD=
HOME_URL=
LOGIN_URL=
"""

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
        print(f"⚠ {REQ_FILE} não encontrado. Criando um vazio...")
        with open(REQ_FILE, "w") as f:
            f.write("")
    
    print("📥 Instalando dependências do requirements.txt...")
    subprocess.check_call([python, "-m", "pip", "install", "-r", REQ_FILE])
    print("✔ requirements instalados!\n")

def install_playwright():
    python = get_python()

    print("📥 Instalando Playwright...")
    subprocess.check_call([python, "-m", "pip", "install", "playwright"])

    print("🌐 Instalando navegadores (chromium, firefox, webkit)...")
    subprocess.check_call([python, "-m", "playwright", "install"])

    print("✔ Playwright instalado com sucesso!\n")

def ensure_env_file():
    if os.path.exists(ENV_FILE):
        print("✔ .env encontrado, mantendo arquivo existente.\n")
        return

    print("⚠ .env não encontrado, criando com variáveis vazias...")
    with open(ENV_FILE, "w") as f:
        f.write(DEFAULT_ENV_CONTENT)
    print("✔ .env criado!\n")

def main():
    if not os.path.exists(VENV_DIR):
        create_venv()
    else:
        print("⚠ venv já existe, pulando criação.\n")

    ensure_env_file()
    install_requirements()
    install_playwright()

    print("🎉 Ambiente configurado com sucesso!")

if __name__ == "__main__":
    main()
