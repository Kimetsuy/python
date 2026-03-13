class Gamer:
    def __init__(self, nome, nick, jf): #jf = jogos favoritos
        self.nome = nome
        self.nick = nick
        self.jf = jf

    def mostrar(self):
        print(f'Nome: {self.nome}')
        print(f'Nick: {self.nick}')
        print('Jogos Favoritos:')
        for jogo in self.jf:
            print(f'- {jogo}')
nome_do_gamer = input('Digite o nome do gamer: ')
nick_do_gamer = input('Digite o nick do gamer: ')
jogos_favoritos = []
while True:
    jogo = input('Digite um jogo favorito (ou "sair" para finalizar): ')
    if jogo.lower() == 'sair':
        break
    jogos_favoritos.append(jogo)
gamer = Gamer(nome_do_gamer, nick_do_gamer, jogos_favoritos)
gamer.mostrar()