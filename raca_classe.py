import random
from abc import abstractmethod, ABC

# Declaração do dicionário como constante
ATRIBUTOS_DESC = {
    "Força": "Dano físico",
    "Destreza": "Precisão ágil",
    "Constituição": "Resistência vital",
    "Inteligência": "Conhecimento lógico e magia",
    "Sabedoria": "Percepção intuitiva",
    "Carisma": "Influência social"
}

# Abstração da raça
class Raca(ABC):
    def __init__(self):
        self.nome = ""
        self.caract = {
            "Movimento": None,
            "Infravisão": None,
            "Alinhamento": None
        }

    def caracteristicas(self):
        return self.caract

    @abstractmethod
    def habilidades_raca(self):
        pass

class Humano(Raca):
    def __init__(self):
        super().__init__()
        self.nome = "Humano"

        self.caract["Movimento"] = "9 Metros"
        self.caract["Infravisão"] = "Não"
        self.caract["Alinhamento"] = "Qualquer"

    def habilidades_raca(self):
        return {
            "Aprendizado": "Humanos ganham 10% a mais de experiência (XP) por aprenderem mais rápido que outras raças.",
            "Adaptabilidade": "Humanos recebem +1 em uma Jogada de Proteção à sua escolha por serem adaptáveis e diversos."
        }

class Elfo(Raca):
    def __init__(self):
        super().__init__()
        self.nome = "Elfo"

        self.caract["Movimento"] = "9 Metros"
        self.caract["Infravisão"] = "18 Metros"
        self.caract["Alinhamento"] = "Neutro"

    def habilidades_raca(self):
        return{
            "Percepção Natural": "Elfos detectam portas secretas a até 6 m com 1 em 1d6 (ou 1-2 em 1d6 se estiverem procurando).",
            "Graciosos": "Elfos têm controle preciso de seus movimentos e recebem +1 em testes de JPD.",
            "Arma Racial": "Elfos tratam o arqueirismo como arte marcial e recebem +1 de dano em ataques à distância com arcos.",
            "Imunidades": "Elfos são imunes a magias ou efeitos de sono e à paralisia causada por Ghouls."
        }

class Anao(Raca):
    def __init__(self):
        super().__init__()
        self.nome = "Anao"

        self.caract["Movimento"] = "6 Metros"
        self.caract["Infravisão"] = "18 Metros"
        self.caract["Alinhamento"] = "Ordem"

    def habilidades_raca(self):
        return{
            "Mineradores": "Anões detectam anomalias em pedras a até 6 m com 1 em 1d6 (ou 1-2 em 1d6 se estiverem procurando).",
            "Vigoroso": "Anões recebem +1 em testes de JPC devido à sua grande resistência física.",
            "Armas Grandes": "Anões só podem usar armas médias e pequenas, mas armas grandes forjadas como raciais contam como médias para eles.",
            "Inimigos": "Ataques de anões contra orcs, ogros e hobgoblins são sempre considerados fáceis."
        }

class Halfling(Raca):
    def __init__(self):
        super().__init__()
        self.nome = "Halfling"

        self.caract["Movimento"] = "6 Metros"
        self.caract["Infravisão"] = "Não Possui"
        self.caract["Alinhamento"] = "Neutro"

    def habilidades_raca(self):
        return{
            "Furtivos": "Halflings podem se esconder com 1-2 em 1d6 e, se forem Ladrões, ganham +1 em Furtividade.",
            "Destemidos": "Halflings recebem +1 em testes de JPS devido à sua resistência mental.",
            "Bons de Mira": "Halflings têm +1 para acertar com armas de arremesso devido à sua tradição racial.",
            "Pequenos": "Ataques de criaturas grandes ou maiores são considerados difíceis contra halflings devido à sua baixa estatura e agilidade.",
            "Restrições": "Halflings estão restritos a armaduras de couro e a armas pequenas ou médias, que usam com duas mãos."
        }

class Gnomo(Raca):
    def __init__(self):
        super().__init__()
        self.nome = "Gnomo"

        self.caract["Movimento"] = "6 Metros"
        self.caract["Infravisão"] = "18 Metros"
        self.caract["Alinhamento"] = "Neutro"

    def habilidades_raca(self):
        return{
            "Avaliadores": "Vantagem em testes de resistência de Int, Sab e Car contra magia.",
            "Sagazes": "Conhece o truque Prestidigitação (ilusão menor) de graça.",
            "Vigorosos": "Deslocamento de 9m (30 pés) e pode usar armadura pesada sem penalidade.",
            "Restrições": "Tamanho Pequeno, tem desvantagem com armas pesadas."
        }

class Meio_Elfo(Raca):
    def __init__(self):
        super().__init__()
        self.nome = "Meio_Elfo"

        self.caract["Movimento"] = "9 Metros"
        self.caract["Infravisão"] = "9 Metros"
        self.caract["Alinhamento"] = "Caos"

    def habilidades_raca(self):
        return{
            "Aprendizado": "Ganha proficiência em duas habilidades à sua escolha.",
            "Graciosos e Vigorosos": "+2 em Carisma e +1 em dois outros atributos; vantagem contra encantamento.",
            "Idioma Extra": "Fala Common, Élfico e mais um idioma à sua escolha.",
            "Imunidade": "Imune a efeitos mágicos que colocam para dormir."
        }

# Função que simula a rolagem de um dado, considerando a quantidade de lados e o número de rolagens
def rolar_dado(lados, rolagem=1):
    # random.radiant(menor, max) sorteia números aleatórios
    # for _ in range(rolagem) realiza um loop de acordo com a quantidade de rolagens informada
    resultado = [random.randint(1, lados) for _ in range(rolagem)]
    return resultado, sum(resultado)  # retorna os resultados das rolagens e sua soma

# Função para exibir o dicionário de atributos
def exibir_descAtr():
    print("\n--- DICIONÁRIO DE ATRIBUTOS ---")
    for atributo, descricao in ATRIBUTOS_DESC.items():
        print(f"{atributo}: {descricao}")


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
                print("Entrada inválida. Digite as opções de números propostos.\n")

        print(f"\nVocê escolheu a raça: {self.raca.nome}")

    def exibir_ficha(self):
        print(f"\n=== FICHA DE {self.nome} ===")
        print(f"Raça: {self.raca.nome}")

        # Exibe os atributos (resultado de cada rolagem e total da soma)
        print("\n--- ATRIBUTOS ---")
        for atributo, valor in self.atributos.items():
            print(f"{atributo}: {valor}")

        # Exibe: Movimento, Infravisão e Alinhamento
        print("\n--- CARACTERÍSTICAS DA RAÇA ---")
        caract = self.raca.caracteristicas()
        for chave, valor in caract.items():
            print(f"{chave}: {valor}")

        # Exibe a habilidade da raça escolhida e sua definição
        print("\n--- HABILIDADES DA RAÇA ---")
        habilidades = self.raca.habilidades_raca()
        for nome, descricao in habilidades.items():
            print(f"{nome}: {descricao}")

# Classe Estilo: Determinar atributos do personagem criado
class Estilo(Personagem):
    # Função - Estilo Clássico
    def classico(self):
        print("\n\nVocê escolheu o Estilo Clássico!! Vamos para a rolagem de seus atributos: ")

        for atributo in self.atributos:
            resultado, soma = rolar_dado(6, 3)
            print(f"{atributo}: {resultado} (Total: {soma})")
            self.atributos[atributo] = soma

    # Função - Estilo Aventureiro
    def aventureiro(self):
        print("\n\nVocê escolheu o Estilo Aventureiro!!")

        # Dicionário de atributos
        if input("Deseja consultar o dicionário de atributos? (s/n): ").lower() == 's':
            exibir_descAtr()

        print("\nVamos para a rolagem de seus atributos:")

        resultados_rolagem = []

        # Realizando rolagem de todos os atributos e armazenando em uma lista
        for i in range(len(self.atributos)):
            resultado, soma = rolar_dado(6, 3)
            resultados_rolagem.append(soma)  # armazenado o resultado das rolagens
            print(f"Rolagem {i + 1}: {resultado} (Total: {soma})")

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

    # Função - Estilo Herói
    def heroi(self):
        print("\n\nVocê escolheu o Estilo Herói!!")

        # Dicionário de atributos
        if input("Deseja consultar o dicionário de atributos? (s/n): ").lower() == 's':
            exibir_descAtr()

        print("\nVamos para a rolagem de seus atributos:")

        resultados_rolagem = []

        for i in range(len(self.atributos)):
            resultado, soma = rolar_dado(6, 4)

            print(f"\nRolagem {i + 1}: {resultado}")  # Exibi resultado de todas as rolagens
            menor_valor = min(resultado)  # Identifica o menor valor
            resultado.remove(menor_valor)  # Remove o menor valor
            soma_final = sum(resultado)  # Realiza a soma sem o menor resultado

            resultados_rolagem.append(soma_final)  # armazenado o resultado das rolagens
            print(f"Rolagem {i + 1}: {resultado} (Eliminado: {menor_valor} Total: {soma_final})")

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
                    print("Entrada inválida. Digite as opções de números propostos.\n")

# Estrutura Main - Menu e Executável
if __name__ == "__main__":
    personagem = Estilo()
    personagem.nome_personagem()

    while True:
        print("\n--- ESCOLHA O SEU ESTILO: ---")
        print(
            "1. CLÁSSICO - Role 3d6 seis vezes e distribua entre os atributos, seguindo a ordem: Força, Destreza, Constituição, Inteligência, Sabedoria e Carisma.")
        print(
            "2. AVENTUREIRO - Role 3d6 seis vezes e distribua como desejar os resultados nos seis atributos dos personagens.")
        print(
            "3. HEROI - Role 4d6 eliminando o d6 mais baixo da soma. Faça isso seis vezes e distribua como desejar os resultados nos seis atributos dos personagens.")

        estilo = int(input("\nEscolha um estilo (1-3): "))

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
            print("\nValor inválido.\n")

    personagem.escolher_raca() # Função de escolha da Raça
    personagem.exibir_ficha() # Função impressão da ficha
