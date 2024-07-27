from flask import Flask, render_template, request, redirect, url_for

# REQUEST - importar solicitações com o modelo de renderização 
app = Flask("reservas")

@app.route("/")
def login():
    return render_template('login.html')

# PRIMEIRO FORMULÁRIO QUE ESTAMOS MODIFICANDO!
@app.route("/cadastro", methods = ["POST", "GET"])
def cadastrar_pessoa():
    if request.method == "POST":
        nome = request.form["nome"] # O objeto request é do próprio Flask.
        email = request.form["email"] # [chave do dicionário]
        senha = request.form["password"]
        return redirect(url_for("login.html")) # ????
    else:
        return render_template('cadastro.html')


@app.route("/cadastrar_sala")   
def cadastrar_sala():
    return render_template('cadastrar-sala.html')

@app.route("/reservar-sala")
def reservar_sala():
    return render_template('reservar-sala.html')

@app.route("/listar_salas")
def listar_sala():
    return render_template('listar-salas.html')

@app.route("/reservas")
def reservas():
    return render_template('reservas.html')

@app.route("/detalhe_reserva")
def detalhe_reserva():
    return render_template('reserva/detalhe-reserva.html')



""""def get_questoes(disciplina):
    todas_questoes = []
    with open(disciplina) as Gabriel_file:
        questoes = csv.reader(Gabriel_file, delimiter='|')
        for questao in questoes:
            todas_questoes.append(questao)
    return todas_questoes
Quem s„o os participantes da BRIC'S? |Brasil, R˙ssia, It·lia, China e Coreia do Sul| 1"""
