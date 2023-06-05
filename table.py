# Criar e personalizar as tabelas


from rich.table import Table
from rich.console import Console

console = Console()

# Adicionar o dashboard
console.print("Bem vindo ao meu dashboard", style="bold green")


# Criar a tabela (table)
table = Table(title="Filmes Favoritos")

table.add_column("ID", justify="left", style="red")
table.add_column("Nome", style="blue")
table.add_column("Idade", style="green")
table.add_row("1", "Python", "1000")
table.add_row("2", "Python", "5000")

console.print(table)


# Executar o dashboard
console.print("Este é meu dashboard final", style="bold blue")