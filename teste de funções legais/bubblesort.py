def bubble_sort(lista):
    """
    Docstring for bubble_sort
    
    :param lista: O array a ser ordenado
    :return: O array ordenado
    Uma função recursiva que ordena o array pegando os elementos proximos e comparando os ditos cujos.
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
# Exemplo de uso
n = int(input('Quantos números deseja inserir? '))
lista = []
for i in range(n):
    numero = int(input(f'Número {i + 1}: '))
    lista.append(numero)
resultado = bubble_sort(lista)
print(f'Lista ordenada: {resultado}')
#pq nao usa sort??
#sort funciona so com listas, se eu quiser organizar um banco de dados?? 
#moggado