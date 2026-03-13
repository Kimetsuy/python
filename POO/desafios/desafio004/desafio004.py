class Livro:
    def __init__(self, titulo, qp):# qp = quantidade de paginas
        self.titulo = titulo
        self.qp = qp
    def passar_pagina(self):
        if self.qp > 0:
            self.qp -= 1
            print(f'Passou para a próxima página. Restam {self.qp} páginas.')
        else:
            print('Você já terminou o livro!')
livro1 = Livro('saficas', 24)
for i in range(25):
    livro1.passar_pagina()