import tkinter as tk
janela = tk.Tk()
janela.title("Algoritmo de Euclides")
janela.geometry("300x200")
def euclides(a, b):
    """
    Docstring for euclides
    
    :param a: Número inteiro
    :param b: Número inteiro
    :return: O máximo divisor comum (MDC) de a e b
    essa função usa o algoritmo de Euclides, que serve pra achar o MDC de dois números INTEIROS 
    """
    if b == 0:
        return a
    else:
        return euclides(b, a % b)
# Exemplo de uso
janela.entry1 = tk.Entry(janela)
janela.entry1.pack()
janela.entry2 = tk.Entry(janela)
janela.entry2.pack()
n1 = janela.entry1.get()
n2 = janela.entry2.get()
janela.button = tk.Button(janela, text="Calcular MDC", command=lambda: calcular_mdc())
janela.button.pack()
def calcular_mdc():
    n1 = int(janela.entry1.get())
    n2 = int(janela.entry2.get())
    resultado = euclides(n1, n2)
    janela.label_resultado = tk.Label(janela, text=f"O MDC de {n1} e {n2} é {resultado}")
    janela.label_resultado.pack()
janela.mainloop()