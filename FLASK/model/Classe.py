from abc import abstractmethod, ABC

# Abstração da Classe
class Classe(ABC):
    def __init__(self):
        self.nome = ""
        self.artefatos = {
            "Armas": None,
            "Armaduras": None,
            "Itens Mágicos": None
        }

    def artefatos_classe(self):
        return self.artefatos

    @abstractmethod
    def habilidades_classe(self):
        pass

class Guerreiro(Classe):
    def __init__(self):
        super().__init__()
        self.nome = "Guerreiro"

        self.artefatos["Armas"] = "Pode usar todas as armas."
        self.artefatos["Armaduras"] = "Pode usar todas as armaduras."
        self.artefatos["Itens Mágicos"] = "Apenas pergaminhos de proteção."
    def habilidades_classe(self):
        return{
            "Aparar": "O Guerreiro pode sacrificar seu escudo ou arma ao ser atingido por um ataque físico para absorver todo o dano, mas o item fica danificado ou é destruído, com itens mágicos podendo perder seus bônus permanentemente.",
            "Maestria em Arma": "O Guerreiro se torna mestre em uma arma à sua escolha, recebendo um bônus de +1 no dano daquela arma.",
            "Ataque Extra": "Um Guerreiro nível 6º ganha um segundo ataque em sequência com a mesma arma em que possui maestria, usando o mesmo bônus de ataque do primeiro."
        }

class Ladrao(Classe):
    def __init__(self):
        super().__init__()
        self.nome = "Ladrão"

        self.artefatos["Armas"] = "Apenas pequenas ou médias."
        self.artefatos["Armaduras"] = "Apenas as leves."
        self.artefatos["Itens Mágicos"] = "Apenas pergaminhos de proteção."
    def habilidades_classe(self):
        return{
            "Ataque Furtivo": "Um Ladrão que ataca furtivamente causa o dobro de dano ao seu alvo.",
            "Ouvir Ruídos": "Um Ladrão pode tentar ouvir ruídos à distância com 1-2 em 1d6 chance de sucesso, desde que esteja em um local silencioso e fora de combate.",
            "Talentos de Ladrão": "Ladrões começam com 2 pontos em cada um dos cinco talentos (Armadilha, Arrombar, Escalar, Punga e Furtividade) e mais 2 pontos adicionais para distribuir livremente."
        }

class Mago(Classe):
    def __init__(self):
        super().__init__()
        self.nome = "Mago"

        self.artefatos["Armas"] = "Apenas pequenas"
        self.artefatos["Armaduras"] = "Nenhuma"
        self.artefatos["Itens Mágicos"] = "Todos"
    def habilidades_classe(self):
        return{
            "Magias Arcanas": "Um Mago memoriza magias diariamente estudando seu grimório para escolher quais feitiços poderá lançar naquele dia.",
            "Ler Magias": "Um Mago pode, uma vez por dia por nível, decifrar inscrições mágicas para identificar qual magia está escrita, mas não para entender sua mensagem ou propriedades de itens.",
            "Detectar Magias": "Um Mago pode, uma vez por dia por nível, detectar a presença de magia em uma área após se concentrar por um tempo, percebendo apenas uma aura sem identificar detalhes."
        }
