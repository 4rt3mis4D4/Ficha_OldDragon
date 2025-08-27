# Declaração do dicionário como constante
ATRIBUTOS_DESC = {
    "Força": "Dano físico",
    "Destreza": "Precisão ágil",
    "Constituição": "Resistência vital",
    "Inteligência": "Conhecimento lógico e magia",
    "Sabedoria": "Percepção intuitiva",
    "Carisma": "Influência social"
}
# Função para exibir o dicionário de atributos
def exibir_descAtr():
    print("\n--- DICIONÁRIO DE ATRIBUTOS ---")
    for atributo, descricao in ATRIBUTOS_DESC.items():
        print(f"{atributo}: {descricao}")
