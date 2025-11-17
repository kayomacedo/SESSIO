from playwright.sync_api import sync_playwright
import time
from database.config_db import load_config
def main():
    with sync_playwright() as p:
        config = load_config()
        login_url = config["login_url"]
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()

        page = context.new_page()
        page.goto(login_url)

        print("\n===========================")
        print(" FAÇA LOGIN MANUALMENTE")
        print("===========================\n")

        input("Pressione ENTER quando estiver logado...")

        context.storage_state(path="session_manager/state.json")
        print("\nSessão inicial salva com sucesso!")

        browser.close()

if __name__ == "__main__":
    main()
