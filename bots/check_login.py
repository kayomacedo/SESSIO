from playwright.sync_api import sync_playwright
import os
from database.config_db import load_config

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATE_FILE = os.path.join(BASE_DIR, "session_manager", "state.json")



def is_logged_in(page):
    config = load_config()
    home_url = config["home_url"]
    link_dashboard = home_url
    if page.url == link_dashboard:
        return True
    else:
        return False
    

def check_login(headless=False):
    config = load_config()
    home_url = config["home_url"]
    

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state=STATE_FILE)
        page = context.new_page()

        page.goto(home_url, timeout=60000)
        page.wait_for_load_state("domcontentloaded")

        

        if is_logged_in(page):
            #print("✅ O usuário está logado!")
            
            return True
        else:
            #print("❌ O usuário NÃO está logado!")
            return False
        
    browser.close()

if __name__ == "__main__":
    logado = check_login()

    if logado:
        print("✅ O usuário está logado!")
    else:
        print("❌ O usuário NÃO está logado!")
