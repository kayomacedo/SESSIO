from getpass import getpass
import os
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


def mostrar_menu():
    console.print(
        Panel.fit(
            "[bold magenta]🛰 MENU PRINCIPAL — Sessio[/bold magenta]\n"
            "\n[cyan]1)[/cyan] 🔍 Verificar status da sessão"
            "\n[cyan]2)[/cyan] 🔐 Fazer Login"
            "\n[cyan]3)[/cyan] 🧹 Fazer Logoff"
            "\n[cyan]4)[/cyan] ⚙️ Abrir Navegador"
            "\n[cyan]5)[/cyan] 🪐 Abrir Session Manager"
            "\n[cyan]6)[/cyan] ❌ Sair",
            border_style="magenta",
            padding=(1, 2),
        )
    )


def run_menu():
    header()

    while True:
        mostrar_menu()
        opcao = Prompt.ask("\n[bold yellow]👉 Escolha uma opção[/bold yellow]")

        match opcao.lower():
            # --------------------------------------
            # VERIFICAR STATUS
            # --------------------------------------
            case "1":
                console.print("\n[cyan]⏳ Verificando sessão...[/cyan]")
                logado = check_login()

                if logado:
                    console.print("\n[bold green]🟢 A sessão está ativa![/bold green]\n")
                else:
                    console.print("\n[bold red]🔴 A sessão NÃO está ativa![/bold red]\n")

            # --------------------------------------
            # LOGIN
            # --------------------------------------
            case "2":
                if check_login():
                    console.print("\n[bold green]🟢 O usuário já está logado![/bold green]\n")
                    continue

                email = Prompt.ask("[cyan]📧 Digite seu email[/cyan]")
                password = getpass("🔑 Digite sua senha: ")
                console.print("\n[cyan]🚀 Realizando login...[/cyan]\n")
                login(email, password)

            # --------------------------------------
            # LOGOUT
            # --------------------------------------
            case "3":
                console.print("[cyan]🧹 Limpando sessão atual...[/cyan]")
                ok = logout()
                if ok:
                    console.print("[bold green]✔ Sessão removida com sucesso![/bold green]\n")
                else:
                    console.print("[bold red]❌ Nenhuma sessão encontrada.\n[/bold red]")

            # --------------------------------------
            # CONFIGURAÇÃO
            # --------------------------------------
            case "4":
                console.print("\n[bold cyan] Abrir Navegador[/bold cyan]")
                open_nav()



            # --------------------------------------
            # RODAR MANAGER EM OUTRO TERMINAL
            # --------------------------------------
            case "5":
                console.print("\n[bold green]🚀 Abrindo Session Manager em outro terminal...[/bold green]\n")
                os.system('start cmd /k "venv\\Scripts\\python session_manager\\manager.py"')
                break

            # --------------------------------------
            # SAIR
            # --------------------------------------
            case "6":
                console.print("\n[bold red]👋 Encerrando Sessio... Até logo![/bold red]")
                break

            case _:
                console.print("[bold red]❌ Opção inválida! Tente novamente.\n[/bold red]")


run_menu()
