from model.utilitarios import rolar_dado

class Estilo:
    def __init__(self):
        self.atributos = {
            "Força": 0,
            "Destreza": 0,
            "Constituição": 0,
            "Inteligência": 0,
            "Sabedoria": 0,
            "Carisma": 0
        }

    # Função - Estilo Clássico
    def classico(self):
        """Rola 3d6 para cada atributo e retorna os resultados"""
        resultados = {}
        for atributo in self.atributos:
            _, soma = rolar_dado(6, 3)
            resultados[atributo] = soma
        return resultados

    # Função - Estilo Aventureiro
    def aventureiro(self):
        """Rola 3d6 seis vezes e retorna os resultados para distribuição"""
        resultados_rolagem = []
        for _ in range(len(self.atributos)):
            _, soma = rolar_dado(6, 3)
            resultados_rolagem.append(soma)
        return resultados_rolagem

    # Função - Estilo Herói
    def heroi(self):
        """Rola 4d6 seis vezes (descarta o menor) e retorna resultados para distribuição"""
        resultados_rolagem = []
        for _ in range(len(self.atributos)):
            resultados, _ = rolar_dado(6, 4)
            resultados.sort()
            soma = sum(resultados[1:])  # Descarta o menor
            resultados_rolagem.append(soma)
        return resultados_rolagem
