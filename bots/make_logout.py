import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
import time

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

        #input("Pressione ENTER quando estiver logado...")


        context.storage_state(path="session_manager/state.json")
        print("\nSessão inicial salva com sucesso!")

        browser.close()
    return True

if __name__ == "__main__":
    logout()
