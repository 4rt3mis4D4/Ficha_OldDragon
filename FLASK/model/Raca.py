from abc import abstractmethod, ABC

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
        self.nome = "Meio-Elfo"

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
