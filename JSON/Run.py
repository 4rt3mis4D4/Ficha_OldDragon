from JSON.Estrutura import exibir_ficha
from JSON.Estilo import Estilo
from JSON.GerarJSON import conversaoPersonagem, salvarJson

# Estrutura Main - Menu e Executável
if __name__ == "__main__":
    personagem = Estilo() # Herança
    personagem.nome_personagem() # Função nome do personagem

    personagem.escolher_estilo() # Função de escolha do Estilo
    personagem.escolher_raca() # Função de escolha da Raça
    personagem.escolher_classe() # Função de escolha da Classe

    exibir_ficha(personagem) # Função impressão da ficha
    salvarJson(personagem) # Função JSON
