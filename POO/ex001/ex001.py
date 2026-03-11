# class Molde:
#     def __init__(self): nao tem como mudar nada pq o so tamo passando o self, vulgo o proprio objeto
#         self.atributo1 = 'Valor do atributo 1'
#         self.atributo2 = 'Valor do atributo 2'
#         self.atributo3 = 'Valor do atributo 3'
#     def metodo1(self):
#         self.atributo1 = 'Valor do atributo 1 modificado'
#         print('Método 1 executado')
#     def metodo2(self):
#         self.atributo2 = 'Valor do atributo 2 modificado'
#         print('Método 2 executado')
#     def metodo3(self):
#         self.atributo3 = 'Valor do atributo 3 modificado'
#         print('Método 3 executado')
# objeto = Molde()
# print(objeto.metodo1())
# print(objeto.metodo2())
# print(objeto.metodo3())
# print(objeto.atributo1)
# print(objeto.atributo2)
# print(objeto.atributo3)
class Pessoa:
    """
    Docstring for Pessoa
    A classe Pessoa representa uma pessoa com nome e idade, e possui métodos para falar e envelhecer.
     - Atributos:
        - nome: O nome da pessoa.
        - idade: A idade da pessoa.
        - Métodos:
        - falar(): Imprime uma mensagem indicando que a pessoa está falando.
        - envelhecer(): Incrementa a idade da pessoa em 1 e imprime a nova idade.
    """
    def __init__(self, nome, idade):#aqui nos ta passando o self, que seria as caracteristicas basicas do objeto, nome e idade seria mais especificos de cada objeto, ou seja, cada um tem o seu, portanto nos passa isso como atributo na funçao
        self.nome = nome
        self.idade = idade
    def falar(self):
        print(f"{self.nome} está falando.")
    def envelhecer(self):
        self.idade += 1
        print(f"{self.nome} envelheceu e agora tem {self.idade} anos.")
    def __str__(self):
        return f"{self.nome}, {self.idade} anos"
pessoa1 = Pessoa("João", 30)#nos pegou a variavel pessoa1, TRANSformou em um objeto com a classe pessoa e passou os atributos especificos(nome e idade)
pessoa1.falar()
pessoa1.envelhecer()
print(pessoa1.__doc__)
print(pessoa1)