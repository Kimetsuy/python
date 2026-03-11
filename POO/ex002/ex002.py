class Conta:
    """
    Docstring for Conta
    Uma classe com 3 atributos: numero, titular e saldo, e 2 métodos: depositar() e sacar().
        - Atributos:
            - numero: O número da conta.
            - titular: O nome do titular da conta.
            - saldo: O saldo atual da conta.
        - Métodos:
            - depositar(valor): Adiciona o valor ao saldo da conta.
            - sacar(valor): Subtrai o valor do saldo da conta, se houver saldo suficiente. Caso contrário, imprime uma mensagem de saldo insuficiente.
    """
    def __init__(self, cad, tit, saldo):
        self.numero = cad
        self.titular = tit
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito realizado. Novo saldo: {self.saldo}")
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque realizado. Novo saldo: {self.saldo}")
            return True
        else:
            print("Saldo insuficiente.")
            return False
    def __str__(self):
        return f"Conta {self.numero}: {self.titular} - Saldo: {self.saldo}"
pessoa1 = Conta('123', 'Pedro', 1000)
pessoa1.depositar(500)
pessoa1.sacar(2000000)
print(pessoa1)