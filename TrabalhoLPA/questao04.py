#Lista que irá armazenar os dados dos funcionários e id global e q iniciará com meu RU
lista_funcionarios = []
id_global = 5321455

#Função onde o usuário irá cadastar os funcionários
def cadastrar_funcionario(id):
    print('---------------------------------------------')
    print('---------MENU CADASTRAR FUNCIONÁRIO----------')
    nome = input("Entre com o nome do Funcionário: ")
    setor = input("Entre com o Setor do Funcionário: ")
    salario = float(input("Entre com o Salário do Funcionário: "))

    #Os dados das informações cadastradas serão adicionadas ao seguinte dicionário
    funcionario = {'id':id, 'nome':nome, 'setor':setor, 'salario':salario}
    # Que por sua vez irá anezar os dados à lista de funcionários
    lista_funcionarios.append(funcionario.copy())

#Função de consulta de funcionarios, onde o usuário devera escolher a opção que deseja fazer a busca
def consultar_funcionarios():
    while True:
        print('---------------------------------------------')
        print('---------MENU CONSULTAR FUNCIONÁRIO----------')
        print('Escolha a opção desejada: ')
        print('1 - Consultar todos')
        print('2 - Consultar por ID')
        print('3 - Consultar por Setor')
        print('4 - Retornar ao menu')
        opc = input(">>")

        #Conforme opção escolhida, buscara os dados da lista por meio dos dicionários e listará as informações desejadas
        if opc == '1':
            for funcionario in lista_funcionarios:
                for chave in funcionario:
                    print(f'{chave}: {funcionario[chave]}')
        elif opc == '2':
            id_informado = int(input("Informe o id a ser buscado: "))
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_informado:
                    for chave in funcionario:
                        print(f'{chave}: {funcionario[chave]}')
        elif opc == '3':
            setor_informado = (input("Informe o setor a ser buscado: "))
            for funcionario in lista_funcionarios:
                if funcionario['setor'].lower() == setor_informado.lower():
                     for chave in funcionario:
                        print(f'{chave}: {funcionario[chave]}')
        elif opc == '4':
            return
        else:
            print("Opção inválida.")

#Função para remover um funcionário já cadastrado
def remover_funcionario():
    while True:
        print('---------------------------------------------')
        print('----------MENU REMOVER FUNCIONÁRIO-----------')

        #Irá buscar os dados do funcionário conforme id informado
        try:
            remover_id = int(input("Digite o ID do funcionário que deseja remover: "))

            #e em seguida caso a busca se confirme, os dados do funcionário serão removidos
            for funcionario in lista_funcionarios:
                if funcionario['id'] == remover_id:
                    lista_funcionarios.remove(funcionario)
                    print("Funcionário removido com sucesso!")
                    return
            if lista_funcionarios == [] :
                print('Não há funcionários cadastrados.')
                return
        except:
            print("ID inválido. Tente novamente.")

#Código Principal (Main)
print('Bem-vindo a Emprasa do Daniel Victor Sousa Mota.') #Mensagem de boas vindas


#Loop referente ao Menu principal, onde o usuario irá navegar pelas funções desejadas conferme opção selecionada
while True:
    print('---------------------------------------------')
    print('---------------MENU PRINCIPAL----------------')
    print('Escolha a opção desejada: ')
    print('1 - Cadastrar Funcionários')
    print('2 - Consultar Funcionário(s)')
    print('3 - Remover funcionário')
    print('4 - Sair')
    opc = input(">>")
    #Conforme opção selecionada, será chamado a função escolhida onde será iniciado o loop da função
    if opc == '1':
        cadastrar_funcionario(id_global)
        id_global += 1
    elif opc == '2':
        consultar_funcionarios()
    elif opc == '3':
        remover_funcionario()
    elif opc == '4':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")

