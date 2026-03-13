from rich import print
class Caneta:
    def __init__(self, cor, frase):
        self.cor = cor
        self.tampada = True
        self.frase = frase
    def escrever(self):
        if self.cor == 'azul':
            return f'[blue]{self.frase}[/blue]'
        elif self.cor == 'vermelha':
            return f'[red]{self.frase}[/red]'
        elif self.cor == 'verde':
            return f'[green]{self.frase}[/green]'
        elif self.cor == 'amarela':
            return f'[yellow]{self.frase}[/yellow]'
        else:
            return self.frase
obj_frase = input('Digite uma frase: ')
obj_cor = input('Digite a cor da caneta (azul, vermelha, verde ou amarela): ')
caneta = Caneta(obj_cor, obj_frase)
print(caneta.escrever())
    