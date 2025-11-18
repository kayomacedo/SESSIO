import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
import time

# Caminho cross-platform
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_FILE = os.path.join(BASE_DIR, "session_manager", "state.json")

def logout():
    with sync_playwright() as p:
        # Configurações
        load_dotenv()
        home_url = os.getenv("HOME_URL")
        login_url = os.getenv("LOGIN_URL")

        browser = p.chromium.launch(headless=True, slow_mo=50)
        context = browser.new_context()

        page = context.new_page()
        page.goto(login_url)

        print("\n===========================")
        print(" Fazendo Logoff")
        print("===========================\n")

        # Salvar o novo estado (logout)
        context.storage_state(path=STATE_FILE)

        print("\nSessão inicial salva com sucesso!")

        browser.close()
    return True

if __name__ == "__main__":
    logout()


