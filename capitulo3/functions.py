# função preencherInventario
def preencherInventario(lista):
    resposta = "S"
    while resposta == "S":
        equipamento = [input("Equipamento: "), float(input("Valor: ")), int(input("Número serial: ")),
                       input("Departamento: ")]
        lista.append(equipamento)
        resposta = input("Digite \"S\" para continuar: ").upper()


# funcao exibirInventario
def exibirInventario(lista):
    for elemento in lista:
        print("Nome..........: ", elemento[0])
        print("Valor.........: ", elemento[1])
        print("Serial......: ", elemento[2])
        print("Departamento: ", elemento[3])


# funcao localizarPorNome()
def localizarPorNome(lista):
    busca = input('\nDigite o nome do equipamento que deseja buscar: ')
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor.......: ", elemento[1])
            print("Serial......: ", elemento[2])
            print("Departamento: ", elemento[3])


# funcao depreciarPorNome
def depreciarPorNome(lista, porc):
    depreciacao = input('\nDigite o nome do equipamento que será depreciado: ')
    for elemento in lista:
        if depreciacao == elemento[0]:
            print('Valor antigo: ', elemento[1])
            elemento[1] = elemento[1] * (1 - porc / 100)
            print('Novo valor: ', elemento[1])


# funcao excluirPorSerial
def excluirPorSerial(lista):
    serial = int(input('\nDigite o serial do equipamento que será excluído: '))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
    return "Itens excluídos."


def menorValor(lista):
    return min(lista)


def maiorValor(lista):
    return max(lista)


def valorTotal(lista):
    return sum(lista)


def totalEquipamentos(lista):
    return len(lista)


# funcao resumirValores
def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", maiorValor(valores))
        print("O equipamento mais barato custa: ", menorValor(valores))
        print("O valor total dos equipamentos: ", valorTotal(valores))
        print("O número total de equipamentos: ", totalEquipamentos(valores))
