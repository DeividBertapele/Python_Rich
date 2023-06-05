from rich import print
from rich.layout import Layout
from rich.panel import Panel

layout = Layout()

layout.split_column(
    Layout(Panel("Meu app", style="on green"), ratio=3),
    Layout(name="topo", ratio=2),
    Layout(name="baixo", ratio=2),
    Layout(Panel("Criador: Python", style="red"), ratio=3)

)

layout['topo'].split_row(
    Layout(Panel('Esquerda')),
    Layout(Panel('Direita')),
)
print(layout)
