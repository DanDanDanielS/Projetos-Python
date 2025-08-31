print('----Bem-vindo a loja de marmitas do Daniel Victor Sousa Mota-----')
print('---------------------- Cardápio----------------------------------')
print('-----------------------------------------------------------------')
print('---|  Tamanho  |  Bife acebolado(BA)  |  Filé de frango(FF)  |---')
print('---|     P     |       R$ 16.00       |        R$ 15.00      |---')
print('---|     M     |       R$ 18.00       |        R$ 17.00      |---')
print('---|     G     |       R$ 22.00       |        R$ 21.00      |---')
print('-----------------------------------------------------------------')

valorTotal = 0 #Acumulador do valor total caso o clente adicione mais pedidos

#Irá perguntar ao usuário quais opções de sabor e tamanho ele deseja
while True:
    sabor = input("Escolha o sabor desejado (BA/FF): ").upper()
    if sabor != "BA" and sabor != "FF":
        print("Sabor inválido, tente novamente.")
        continue


    tamanho = input("Escolha o tamanho desejado (P/M/G): ").upper()
    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        print("Tamanho inválido, tente novamente.")
        continue


    #Verifica qual será o valor do pedido de acordo com o tamanho selecionado
    if sabor == "BA":
        if tamanho == "P":
            valor = 16
        elif tamanho == "M":
            valor = 18
        else:
            valor = 22
    else:
        if tamanho == "P":
            valor = 15
        elif tamanho == "M":
            valor = 17
        else:
            valor = 21

    valorTotal += valor #Valor será adicionado ao acumulador

    print(f'Você pediu um {sabor} no tamanho {tamanho}: R$ {valor:.2f}')


    pergunta = input("Deseja pedir mais alguma coisa? (S/N):").upper() #Pergunta se  o usuário deseja pedir mais
    if pergunta == "S":
        continue
    else:
        break

print(f"O valor total do pedido é de R$ {valorTotal:.2f}") #Informa ao usuário o valor total do pedido














