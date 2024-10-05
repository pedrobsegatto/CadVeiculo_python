import os, time
from veiculo import Veiculo
from carro import Carro
from moto import Moto
from caminhao import Caminhao
#BD em memória
listaVeiculos = [
    Carro("Toyota", 'Etios', 'ABC', 2022, 4),
    Moto("Honda", "CG 160", 'DEF', 2008, 250),
    Caminhao("volvo", "FH 540", 'GHI', 1995, 2, 6000)
]

def limparTela(tempo):
    time.sleep(tempo)
    os.system("cls")


def placa_existe(placa):
    for veiculo in listaVeiculos:
        if veiculo.get_placa() == placa:
            return True
    return False


def cadastrar():

    tipo = input('''\n(1) Carro - (2) Moto - (3) Caminhão
Qual o tipo de veículo: ''')
    if tipo not in ["1","2","3"]:
        print("Tipo inválido. Tente novamente")
        limparTela(1)
        return
    

    marca = input("Digite a marca:")
    modelo = input("Digite o modelo:")
    placa = input("Digite o placa:")
    ano = input("Digite o ano:")

    if not marca or not modelo or not placa or not ano:
        print("\nTodos os campos são obrigatórios. Tente novamente.")
        limparTela(2)
        return
    
    try:
        int(ano)
    except:
        print("Ano inválido. Tente novamente.")
        limparTela(1)
        return
    if ano == '0':
        print("\nO ano não pode ser '0'.")
        limparTela(2)
        return
    
    if placa_existe(placa):
        print("\nJá existe um veículo com essa placa.")
        limparTela(2)
        return

    if tipo == '1':
        nPortas = input('Digite o número de portas:')
        if not nPortas or nPortas == '0':
            print("\nO número de portas não pode ser '0'.")
            limparTela(1)
            return
        veiculoAdd = Carro(marca, modelo, placa, ano, nPortas)

    elif tipo == '2':
        cilindradas = input('Digite as cilindradas: ')
        if not cilindradas:
            print("\nTodos os campos são obrigatórios. Tente novamente.")
            limparTela(1)
        veiculoAdd = Moto(marca, modelo, placa, ano, cilindradas)
    
    elif tipo == '3':
        nPortas = input('Digite o número de portas: ')
        capacidade = input('Digite a capacidade: ')
        if not nPortas or nPortas == '0' or not capacidade:
            print("\nTodos os campos são obrigatórios e o número de portas não pode ser '0'.")
            limparTela(2)
        veiculoAdd = Caminhao(marca, modelo, placa, ano, nPortas, capacidade)

    listaVeiculos.append(veiculoAdd)
    limparTela(1)
    print("Veiculo registrado!")
    limparTela(1)
    

def listar():
    os.system('cls')
    if len(listaVeiculos) == 0:
        print ("Não existem veículos cadastrados\n")
    else:
        for n, veiculo in enumerate(listaVeiculos):
            print(f"Veículo: {n + 1}")
            print(f" - {veiculo}")
            print()


def pesquisar():
    placa = input("Digite a placa que deseja pesquisar:")
    encontrou = False
    for veiculo in listaVeiculos:
        if veiculo.get_placa() == placa:
            print(veiculo)
            encontrou = True
    if encontrou == False:
        print("\nVeículo não encontrado\n")
    limparTela(1)


def excluir():
    listar()
    print("Digite a placa que deseja excluir:")
    placa = input()
    encontrou = False
    for veiculo in listaVeiculos:
        if veiculo.get_placa() == placa:
            listaVeiculos.remove(veiculo)
            encontrou = True
            break
    if encontrou:
        print("\nVeículo excluído\n")
    else:
        print("\nVeículo não encontrado\n")
    limparTela(1)

os.system('cls')
while True:
    print("Escolha uma das opções:")
    print("1 - Cadastrar Veículo")
    print("2 - Listar Veículos")
    print("3 - Pesquisar Veículo")
    print("4 - Excluir Veículo")
    print("0 - SAIR\n")
    opcao = int(input("Opção: "))
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        pesquisar()
    elif opcao == 4:
        excluir()
    elif opcao == 0:
        break
    else:
        print("Opção Inválida")
        limparTela(1)