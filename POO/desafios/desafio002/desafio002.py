class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def mostrar_etiqueta(self):
        print(f"nome do produto: {self.nome} preço do produto: {self.preco}")
obj_cadeira = Produto('Jenifer', '2 AOA')
obj_cadeira.mostrar_etiqueta()