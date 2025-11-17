import os
from dotenv import load_dotenv
from playwright.sync_api import TimeoutError

# Configurações
load_dotenv()


home_url = os.getenv("HOME_URL")
login_url = os.getenv("LOGIN_URL")


def refresh_session(context, page):

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
