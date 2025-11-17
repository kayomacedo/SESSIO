from playwright.sync_api import sync_playwright
import time
import os
import sys
from database.config_db import load_config

STATE_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "session_manager", "state.json")
def bot(worker_id):
    with sync_playwright() as p:
        config = load_config()
        home_url = config["home_url"]
        browser = p.chromium.launch(headless=False, slow_mo=30)
        context = browser.new_context(storage_state=STATE_FILE)
        page = context.new_page()

        page.goto(home_url )
        print(f"[WORKER {worker_id}] Logado! URL:", page.url)

        time.sleep(10)

if __name__ == "__main__":
    wid = sys.argv[1]
    bot(wid)
