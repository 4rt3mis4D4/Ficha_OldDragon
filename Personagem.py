from Raca import Humano, Elfo, Anao, Halfling, Gnomo, Meio_Elfo
from Classe import Guerreiro, Ladrao, Mago
from Dados import rolar_dado
from Dicionario import exibir_descAtr
from Ficha import exibir_ficha

# Classe Personagem
class Personagem:
    # Construtor: inicializar variáveis
    def __init__(self):
        self.nome = ""
        self.raca = None
        self.atributos = {
            "Força": 0,
            "Destreza": 0,
            "Constituição": 0,
            "Inteligência": 0,
            "Sabedoria": 0,
            "Carisma": 0
        }  # Conjunto atributos

    def nome_personagem(self):
        self.nome = input("Digite o nome do seu personagem: ")

    def escolher_raca(self):
        print("\n--- ESCOLHA A SUA RAÇA: ---\n")
        print("1. Humano - A raça mais versátil e adaptável, perfeita para qualquer classe")
        print("2. Elfo - Um povo gracioso e atemporal, conectado à natureza e à magia")
        print("3. Anão - Um resistente especialista em combate e trabalho em pedra")
        print("4. Halfling - Um povo pequeno, ágil e incrivelmente sortudo")
        print("5. Gnomo - Mestres ilusionistas e inventores inteligentes e curiosos")
        print("6. Meio Elfo - Um diplomata carismático e versátil que combina a adaptabilidade humana com a graça élfica")

        while True:
            try:
                opcao = int(input("\nEscolha uma raça (1-6): "))
                if opcao == 1:
                    self.raca = Humano()
                    break
                elif opcao == 2:
                    self.raca = Elfo()
                    break
                elif opcao == 3:
                    self.raca = Anao()
                    break
                elif opcao == 4:
                    self.raca = Halfling()
                    break
                elif opcao == 5:
                    self.raca = Gnomo()
                    break
                elif opcao == 6:
                    self.raca = Meio_Elfo()
                    break
                else:
                    print("\nValor inválido.\n")
            except ValueError:
                print("Entrada inválida. Digite as opções dos números propostos.\n")

        print(f"\nVocê escolheu a raça: {self.raca.nome}")

    def escolher_classe(self):
        print("\n--- ESCOLHA A SUA CLASSE: ---\n")
        print("1. Guerreiro - Aventureiros especializados em combate, sempre na linha de frente e mortais quando desembainham suas armas.")
        print("2. Ladrão - Aventureiro táctico, perito em sobreviver em masmorras. Furtivo, traiçoeiro e fatal quando ataca suas vítimas sorrateiramente")
        print("3. Mago - Aventureiro estudioso, especializado nas artes arcanas, dedicado a conjurar magias escritas em grimórios e pergaminhos.")

        while True:
            try:
                opcao = int(input("\nEscolha uma classe (1-3): "))
                if opcao == 1:
                    self.classe = Guerreiro()
                    break
                elif opcao == 2:
                    self.classe = Ladrao()
                    break
                elif opcao == 3:
                    self.classe = Mago()
                    break
                else:
                    print("\nValor inválido.\n")
            except ValueError:
                print("Entrada inválida. Digite as opções dos números propostos.\n")

        print(f"\nVocê escolheu a raça: {self.classe.nome}")

    def escolher_estilo(self):
        while True:
            print("\n--- ESCOLHA O SEU ESTILO: ---")
            print(
                "1. CLÁSSICO - Role 3d6 seis vezes e distribua entre os atributos, seguindo a ordem: Força, Destreza, Constituição, Inteligência, Sabedoria e Carisma.")
            print(
                "2. AVENTUREIRO - Role 3d6 seis vezes e distribua como desejar os resultados nos seis atributos dos personagens.")
            print(
                "3. HEROI - Role 4d6 eliminando o d6 mais baixo da soma. Faça isso seis vezes e distribua como desejar os resultados nos seis atributos dos personagens.")

            opcao = int(input("\nEscolha um estilo (1-3): "))

            if opcao == 1:
                self.classico()
                break
            elif opcao == 2:
                self.aventureiro()
                break
            elif opcao == 3:
                self.heroi()
                break
            else:
                print("\nValor inválido.\n")
