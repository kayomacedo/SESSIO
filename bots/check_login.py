from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATE_FILE = os.path.join(BASE_DIR, "session_manager", "state.json")

# Configurações
load_dotenv()
home_url = os.getenv("HOME_URL")
login_url = os.getenv("LOGIN_URL")



def is_logged_in(page):
    link_dashboard = home_url
    if page.url == link_dashboard:
        return True
    else:
        return False
    

def check_login(headless=False):
    

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
