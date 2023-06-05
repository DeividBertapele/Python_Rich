# criar log do progresso

from time import sleep

from rich.console import Console

console = Console()


def criar_arquivos():
    for i in range(10):
        with open(f'arquivo{i}.txt', 'w') as file:
            file.write("Criamos um novo arquivo")
            sleep(1)
            console.log(f"Tarefa {i} finalizada!")


with console.status("[green]Realizando a tarefa.....[/]") as arquivo:
    criar_arquivos()
