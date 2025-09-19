from flask import Flask, render_template, request, session, redirect, url_for
from model.estrutura import Personagem
from model.raca import Humano, Elfo, Anao, Halfling, Gnomo, Meio_Elfo
from model.classe import Guerreiro, Ladrao, Mago
from model.utilitarios import rolar_dado
from model.estilo import Estilo
from collections import Counter

app = Flask(__name__)
app.config["SECRET_KEY"] = "chave-secreta" # Chave secreta para sessions

# Página inicial
@app.route("/")
def index():
    return render_template("index.html")

# Criar personagem - GET mostra formulário, POST processa
@app.route("/criar_personagem", methods=["GET", "POST"])
def criar_personagem():
    if request.method == "POST":
        # Salva dados na session
        session['nome'] = request.form.get("nome")
        session['raca'] = request.form.get("raca")
        session['classe'] = request.form.get("classe")
        session['estilo'] = request.form.get("estilo")
        
        # Limpa atributos anteriores da session
        if 'atributos' in session:
            del session['atributos']
        if 'valores_rolagem' in session:
            del session['valores_rolagem']
        
        return redirect(url_for('gerar_atributos'))
    
    # Se for GET, mostra o formulário
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
    
    return render_template("criar_personagem.html", 
                         racas=racas, 
                         classes=classes, 
                         estilos=estilos)

# Gerar atributos
@app.route("/gerar_atributos", methods=["GET", "POST"])
def gerar_atributos():
    if 'nome' not in session:
        return redirect(url_for('criar_personagem'))
    
    personagem = Personagem()
    personagem.nome = session['nome']
    
    # Configura raça
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
    
    # Configura classe
    classe_key = session['classe']
    if classe_key == 'guerreiro':
        personagem.classe = Guerreiro()
    elif classe_key == 'ladrao':
        personagem.classe = Ladrao()
    elif classe_key == 'mago':
        personagem.classe = Mago()
    else:
        personagem.classe = Guerreiro()  # Default
    
    estilo = session['estilo']
    estilo_obj = Estilo()
    
    # Gera atributos baseado no estilo
    if estilo == 'classico':
        # Estilo clássico: rola 3d6 para cada atributo e salva automaticamente
        for atributo in personagem.atributos:
            _, soma = rolar_dado(6, 3)
            personagem.atributos[atributo] = soma
        session['atributos'] = personagem.atributos
        return redirect(url_for('exibir_ficha'))
    
    elif estilo == 'aventureiro':
        if request.method == "POST":
            # VALIDAÇÃO: Verificar se todos os valores são os que foram rolados
            valores_escolhidos = []
            atributos_preenchidos = {}
            valores_rolados = session.get('valores_rolagem', [])
            
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
        
        else:
            # Usa a função aventureiro do módulo estilo para gerar valores
            valores = estilo_obj.aventureiro()
            session['valores_rolagem'] = valores
            return render_template("distribuir_atributos.html", 
                                 personagem=personagem, 
                                 valores=valores,
                                 estilo=estilo)
    
    elif estilo == 'heroi':
        if request.method == "POST":
            # VALIDAÇÃO: Verificar se todos os valores são os que foram rolados
            valores_escolhidos = []
            atributos_preenchidos = {}
            valores_rolados = session.get('valores_rolagem', [])
            
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
        
        else:
            # Usa a função heroi do módulo estilo para gerar valores
            valores = estilo_obj.heroi()
            session['valores_rolagem'] = valores
            return render_template("distribuir_atributos.html", 
                                 personagem=personagem, 
                                 valores=valores,
                                 estilo=estilo)

# Exibir ficha final
@app.route("/ficha")
def exibir_ficha():
    if 'nome' not in session or 'atributos' not in session:
        return redirect(url_for('criar_personagem'))
    
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

# Rota para limpar session e começar novo personagem
@app.route("/novo")
def novo_personagem():
    session.clear();
    return redirect(url_for('criar_personagem'))

# Handler de erro para método não permitido
@app.errorhandler(405)
def method_not_allowed(e):
    return redirect(url_for('criar_personagem'))

# Handler de erro para página não encontrada
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
