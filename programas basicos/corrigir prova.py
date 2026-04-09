quant = int(input("Quantas questões a prova tem? "))
respostas = []
for i in range(quant):
    resposta = input(f"O que você botou na questão {i+1}: ")
    respostas.append(resposta)
gabarito = []
for i in range(quant):
    resposta = input(f"Gabarito da questão {i+1}: ")
    gabarito.append(resposta)
acertos = 0
for i in range(quant):
    if respostas[i] == gabarito[i]:
        acertos += 1
print(f"Você acertou {acertos} questões.")
print(f'A sua porcentagem de acertos foi de {(acertos/quant)*100:.2f}%')