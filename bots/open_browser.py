from playwright.sync_api import sync_playwright
import os
from database.config_db import load_config

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATE_FILE = os.path.join(BASE_DIR, "session_manager", "state.json")



def open(headless=True):
    config = load_config()
    home_url = config["home_url"]
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state=STATE_FILE)
        page = context.new_page()

        page.goto(home_url, timeout=60000)
        page.wait_for_load_state("domcontentloaded")

        input("Pressione Enter para fechar o navegador...")
        
        
    browser.close()

if __name__ == "__main__":
    open()
