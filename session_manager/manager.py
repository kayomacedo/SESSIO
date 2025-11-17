import sys
import os
import time
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)
from session_manager.refresh import refresh_session
from bots.check_login import is_logged_in
from bots.make_login import login
from database.config_db import load_config

# Caminho do state.json
STATE_FILE = os.path.join(os.path.dirname(__file__), "state.json")

CHECK_INTERVAL = 60 * 3       # verifica a cada 3 min
REFRESH_INTERVAL = 60 * 20    # renova a cada 20 min

# IMPORT ABSOLUTO (raiz adicionada)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)

# Configurações
load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
home_url = os.getenv("HOME_URL")
login_url = os.getenv("LOGIN_URL")



def manager_loop():
    last_refresh = 0
    control = False
  
    with sync_playwright() as p:
        config = load_config()
      
        browser = p.chromium.launch(headless=True)

        # carregar state.json se existir
        context = browser.new_context(storage_state=STATE_FILE)
        page = context.new_page()

        page.goto(home_url)
        page.wait_for_load_state("domcontentloaded")

        print("🚀 Session Manager iniciado!")

        while True:
            now = time.time()

            # ==================================================
            # 🔥 1) Detectar sessão perdida
            # ==================================================
            if not is_logged_in(page):
                print("❌ Sessão perdida! Reautenticação necessária.")
                control = True
                break

            # ==================================================
            # 🔄 2) Renovar sessão periodicamente
            # ==================================================
            if now - last_refresh > REFRESH_INTERVAL:
                print("♻️ Renovando sessão automaticamente...")

                refresh_session(context, page)

                # salvar o novo state.json
                context.storage_state(path=STATE_FILE)
                last_refresh = now

                print("✔ Sessão renovada!")

            time.sleep(CHECK_INTERVAL)

    
    if control:
        #Faz o login
        #login(email,password)
        print("Precisa fazer login...")
        manager_loop()

if __name__ == "__main__":
    manager_loop()
