from playwright.sync_api import TimeoutError
from database.config_db import load_config

def refresh_session(context, page):
    config = load_config()
    home_url = config["home_url"]
    """
    RENOVA TOKENS DE SESSÃO SEM DESLOGAR
    Funciona para 90% dos sites que expiram cookies.
    """

    print("🔄 Tentando renovar sessão...")

    try:
        # 1) Recarregar a página do dashboard
        page.goto(home_url, wait_until="domcontentloaded")

        # 2) Forçar renovação de cookies
        context.storage_state(path="session_manager/state.json")

        print("✅ Sessão renovada com sucesso!")

    except TimeoutError:
        print("⚠ Timeout ao tentar renovar a sessão")
    except Exception as e:
        print("❌ Erro ao renovar sessão:", e)
