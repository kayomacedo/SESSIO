import time
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATE_FILE = os.path.join(BASE_DIR, "session_manager", "state.json")



def open(headless=True):
    # Configurações
    load_dotenv()
    home_url = os.getenv("HOME_URL")
    login_url = os.getenv("LOGIN_URL")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state=STATE_FILE)
        page = context.new_page()

        page.goto(home_url, timeout=60000)
        page.wait_for_load_state("domcontentloaded")

        #input("Pressione Enter para fechar o navegador...")
        # Manter ABERTO por 10 minutos (600s)
        time.sleep(600)

        
        
    browser.close()

if __name__ == "__main__":
    open()
