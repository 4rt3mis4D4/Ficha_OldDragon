import random

#Declaração do dicionário como constante 
ATRIBUTOS_DESC = {
    "Força": "Dano físico",
    "Destreza": "Precisão ágil",
    "Constituição": "Resistência vital",
    "Inteligência": "Conhecimento lógico e magia",
    "Sabedoria": "Percepção intuitiva",
    "Carisma": "Influência social"
}

#Função que simula a rolagem de um dado, considerando a quantidade de lados e o número de rolagens
def rolar_dado(lados, rolagem=1):
    #random.radiant(menor, max) sorteia números aleatórios
    #for _ in range(rolagem) realiza um loop de acordo com a quantidade de rolagens informada
    resultado = [random.randint(1, lados) for _ in range(rolagem)]
    return resultado, sum(resultado) #retorna os resultados das rolagens e sua soma

#Função para exibir o dicionário de atributos
def exibir_descAtr():
    print("\n--- DICIONÁRIO DE ATRIBUTOS ---")
    for atributo, descricao in ATRIBUTOS_DESC.items():
        print(f"{atributo}: {descricao}")

#Classe Personagem
class Personagem:
    #Construtor: inicializar variáveis
    def __init__(self):
        self.nome = ""
        self.atributos = {
            "Força": 0,
            "Destreza": 0,
            "Constituição": 0,
            "Inteligência": 0,
            "Sabedoria": 0,
            "Carisma": 0
        } #Conjunto atributos

    def nome_personagem(self):
        self.nome = input("Digite o nome do seu personagem: ")

#Classe Estilo: Determinar atributos do personagem criado
class Estilo(Personagem):
    #Função - Estilo Clássico
    def classico (self):
        print("\n\nVocê escolheu o Estilo Clássico!! Vamos para a rolagem de seus atributos: ")

        for atributo in self.atributos:
            resultado, soma = rolar_dado(6, 3)
            print(f"{atributo}: {resultado} (Total: {soma})")
            self.atributos[atributo] = soma

        self.mostrar_atributos()

    #Função - Estilo Aventureiro
    def aventureiro (self):
        print("\n\nVocê escolheu o Estilo Aventureiro!!")

        #Dicionário de atributos
        if input("Deseja consultar o dicionário de atributos? (s/n): ").lower() == 's':
            exibir_descAtr()

        print("\nVamos para a rolagem de seus atributos:")

        resultados_rolagem = []

        #Realizando rolagem de todos os atributos e armazenando em uma lista
        for i in range(len(self.atributos)):
            resultado, soma = rolar_dado(6, 3)
            resultados_rolagem.append(soma) #armazenado o resultado das rolagens
            print(f"Rolagem {i+1}: {resultado} (Total: {soma})")

        print(f"\nTotal das rolagens: {resultados_rolagem}")
        print("\nAgora distribua os valores para os atributos de sua preferência:")
        
        for atributo in self.atributos:
            while True:
                print(f"Valores Disponíveis: {resultados_rolagem}")
                try:
                    escolha = int(input(f"Escolha o valor para {atributo}: "))
                    if escolha in resultados_rolagem:
                        resultados_rolagem.remove(escolha)
                        self.atributos[atributo] = escolha
                        break
                    else:
                        print("Valor inexistente. Escolha novamente.\n")
                except ValueError:
                    print("Entrada inválida. Digite um número.\n")

        self.mostrar_atributos()


    #Função - Estilo Herói
    def heroi (self):
        print("\n\nVocê escolheu o Estilo Herói!!")

        #Dicionário de atributos
        if input("Deseja consultar o dicionário de atributos? (s/n): ").lower() == 's':
            exibir_descAtr()

        print("\nVamos para a rolagem de seus atributos:")

        resultados_rolagem = []

        for i in range(len(self.atributos)):
            resultado, soma = rolar_dado(6, 4)

            print(f"\nRolagem {i+1}: {resultado}") #Exibi resultado de todas as rolagens
            menor_valor = min(resultado) #Identifica o menor valor
            resultado.remove(menor_valor) #Remove o menor valor
            soma_final = sum(resultado) #Realiza a soma sem o menor resultado

            resultados_rolagem.append(soma_final) #armazenado o resultado das rolagens
            print(f"Rolagem {i+1}: {resultado} (Eliminado: {menor_valor} Total: {soma_final})")

        print(f"\nTotal das rolagens: {resultados_rolagem}")
        print("\nAgora distribua os valores para os atributos de sua preferência:")

        for atributo in self.atributos:
            while True:
                print(f"Valores Disponíveis: {resultados_rolagem}")
                try:
                    escolha = int(input(f"Escolha o valor para {atributo}: "))
                    if escolha in resultados_rolagem:
                        resultados_rolagem.remove(escolha)
                        self.atributos[atributo] = escolha
                        break
                    else:
                        print("Valor inexistente. Escolha novamente.\n")
                except ValueError:
                    print("Entrada inválida. Digite um número.\n")
                
        self.mostrar_atributos()


    #Função - exibir atributos (resultado de cada rolagem e total da soma)
    def mostrar_atributos(self):
        print(f"\n=== Ficha de {self.nome} ===")

        for atributo, valor in self.atributos.items():
            print(f"{atributo}: {valor}")
    
    #Abstração da raça
    class Raca(ABC):
        def caracteristicas (self):
            self.caract = {
                "Movimento": None,
                "Infravisão": None,
                "Alinhamento": None
            }
            return self.caract
        
        @abstractmethod
        def habilidades_raca (self):
            pass
            
    class Humano(Raca):
        def caracteristicas(self):
            #Herança para puxar o dicionário de caracteristicas da classe
            caract = super().caracteristicas();
            #Caracteristicas da Classe Específica
            caract["Movimento"] = "9 Metros"
            caract["Infravisão"] = "Não"
            caract["Alinhamento"] = "Qualquer"
            return caract
        
        def habilidades_raca (self):
            return{
                "Aprendizado": "Humanos ganham 10% a mais de experiência (XP) por aprenderem mais rápido que outras raças.",
                "Adaptabilidade": "Humanos recebem +1 em uma Jogada de Proteção à sua escolha por serem adaptáveis e diversos."
            }
            

#Estrutura Main - Menu e Executável
if __name__ == "__main__":
    personagem = Estilo()
    personagem.nome_personagem()

    while True:
        print("\n--- Escolha o seu ESTILO para rolagem dos atributos: ---")
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
