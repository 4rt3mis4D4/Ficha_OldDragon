import random

#Função que simula a rolagem de um dado, considerando a quantidade de lados e o número de rolagens
def rolar_dado(lados, rolagem=1):
    #random.radiant(menor, max) sorteia números aleatórios
    #for _ in range(rolagem) realiza um loop de acordo com a quantidade de rolagens informada
    resultado = [random.randint(1, lados) for _ in range(rolagem)]
    return resultado, sum(resultado) #retorna o resultado de cada rolagem e soma

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.atributos = {}

class Estilo(Personagem):
    def classico (self):
        print("Você escolheu o Estilo Clássico!! Vamos para a rolagem de seus atributos: ")
        nomes_atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
        for atributo in nomes_atributos:
            total = rolar_dado(6, 3)
            self.atributos[atributo] = total
        self.mostrar_atributos()

    def aventureiro (self):
        print("Você escolheu o Estilo Aventureiro!! Vamos para a rolagem de seus atributos: ")

    def heroi (self):
        print("Você escolheu o Estilo Herói!! Vamos para a rolagem de seus atributos: ")

    def mostrar_atributos(self):
        print(f"\nFicha de {self.nome}:")
        for atributo, (resultados, soma) in self.atributos.items():
            print(f"{atributo}: {resultados} (Total: {soma})")

if __name__ == "__main__":
    nome_personagem = input("Digite o nome do seu personagem: ")
    personagem = Estilo(nome_personagem)
    print("Escolha o seu estilo: ")
    print("1. CLÁSSICO - Role 3d6 seis vezes e distribua entre os atributos, seguindo a ordem: Força, Destreza, Constituição, Inteligência, Sabedoria e Carisma.")
    print("2. AVENTUREIRO - Role 3d6 seis vezes e distribua como desejar os resultados nos seis atributos dos personagens.")
    print("3. HEROI - Role 4d6 eliminando o d6 mais baixo da soma. Faça isso seis vezes e distribua como desejar os resultados nos seis atributos dos personagens.")
    estilo = int(input())
    if estilo == 1:
        personagem.classico()
