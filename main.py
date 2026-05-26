estoque = {
    'condicionador': {'valor em R$': 10 , 'quantidade': 2},
    'shampoo': {'valor em R$': 8.50 , 'quantidade': 6},
    'sabonete': {'valor em R$': 3.50 , 'quantidade': 10}
} # Criação de discionário dentro de discionários para uma melhor identificação dos valores.

while True: # Criação de um loop, para que o código não pare de 'rodar' após a priemira iteração e reinicie todas as alterações feitas na lista.
    print('\n Oque deseja fazer no Sistema de Estoque? \n adicionar, atualizar, remover, visualizar ou sair')
    acao = input('\n Digite a opção: ')

    while acao not in ['adicionar', 'atualizar', 'remover', 'visualizar', 'sair']: # outro loop, para que o usuario use apenas as opções fornecidas no menu.
        print('\nEscolha entre: \n adicionar, atualizar, remover, visualizar ou sair')
        acao = input('\nDigite a opção: ')

    if (acao == 'adicionar'):
        novo_produto = input('\n Nome do Produto: ')
        if novo_produto in estoque: # o segundo if é feito para adicionar apenas o produto, caso já exista na lista, e a quantidade, pois não faz sentido pedir o valor de um produto que já tem um valor.
            print(f'\n {novo_produto} já tem no estoque! \n')
            quantidade_produto = int(input('Quantidade a ser adicionada: '))
            estoque[novo_produto]['quantidade'] += quantidade_produto
    
        else: # caso o produto não exista na lista, pede-se o valor e quantidade a ser adicionada.
            valor_produto = float(input('Valor do Produto em R$: '))
            quantidade_produto = int(input('Quantidade a ser adicionada: '))
            estoque[novo_produto] = {'valor em R$' : valor_produto , 'quantidade': quantidade_produto}

        print(f'\n Lista após a adição:\n {estoque}')

    elif (acao == 'atualizar'):
        print(f'\n Lista atual: \n {estoque}')
        atualizar_produto = input('\n Nome do produto que deseja atualizar: ')
        if atualizar_produto in estoque: # se o produto existir na lista, mostra-se o valor e a quantidade que tem no estoque, e pode alterar essas variáveis. Caso não queira, repita o valor que aparece na interface.
            print(f"\n Valor atual do produto em R$: {estoque[atualizar_produto]['valor em R$']}")
            print(f"Quantidade atual do produto em estoque: {estoque[atualizar_produto]['quantidade']} \n")
            atualizar_valor = float(input('Valor atualizado em R$: '))
            atualizar_quantidade = int(input('Quantidade atualizada: '))
            estoque[atualizar_produto] = {'valor em R$': atualizar_valor , 'quantidade': atualizar_quantidade}

            print(f'\n Lista após a atualização:\n {estoque}')

        else: # caso o produto não exista, o código retorna ao menu inicial.
            print('\n Não existe esse produto na lista!')

    elif (acao == 'remover'):
        print(f'\n Lista antes remoção:\n {estoque} \n')
        remover_produto = input('Digite qual item deseja remover: ')
        if remover_produto in estoque:
            estoque.pop(remover_produto) # o usuário digita o produto que deseja remover, caso esteja na lista, a função '.pop' remove o produto e os valores atribuidos a ele.
            print(f'\n Lista após remoção:\n {estoque}')

        else: # caso o produto não exista, o código retorna ao menu inicial.
            print('\n Não existe esse produto na lista!')
    

    elif (acao == 'visualizar'): # visualiza a lista inicial ou com as modificações feitas.
        print(f'\n Estoque atual:\n {estoque}')

    elif (acao == 'sair'):
        print('\n Vocè saiu do sistema! \n')
        break # o loop para aqui.

    continua = input('\n Deseja continuar no sistema? (sim / nao): ') # pergunta se o usuário deseja continuar no sistema
 
    while continua not in ['sim' , 'nao']: # mais um loop, para que o usuário possa escolher apenas entre 'sim' ou 'nao' para continuar no sistema.
        print('\n Digite somente as opções "sim" ou "nao"')
        continua = input('Deseja continuar no sistema? (sim / nao): ')

    if continua == 'nao': # caso a reposta seja 'nao', encerra o programa aqui.
        print('\n Digite "sair" no menu principal!')
