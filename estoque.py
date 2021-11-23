OPCOES_VALIDAS = 'CLBARS'


def menu_de_movimentos():
    print('----------------------MENU----------------------')
    MOVIMENTO_1 = '[C] - CADASTRAR'
    MOVIMENTO_2 = '[L] - LISTAR'
    MOVIMENTO_3 = '[B] - BUSCAR'
    MOVIMENTO_4 = '[A] - ATUALIZAR'
    MOVIMENTO_5 = '[R] - REMOVER PRODUTO'
    MOVIMENTO_6 = '[S] - SAIR'

    print(MOVIMENTO_1)
    print(MOVIMENTO_2)
    print(MOVIMENTO_3)
    print(MOVIMENTO_4)
    print(MOVIMENTO_5)
    print(MOVIMENTO_6)
    movimento = str(input('Infome o movimento: '))
    if movimento in OPCOES_VALIDAS:
        return movimento
    else:
        print('Esta operação não existe, tente novamente! ')
        return menu_de_movimentos()


list_nome = []
list_quantidade = []


def cadastrar():
    print('----------------------CADASTRAR PRODUTOS----------------------')
    produto = str(input('Digite o nome do produto: '))
    if produto in list_nome:
        print("Este produto já existe")
    else:
        list_nome.append(produto)
        quantidade = int(input("Digite a quantidade do produto: "))
        list_quantidade.append(quantidade)
        print("Produto cadastrado")


def listar():
    print('----------------------LISTAR PRODUTOS----------------------')
    if list_nome != [] and list_quantidade != []:
        lista_new = list_quantidade.copy()
        lista_new1 = list_nome.copy()
        ordem = input('Listar por nome ou quantidade: ').title()
        if ordem == 'Nome':
            lista_new1.sort()
            for i in range(len(list_nome)):
                new = lista_new1[i]
                if new in list_nome:
                    x = list_nome.index(new)
                    print(f'Produto: {new}')
                    print(f'Quantidade: {list_quantidade[x]}')
            return list_nome, list_quantidade
        else:
            for i in range(len(list_quantidade)):
                aux = lista_new.index(max(lista_new))
                print(f'produto: {lista_new1[aux]}')
                print(f'quantidade: {lista_new[aux]}')
                lista_new.pop(aux)
                lista_new1.pop(aux)


def buscar():
    print('----------------------BUSCAR PRODUTOS----------------------')
    escolha = str(input('Buscar por nome ou quantidade: '))
    if escolha == 'nome':
        nome = str(input('Digite o nome do produto: '))
        if nome in list_nome:
            aux = list_nome.index(nome)
            print(list_nome[aux])
            print(list_quantidade[aux])
        else:
            print('Este produto não está cadastrado:')
    else:
        quantidade = int(input('Digite a quantidade dos produtos que você quer visualizar: '))
        if quantidade in list_quantidade:
            for i in range(len(list_quantidade)):
                if quantidade == list_quantidade[i]:
                    print(list_nome[i])
                    print(list_quantidade[i])


def atualizar():
    print('----------------------ATUALIZAR PRODUTOS----------------------')
    nome_produto = str(input('Digite o nome do produto: '))
    quantidade_nova = int(input('Digite a quantidade do produto: '))
    if nome_produto in list_nome:
        new = list_nome.index(nome_produto)
        list_quantidade[new] = quantidade_nova
        print(list_nome[new])
        print(list_quantidade[new])
    else:
        return 'Este produto não está cadastrado'


def remover_produto():
    print('----------------------REMOVER PRODUTO----------------------')
    produto = str(input('Digite o nome do produto: '))
    if produto in list_nome:
        aux = list_nome.index(produto)
        list_quantidade.pop(aux)
        list_nome.pop(aux)
        print('Produto removido')
    else:
        print('Este produto não está cadastrado')


if __name__ == '__main__':
    movimento = menu_de_movimentos()
    while movimento in OPCOES_VALIDAS:
        if movimento == 'C':
            cadastrar()
            movimento = menu_de_movimentos()
        elif movimento == 'L':
            listar()
            movimento = menu_de_movimentos()
        elif movimento == 'B':
            buscar()
            movimento = menu_de_movimentos()
        elif movimento == 'A':
            atualizar()
            movimento = menu_de_movimentos()
        elif movimento == 'R':
            remover_produto()
            movimento = menu_de_movimentos()
        elif movimento == 'S':
            print('Operação encerrada com sucesso!')
            break
        else:
            print('Esta operação não existe, tente novamente!')
            movimento = menu_de_movimentos()




