import time
import os
from rich.console import Console
from rich.panel import Panel

console = Console()

class Menu:
    @staticmethod
    def limpar():
        os.system("cls" if os.name == "nt" else "clear")


    @staticmethod
    def tela_inicial():
        Menu.limpar()

        console.print("\n")
        console.print("[bold yellow]UNIVERSIDADE FEDERAL DO PIAUÍ[/bold yellow]", justify="center")
        console.print("[cyan]Bacharelado em Sistemas de Informação[/cyan]", justify="center")

        console.print("\n[bold white]Disciplina:[/bold white] Programação Orientada a Objetos", justify="center")
        console.print("[bold white]Professor:[/bold white] Thiago José Barbosa Lima", justify="center")
        console.print("[bold white]Aluna:[/bold white] Allana Camily de Sousa Martins", justify="center")

        console.print("\n[bold green]TRABALHO[/bold green]", justify="center")
        console.print("[yellow]Pokédex com API Pokémon[/yellow]", justify="center")

        console.print("\n")
        console.print("[cyan]Inicializando sistema[/cyan]", justify="center", end="")

        for _ in range(5):
            time.sleep(0.5)
            console.print(".", end="")

        time.sleep(1)
        Menu.limpar()

    @staticmethod
    def mostar_logo():
        console.print(
            Panel.fit(
            "[bold yellow]POKÉDEX[/bold yellow]\n"
            "[cyan]Sistema de Consulta Pokémon[/cyan]",
            title="UFPI"
        )
    )
    
    @staticmethod
    def mostrar_menu():
        console.print("\n[bold green]MENU PRINCIPAL[/bold green]")
        console.print("[1] Consultar e cadastrar Pokémon")
        console.print("[2] Listar Pokémons cadastrados")
        console.print("[3] Exibir dados de um Pokémon")
        console.print("[4] Exibir imagem de um Pokémon")
        console.print("[5] Quantidade cadastrada")
        console.print("[0] Sair")

    def tela_saida():
        Menu.limpar()
    
        console.print("\n")
        console.print("[bold yellow]Encerrando a Pokédex[/bold yellow]", justify="center")
        console.print("[white]Obrigado por utilizar o sistema.[/white]", justify="center")

        console.print("\n[cyan]Finalizando sistema[/cyan]", justify="center", end="")

        for _ in range(5):
            time.sleep(0.5)
            console.print(".", end="")

        console.print("\n")
        console.print("[bold green]Até logo![/bold green]", justify="center")

        time.sleep(2)

    @staticmethod
    def sucesso(msg):
        console.print(f"\n[bold green]✓ {msg}[/bold green]")

    @staticmethod
    def erro(msg):
        console.print(f"\n[bold red]✗ {msg}[/bold red]")