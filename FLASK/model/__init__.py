from .Classe import Guerreiro, Ladrao, Mago
from .Raca import Humano, Elfo, Anao, Halfling, Gnomo, Meio_Elfo
from .Utilitarios import rolar_dado


# Dicionários auxiliares para lookup no Flask app
CLASSES = {
"Guerreiro": Guerreiro,
"Ladrão": Ladrao,
"Mago": Mago
}


RACAS = {
"Humano": Humano,
"Elfo": Elfo,
"Anão": Anao,
"Halfling": Halfling,
"Gnomo": Gnomo,
"Meio-Elfo": Meio_Elfo
}
