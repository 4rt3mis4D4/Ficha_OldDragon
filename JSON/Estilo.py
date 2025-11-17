from Utilitarios import rolar_dado, exibir_descAtr
from Estrutura import Personagem

class Estilo(Personagem):
    def distribuir_resultados(self, resultados_rolagem):
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
                    print("Entrada inválida. Digite as opções dos números propostos.\n")

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

        self.distribuir_resultados(resultados_rolagem)

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

        self.distribuir_resultados(resultados_rolagem)
