# Renderizar, acessar requisições, armazenar e redirecionar
from flask import Flask, render_template, request, session, redirect, url_for 

# Importando classes e funções dos arquivos Python da pasta "model"
from model.estrutura import Personagem
from model.raca import Humano, Elfo, Anao, Halfling, Gnomo, Meio_Elfo
from model.classe import Guerreiro, Ladrao, Mago
from model.utilitarios import rolar_dado
from model.estilo import Estilo

from collections import Counter # Validação de Atributos

# FUNÇÃO AUXILIAR: para validação dos atributos nos estilos aventureiro e herói
def validar_atributos(personagem, estilo, valores_rolados):
    # VALIDAÇÃO: Verificar se todos os valores são os que foram rolados
    valores_escolhidos = []
    atributos_preenchidos = {}
    
    for atributo in personagem.atributos:
        valor_completo = request.form.get(atributo, '0')
        try:
            # Extrair apenas o valor (ignorar o índice)
            valor = int(valor_completo.split('-')[0])
        except (ValueError, IndexError):
            return render_template("distribuir_atributos.html", 
                                 personagem=personagem, 
                                 valores=valores_rolados,
                                 estilo=estilo,
                                 erro="Erro: Valor inválido para " + atributo)
        
        valores_escolhidos.append(valor)
        atributos_preenchidos[atributo] = valor
    
    # Verificar se a contagem de cada valor bate (permite valores repetidos)
    contador_escolhidos = Counter(valores_escolhidos)
    contador_rolados = Counter(valores_rolados)
    
    if contador_escolhidos != contador_rolados:
        return render_template("distribuir_atributos.html", 
                             personagem=personagem, 
                             valores=valores_rolados,
                             estilo=estilo,
                             erro="Erro: Você deve usar exatamente os valores que foram rolados! Valores rolados: " + str(valores_rolados))
    
    # Se passou na validação, salvar os atributos
    personagem.atributos = atributos_preenchidos
    session['atributos'] = personagem.atributos
    return redirect(url_for('exibir_ficha'))

# Aplicação Flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "chave-secreta" # Chave secreta para sessions

# Página inicial - index.html
@app.route("/") # Definindo Rota (quando executar)
def index():
    return render_template("index.html") # Renderizando template (o que retornar)

# Página criação do personagem - criar_personagem.html (GET mostra formulário, POST processa)
@app.route("/criar_personagem", methods=["GET", "POST"])
def criar_personagem():
    # Se for POST:
    if request.method == "POST":
        # Salva dados na session
        session['nome'] = request.form.get("nome")
        session['raca'] = request.form.get("raca")
        session['classe'] = request.form.get("classe")
        session['estilo'] = request.form.get("estilo")
        
        # Limpa dados antigos na session
        if 'atributos' in session:
            del session['atributos']
        if 'valores_rolagem' in session:
            del session['valores_rolagem']
        
        return redirect(url_for('gerar_atributos'))
    
    # Se for GET:
    # Mostra o formulário de opções em formato de dicionário
    racas = {
        'humano': 'Humano',
        'elfo': 'Elfo', 
        'anao': 'Anão',
        'halfling': 'Halfling',
        'gnomo': 'Gnomo',
        'meio_elfo': 'Meio Elfo'
    }
    
    classes = {
        'guerreiro': 'Guerreiro',
        'ladrao': 'Ladrão', 
        'mago': 'Mago'
    }
    
    estilos = {
        'classico': 'Clássico',
        'aventureiro': 'Aventureiro',
        'heroi': 'Herói'
    }
    
    # Renderiza template (criar_personagem.html) e passa variáveis
    return render_template("criar_personagem.html", 
                         racas=racas, 
                         classes=classes, 
                         estilos=estilos) 

# Página geração de atributos - distribuir_atributos.html
@app.route("/gerar_atributos", methods=["GET", "POST"])
def gerar_atributos():
    # Verifica se o usuário veio da página anterior (criar_personagem) pela chave nome
    if 'nome' not in session:
        return redirect(url_for('criar_personagem')) 
    
    personagem = Personagem() # Cria Instância de Personagem
    personagem.nome = session['nome']
    
    # Armazena a raça escolhida pelo usuário e de acordo com o escolhido, herda todas as caracteristicas dele
    raca_key = session['raca']
    if raca_key == 'humano':
        personagem.raca = Humano()
    elif raca_key == 'elfo':
        personagem.raca = Elfo()
    elif raca_key == 'anao':
        personagem.raca = Anao()
    elif raca_key == 'halfling':
        personagem.raca = Halfling()
    elif raca_key == 'gnomo':
        personagem.raca = Gnomo()
    elif raca_key == 'meio_elfo':
        personagem.raca = Meio_Elfo()
    else:
        personagem.raca = Humano()  # Default
    
    # Armazena a classe escolhida pelo usuário e de acordo com o escolhido, herda todas as caracteristicas dele
    classe_key = session['classe']
    if classe_key == 'guerreiro':
        personagem.classe = Guerreiro()
    elif classe_key == 'ladrao':
        personagem.classe = Ladrao()
    elif classe_key == 'mago':
        personagem.classe = Mago()
    else:
        personagem.classe = Guerreiro()  # Default
    
    estilo = session['estilo'] # Armazena o estilo escolhido pelo usuário
    estilo_obj = Estilo() # importa a classe Estilo e o armazena 
    
    # Gera atributos baseado no estilo
    if estilo == 'classico':
        atributos_gerados = estilo_obj.classico()
        personagem.atributos = atributos_gerados
        session['atributos'] = personagem.atributos
        
        return redirect(url_for('exibir_ficha'))
    
    elif estilo == 'aventureiro':
        # POST AVENTUREIRO:
        if request.method == "POST":
            valores_rolados = session.get('valores_rolagem', [])
            return validar_atributos(personagem, estilo, valores_rolados)
        
        else: # GET AVENTUREIRO
            # Usa a função aventureiro do módulo estilo para gerar valores
            valores = estilo_obj.aventureiro()
            session['valores_rolagem'] = valores
            return render_template("distribuir_atributos.html", 
                                 personagem=personagem, 
                                 valores=valores,
                                 estilo=estilo)
    
    elif estilo == 'heroi':
        # POST HERÓI:
        if request.method == "POST":
            valores_rolados = session.get('valores_rolagem', [])
            return validar_atributos(personagem, estilo, valores_rolados)
        
        else: # GET HERÓI
            # Usa a função heroi do módulo estilo para gerar valores
            valores = estilo_obj.heroi()
            session['valores_rolagem'] = valores
            return render_template("distribuir_atributos.html", 
                                 personagem=personagem, 
                                 valores=valores,
                                 estilo=estilo)
 
# Página exibir ficha - ficha.html
@app.route("/ficha")
def exibir_ficha():
    # Verifica se todos os dados necessários estão na session
    if 'nome' not in session or 'atributos' not in session:
        return redirect(url_for('criar_personagem')) # Caso contrário retorna para a página de criação do personagem
    
    # Recria personagem com dados da session
    personagem = Personagem()
    personagem.nome = session.get('nome', '')
    
    # Recria raça
    raca_key = session.get('raca')
    if raca_key == 'humano':
        personagem.raca = Humano()
    elif raca_key == 'elfo':
        personagem.raca = Elfo()
    elif raca_key == 'anao':
        personagem.raca = Anao()
    elif raca_key == 'halfling':
        personagem.raca = Halfling()
    elif raca_key == 'gnomo':
        personagem.raca = Gnomo()
    elif raca_key == 'meio_elfo':
        personagem.raca = Meio_Elfo()
    else:
        personagem.raca = Humano()
    
    # Recria classe
    classe_key = session.get('classe')
    if classe_key == 'guerreiro':
        personagem.classe = Guerreiro()
    elif classe_key == 'ladrao':
        personagem.classe = Ladrao()
    elif classe_key == 'mago':
        personagem.classe = Mago()
    else:
        personagem.classe = Guerreiro()
    
    # Recupera atributos
    personagem.atributos = session.get('atributos', {})
    
    return render_template("ficha.html", personagem=personagem)


# ROTAS ADICIONAIS:
# Rota para limpar session e começar novo personagem
@app.route("/novo")
def novo_personagem():
    session.clear();
    return redirect(url_for('criar_personagem'))

# Manipuladores de erro para redirecionar usuários em caso de erros 
# Handler de erro para método não permitido
@app.errorhandler(405)
def method_not_allowed(e):
    return redirect(url_for('criar_personagem'))

# Handler de erro para página não encontrada
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

if __name__ == "__main__":
    # Inicia a aplicação Flask em modo debug, acessível por qualquer endereço na porta 5000.
    app.run(debug=True, host='0.0.0.0', port=5000) 
