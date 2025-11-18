from getpass import getpass
import os
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

from bots.check_login import check_login
from bots.make_login import login
from bots.make_logout import logout
from session_manager.manager import manager_loop
from bots.open_browser import open as open_nav

console = Console()


def header():
    console.print(
        Panel.fit(
            Text("✨ S E S S I O  —  Session Automation Framework ✨", justify="center"),
            border_style="magenta",
            title="🚀 Sessio",
            padding=(1, 2),
        )
    )


# ============================================================
#   MENU
# ============================================================
def mostrar_menu():
    console.print(
        Panel.fit(
            "[bold magenta]🛰 MENU PRINCIPAL — Sessio[/bold magenta]\n"
            "\n[cyan]1)[/cyan] 🔍 Verificar status da sessão"
            "\n[cyan]2)[/cyan] 🔐 Fazer Login"
            "\n[cyan]3)[/cyan] 🧹 Fazer Logoff"
            "\n[cyan]4)[/cyan] 🌐 Abrir Navegador"
            "\n[cyan]5)[/cyan] 🪐 Abrir Session Manager"
            "\n[cyan]6)[/cyan] 🔑 Abrir Login Inicial (zera sessão)"
            "\n[cyan]7)[/cyan] ❌ Sair",
            border_style="magenta",
            padding=(1, 2),
        )
    )

def run_manager():
    # Python do venv (Windows ou Linux)
    venv_python = (
        os.path.join("venv", "Scripts", "python.exe")
        if os.name == "nt"
        else os.path.join("venv", "bin", "python")
    )

    manager_script = os.path.join("session_manager", "manager.py")

    if os.name == "nt":
        subprocess.Popen(f'start cmd /k "{venv_python} {manager_script}"', shell=True)
    else:
        subprocess.Popen([venv_python, manager_script])


def run_nav(headless=False):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Python sem terminal (Windows) / Python normal (Linux)
    venv_python = (
        os.path.join(BASE_DIR, "venv", "Scripts", "pythonw.exe")
        if os.name == "nt"
        else os.path.join(BASE_DIR, "venv", "bin", "python")
    )

    nav_script = os.path.join(BASE_DIR, "bots", "open_browser.py")

    headless_arg = "false" if not headless else "true"

    if os.name == "nt":
        subprocess.Popen([venv_python, nav_script, headless_arg], shell=False)
    else:
        subprocess.Popen([venv_python, nav_script, headless_arg])


# ============================================================
#   FIRST LOGIN (manual)
# ============================================================
def run_first_login():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    venv_python = (
        os.path.join(BASE_DIR, "venv", "Scripts", "python.exe")
        if os.name == "nt" else os.path.join(BASE_DIR, "venv", "bin", "python")
    )

    script = os.path.join(BASE_DIR, "_first_login.py")

    if os.name == "nt":
        subprocess.Popen(f'start cmd /k "{venv_python} {script}"', shell=True)
    else:
        subprocess.Popen([venv_python, script])




def run_menu():
    header()

    while True:
        mostrar_menu()

        opcao = Prompt.ask(
            "\n[bold yellow]👉 Escolha uma opção[/bold yellow]",
            choices=["1", "2", "3", "4", "5", "6", "7"],
            show_choices=False
        )

        match opcao:

            case "1":
                console.print("\n[cyan]⏳ Verificando sessão...[/cyan]")
                logado = check_login()
                console.print(
                    "\n[bold green]🟢 Sessão ativa![/bold green]\n"
                    if logado else
                    "\n[bold red]🔴 Sessão inativa![/bold red]\n"
                )

            case "2":
                if check_login():
                    console.print("\n[bold green]🟢 Você já está logado![/bold green]\n")
                    continue

                console.print("\n[cyan]🔐 Iniciando login...[/cyan]")
                email = Prompt.ask("[cyan]📧 Email[/cyan]")
                password = getpass("🔑 Senha: ")

                console.print("\n[cyan]🚀 Efetuando login...[/cyan]")
                login(email, password)

            case "3":
                console.print("\n[cyan]🧹 Limpando sessão...[/cyan]")
                ok = logout()
                console.print(
                    "[bold green]✔ Sessão encerrada![/bold green]\n"
                    if ok else
                    "[bold red]❌ Não havia sessão ativa.\n[/bold red]"
                )

            case "4":
                console.print("\n[bold cyan]🌐 Abrindo navegador...[/bold cyan]")
                run_nav()

            case "5":
                console.print("\n[bold green]🚀 Abrindo Session Manager...[/bold green]\n")
                run_manager()
              

            case "6":
                console.print("\n[bold magenta]🔑 Abrindo tela de primeiro login...[/bold magenta]\n")
                run_first_login()
           

            case "7":
                console.print("\n[bold red]👋 Encerrando Sessio... Até breve![/bold red]")
                break



run_menu()
