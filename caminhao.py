from veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, placa, ano, n_portas, comprimento, capacidade):
        super().__init__(marca, modelo, placa,ano)
        self.__n_portas = n_portas
        self.__comprimento = comprimento
        self.__capacidade = capacidade
    #Sobrescrita do método __str__()
    def __str__(self):
        #Invoco o método __str__() da SUPERCLASSE (Veiculo)
        # Armazeno o retorno na variável "retorno"
        retorno = super().__str__()
        #Retorno a concatenação do valor da variável
        # "retorno" com as "__cilindradas"
        return f'''{retorno}
 - N_portas: {self.__n_portas}
 - Comprimento: {self.__comprimento}
 - Capacidade: {self.__capacidade}
'''