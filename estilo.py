import random

#Função que simula a rolagem de um dado, considerando a quantidade de lados e o número de rolagens
def rolar_dado(lados, rolagem=1):
    #random.radiant(menor, max) sorteia números aleatórios
    #for _ in range(rolagem) realiza um loop de acordo com a quantidade de rolagens informada
    resultado = [random.randint(1, lados) for _ in range(rolagem)]
    return resultado, sum(resultado) #retorna os resultados das rolagens e sua soma

#Classe Personagem
class Personagem:
    #Construtor: inicializar variáveis
    def __init__(self, nome):
        self.nome = nome
        self.atributos = {} #Conjunto atributos

#Classe Estilo: Determinar atributos do personagem criado
class Estilo(Personagem):
    #Função - Estilo Clássico
    def classico (self):
        print("Você escolheu o Estilo Clássico!! Vamos para a rolagem de seus atributos: ")
        nomes_atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

        for atributo in nomes_atributos:
            resultado, soma = rolar_dado(6, 3)
            print(f"{atributo}: {resultado} (Total: {soma})")
            self.atributos[atributo] = soma

        self.mostrar_atributos()

    #Função - Estilo Aventureiro
    def aventureiro (self):
        print("Você escolheu o Estilo Aventureiro!! Vamos para a rolagem de seus atributos: ")
        nomes_atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
        resultados_rolagem = []

        #Realizando rolagem de todos os atributos e armazenando em uma lista
        for i in range(6):
            resultado, soma = rolar_dado(6, 3)
            resultados_rolagem.append(soma) #armazenado o resultado das rolagens
            print(f"Rolagem {i+1}: {resultado} (Total: {soma})")

        print(f"\nTotal das rolagens: {resultados_rolagem}")
        print(f"Lista de Atributos: {nomes_atributos}")
        print("\nAgora distribua os valores para os atributos de sua preferência:")

        for atributo in nomes_atributos:
            print(f"Valores Disponíveis: {resultados_rolagem}")
            escolha = int(input(f"Escolha o valor para {atributo}: "))
            print()

            #in - pertence
            if escolha in resultados_rolagem:
                resultados_rolagem.remove(escolha) #Remove o valor ja escolhido
                self.atributos[atributo] = escolha #Adiciona o valor escolhido no atributo
            else:
                print("Valor inexistente. Escolha novamente.")
                nomes_atributos.insert(0, atributo) #volta uma interação

        self.mostrar_atributos()


    #Função - Estilo Herói
    def heroi (self):
        print("Você escolheu o Estilo Herói!! Vamos para a rolagem de seus atributos: ")

        nomes_atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
        resultados_rolagem = []

        for i in range(6):
            resultado, soma = rolar_dado(6, 4)

            print(f"\nRolagem {i+1}: {resultado}") #Exibi resultado de todas as rolagens
            menor_valor = min(resultado) #Identifica o menor valor 
            resultado.remove(menor_valor) #Remove o menor valor
            soma_final = sum(resultado) #Realiza a soma sem o menor resultado 

            resultados_rolagem.append(soma_final) #armazenado o resultado das rolagens
            print(f"Rolagem {i+1}: {resultado} (Eliminado: {menor_valor} Total: {soma_final})")

        print(f"\nTotal das rolagens: {resultados_rolagem}")
        print(f"Lista de Atributos: {nomes_atributos}")
        print("\nAgora distribua os valores para os atributos de sua preferência:")

        for atributo in nomes_atributos:
            print(f"Valores Disponíveis: {resultados_rolagem}")
            escolha = int(input(f"Escolha o valor para {atributo}: "))
            print()

            # in - pertence
            if escolha in resultados_rolagem:
                resultados_rolagem.remove(escolha)  # Remove o valor ja escolhido
                self.atributos[atributo] = escolha  # Adiciona o valor escolhido no atributo
            else:
                print("Valor inexistente. Escolha novamente.")
                nomes_atributos.insert(0, atributo)  # volta uma interação

        self.mostrar_atributos()


    #Função - exibir atributos (resultado de cada rolagem e total da soma)
    def mostrar_atributos(self):
        print(f"\n=== Ficha de {self.nome} ===")

        for atributo, valor in self.atributos.items():
            print(f"{atributo}: {valor}")

#Estrutura Main - executável
if __name__ == "__main__":
    nome_personagem = input("Digite o nome do seu personagem: ")
    personagem = Estilo(nome_personagem)

    while True:
        print("Escolha o seu estilo: ")
        print("1. CLÁSSICO - Role 3d6 seis vezes e distribua entre os atributos, seguindo a ordem: Força, Destreza, Constituição, Inteligência, Sabedoria e Carisma.")
        print("2. AVENTUREIRO - Role 3d6 seis vezes e distribua como desejar os resultados nos seis atributos dos personagens.")
        print("3. HEROI - Role 4d6 eliminando o d6 mais baixo da soma. Faça isso seis vezes e distribua como desejar os resultados nos seis atributos dos personagens.")

        estilo = int(input())

        if estilo == 1:
            personagem.classico()
            break
        elif estilo == 2:
            personagem.aventureiro()
            break
        elif estilo == 3:
            personagem.heroi()
            break
        else:
            print("\nValor inválido. Digite apenas 1, 2 ou 3.\n")
