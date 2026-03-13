class Churrasco:
    def __init__(self, q, qc, pc, ct):# q = quantidade de pessoas, qc = quantidade de carne por pessoa, pc =  preço da carne, ct = custo total
        self.q = q
        self.qc = qc
        self.pc = pc
        self.ct = ct
    def calcular_custo_total(self):
        self.ct = self.q * self.qc * self.pc
        print(f"O custo total do churrasco é: {self.ct} AOA")
    def info(self):
        print(f"Quantidade de pessoas: {self.q} Quantidade de carne por pessoa: {self.qc} Preço da carne: {self.pc} Custo total: {self.ct}")
obj_churras = Churrasco(11, 3, 1500, 0)
obj_churras.calcular_custo_total()
obj_churras.info()