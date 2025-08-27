def exibir_ficha(personagem):
    print(f"\n=== FICHA DE {personagem.nome} ===")
    print(f"Raça: {personagem.raca.nome}")
    print(f"Classe: {personagem.classe.nome}")

    # Exibe os atributos (resultado de cada rolagem e total da soma)
    print("\n--- ATRIBUTOS ---")
    for atributo, valor in personagem.atributos.items():
        print(f"{atributo}: {valor}")

    # Exibe: Movimento, Infravisão e Alinhamento
    print("\n--- CARACTERÍSTICAS DA RAÇA ---")
    caract = personagem.raca.caracteristicas()
    for chave, valor in caract.items():
        print(f"{chave}: {valor}")

    # Exibe a habilidade da raça escolhida e sua definição
    print("\n--- HABILIDADES DA RAÇA ---")
    habilidades = personagem.raca.habilidades_raca()
    for nome, descricao in habilidades.items():
        print(f"{nome}: {descricao}")

    # Exibe os artefatos da classe
    print("\n--- ARTEFATOS DA CLASSE ---")
    artefatos_classe = personagem.classe.artefatos_classe()
    for chave, valor in artefatos_classe.items():
        print(f"{chave}: {valor}")

    # Exibe as habilidades da classe escolhida e sua definição
    print("\n--- HABILIDADES DA CLASSE")
    hab_classe = personagem.classe.habilidades_classe()
    for chave, valor in hab_classe.items():
        print(f"{chave}: {valor}")
