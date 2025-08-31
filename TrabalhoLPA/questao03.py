#Função que exibirá ao usuário as opções de camisetas e seus valores, e irá perguntar qual modelo ele deseja
def escolha_modelo():
    while True:
        print('Modelos disponíveis: ')
        print('MCS - Manga Curta Simple, valor unitário: R$ 1.80')
        print('MLS - Manga Longa Simple, valor unitário: R$ 2.10')
        print('MCE - Manga Curta com Estampa, valor unitário: R$ 2.90')
        print('MLE - Manga Longa com Estampa, valor unitário: R$ 3.20')

        mod = input("Escolha o modelo desejado (MCS/MLS/MCE/MLE): ").upper()

        #Valor do produto será definido conforme seleção de modelos informados
        if mod == "MCS":
            return 1.80
        elif mod == "MLS":
            return 2.10
        elif mod == "MCE":
            return 2.90
        elif mod == "MLE":
            return 3.20
        else:
            print("Modelo inválido! Tente novamente.")
            continue

#Função que irá perguntar quantas camisetas o usuário deseja
def num_camisetas():
    while True:
        try:
            num = int(input("Informe o número de camisetas que deseja: "))
        except:
            print("O valor informado deve ser númerico.")
            continue

        #baseado na quantidade selecionada calculará o desconto dísponivel
        if num < 20:
            return num
        elif num >= 20 and num < 200:
            desconto = num - (num*(5/100))
            return desconto
        elif num >= 200 and num < 2000:
            desconto = num - (num*(7/100))
            return desconto
        elif num >= 2000 and num < 20000:
            desconto = num - (num*(12/100))
            return desconto
        else:
            print("Não aceitamos tantas camisetas de uma vez. Tente novamente.")
            continue

#Função que irá informar ao usúario as opções de frete e seus valores
def frete():
    while True:
        print('Opções de Frete: ')
        print('1 - Frete por Transportadora: R$ 100.00')
        print('2 - Frete por Sedex: R$ 200.00')
        print('0 - Retirar pedido na Fábrica: R$ 0.00')

        opFrete = input("Escolha o tipo de Frete (0, 1, 2): ").upper()

        #Irá retornar o valor do frete conforme opção selecionada
        if opFrete == "1":
            return 100
        elif opFrete == "2":
            return 200
        elif opFrete == "0":
            return 0
        else:
            print("Opção de Frete inválida! Tente novamente.")
            continue

#Aqui é o código principal (Main)
print("Bem-vindo a Fábrica de Camisetas do Daniel Victor Sousa Mota ") #Mensagem de boas vindas ao usuário

#As funções serão chamadas por essas variáveis, onde aparecerá os inputs de opções de seleção ao usuário
modelo1 = escolha_modelo()
num1 = num_camisetas()
frete1 = frete()

total = (modelo1 * num1) + frete1 #Variável para calcular o valor total do pedido

#Mensagem informando os valores do pedido ao usuário
print(f"Valor Total do pedido: R$ {total:.2f} (Modelo: R$ {modelo1:.2f} * Quantidade (com desconto): R$ {num1:.2f} + frete: R$ {frete1:.2f}")



