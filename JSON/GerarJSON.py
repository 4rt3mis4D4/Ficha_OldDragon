import json

def conversaoPersonagem(personagem):
    return {
        "nome": personagem.nome,
        "raca": {
            "nome": personagem.raca.nome,
            "caracteristicas": personagem.raca.caracteristicas(),
            "habilidades": personagem.raca.habilidades_raca()
        },
        "classe": {
            "nome": personagem.classe.nome,
            "artefatos": personagem.classe.artefatos_classe(),
            "habilidades": personagem.classe.habilidades_classe()
        },
        "atributos": personagem.atributos
    }

def salvarJson(personagem, arquivo = "personagem.json"):
    dados = conversaoPersonagem(personagem)

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

    print(f"\nFicha salva em: {arquivo}")
