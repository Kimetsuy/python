from rich import print
class Funcionario:
    """
    Docstring for Funcionario
    Atributos:
    nome - nome do funcionario
    setor - setor onde o funcionario trabalha
    cargo - cargo do funcionario
    metodos
    __init__ - metodo construtor da classe
    se.apresentar - metodo que permite que o funcionario se apresente
    """
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def se_apresentar(self):
        print(f"Olá, meu nome é {self.nome}, trabalho no setor de {self.setor} e meu cargo é {self.cargo}.")
obj_teste = Funcionario("João", "TI", "Analista de Sistemas")
obj_teste.se_apresentar()
print(obj_teste.__doc__)
obj_teste1 = Funcionario("Fabio", "Fortnite", "Gaymer")
obj_teste1.se_apresentar()