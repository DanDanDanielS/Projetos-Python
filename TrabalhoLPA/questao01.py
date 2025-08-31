print('Bem-vindo a Loja do Daniel Victor Sousa Mota RU: 5321455')

valorPedido = float(input('Informe o valor do Pedido: ')) #Irá pedir ao usuário o valor do pedido
qtdParcelas = int(input('Informe a quantidade de Parcelas: ')) #Irá pedir ao usuário a quantidade de parcelas

#Ira calcular o juros baseado na quantidade de parcelas
if qtdParcelas < 4:
    juros = 0/100
elif qtdParcelas >= 4 and qtdParcelas < 6:
    juros = 4/100
elif qtdParcelas >= 6 and qtdParcelas < 9:
    juros = 8/100
elif qtdParcelas >= 9 and qtdParcelas < 13:
    juros = 16/100
else:
    juros = 32/100

#Calculará o valor da parcela e do valor total parcelado
valorDaParcela = (valorPedido * (1+juros)) / qtdParcelas
valorTotalParcelado = valorDaParcela * qtdParcelas

#Apresenta ao usuário o resultado dos valores finais
print(f'O valor da Parcela é: R$ {valorDaParcela:.2f}')
print(f'O valor total Parcelado é: R$ {valorTotalParcelado:.2f}')
