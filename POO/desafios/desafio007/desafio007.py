class ControleRemoto:
    def __init__(self, canal, volume, estado):
        self.canal = canal
        self.volume = volume
        self.estado = estado
    def ligar(self):
        self.estado = 'Ligado'
    def desligar(self):
        self.estado = 'Desligado'
    def aumentar_volume(self):
        self.volume += 1
    def diminuir_volume(self):
        self.volume -= 1
    def mudar_canal(self, canal):
        self.canal = canal
controle = ControleRemoto(1, 10, 'Desligado')
controle.ligar()
print(f'Canal: {controle.canal}, Volume: {controle.volume}, Estado: {controle.estado}')
controle.aumentar_volume()
print(f'Canal: {controle.canal}, Volume: {controle.volume}, Estado: {controle.estado}')
controle.mudar_canal(5)
print(f'Canal: {controle.canal}, Volume: {controle.volume}, Estado: {controle.estado}')
controle.desligar()

        