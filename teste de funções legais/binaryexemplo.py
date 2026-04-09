def busca_binaria(lista, alvo):
    """
    Docstring for busca_binaria
    
    :param lista: O array onde a busca será realizada
    :param alvo: O elemento a ser buscado
    :return: O índice do elemento encontrado ou uma mensagem de erro
    """
    if len(lista) <= 0:
        return f'O elemento {alvo} não está presente na lista.'
    a_lista_e_par  = len(lista) % 2 == 0
    if a_lista_e_par:
        meio = len(lista) // 2
    else:
        meio = (len(lista) + 1) // 2
        return meio - 1
    if lista[meio] == alvo:
        return (f'O elemento {alvo} está no índice {meio}')
    elif lista[meio] < alvo:
        return busca_binaria(lista[meio + 1:], alvo)
    elif lista[meio] > alvo:
        return busca_binaria(lista[:meio], alvo)
# Exemplo de uso
n = int(input('Quantos números deseja inserir? '))
lista = []
for i in range(n):
    numero = int(input(f'Número {i + 1}: '))
    lista.append(numero)
alvo = int(input('Qual número deseja buscar? '))
resultado = busca_binaria(lista, alvo)
print(f'O número que você busca está no índice: {resultado}')
print(busca_binaria.__doc__)