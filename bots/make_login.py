import os
from playwright.sync_api import sync_playwright
from database.config_db import load_config
from bots import check_login

STATE_PATH = "session_manager/state.json"


def login(email, password):
    config = load_config()
    login_url = config["login_url"]
    #home_url = config["home_url"]
    
    if not email or not password:
        raise ValueError("❌ Email ou senha não encontrados!")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto(login_url, timeout=60000)
        page.wait_for_load_state("domcontentloaded")

        page.wait_for_selector('input[name="email"]')
        page.locator('input[name="email"]').fill(email)

        page.wait_for_selector('input[name="password"]')
        page.locator('input[name="password"]').fill(password)

        page.locator('button[type="submit"]').click()
        page.wait_for_url("**/dashboard*", timeout=60000)

        print("✅ Login realizado com sucesso!")

        os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
        context.storage_state(path=STATE_PATH)

        print("💾 Sessão salva em:", STATE_PATH)

        browser.close()

    return True



if __name__ == "__main__":

    email = input("Informe seu email: ")
    password = input("Informe sua senha: ")
    
    login(email,password)
