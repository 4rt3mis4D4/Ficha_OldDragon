import random

# Função que simula a rolagem de um dado, considerando a quantidade de lados e o número de rolagens
def rolar_dado(lados, rolagem=1):
    # random.radiant(menor, max) sorteia números aleatórios
    # for _ in range(rolagem) realiza um loop de acordo com a quantidade de rolagens informada
    resultado = [random.randint(1, lados) for _ in range(rolagem)]
    return resultado, sum(resultado)  # retorna os resultados das rolagens e sua soma
