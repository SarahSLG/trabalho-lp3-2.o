from flask import Flask, render_template, request, redirect, url_for
import csv
from reserva_app import funcoes

# REQUEST - importar solicitações com o modelo de renderização 

app = Flask("reservas")

@app.route("/")
def login():
    return render_template('login.html')


# responsável por renderizar a página cadastro pro usuário - método get
@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')


# Responsável por processar os dados do formulário da página de cadastro
@app.route("/cadastro", methods = ['POST'])
def cadastrar_pessoa():
    cod = funcoes.cadastro_arquivo()
    nome = request.form['nome'] # O objeto request é do próprio Flask.
    email = request.form['email'] # [chave do dicionário]
    senha = request.form['password'] 
    codigo = (len(cod))+2
    admin = False
    funcoes.salvar_cadastro(nome, email, senha, codigo, admin)
    return render_template('login.html')
        
@app.route("/cadastrar_sala")   
def cadastrar_sala():
    return render_template('cadastrar-sala.html')

@app.route("/cadastrar_sala", methods = ['POST'])
def formulario_sala():
    cod = funcoes.salas_arquivo()
    tipo = request.form['tipo']
    capacidade = request.form['capacidade'] # [chave do dicionário] 
    descricao = request.form['descricao']# O objeto request é do próprio Flask.
    codigo = (len(cod))+2
    ativo = True
    funcoes.cadastrar_salas(codigo, tipo, descricao, capacidade, ativo)
    return render_template('listar-salas.html', salas = funcoes.salas_arquivo())
    

@app.route("/reservar_sala")
def reservarsala(): 
    return render_template('reservar-sala.html', salas = funcoes.salas_arquivo())


@app.route("/reservar_sala", methods = ['POST'])
def reservar_sala():
    cod = funcoes.reservas_arquivo()
    codigo = len(cod)+1
    sala = request.form['sala']
    d_inicio = request.form['inicio']
    d_fim = request.form['fim']
    admin = False
    ativo = True
    funcoes.cadastrar_reserva(codigo, sala, d_inicio, d_fim, admin, ativo)
    return render_template('reserva/detalhe-reserva.html')

@app.route("/listar_salas")
def listar_sala():
    return render_template('listar-salas.html', salas = funcoes.salas_arquivo())

@app.route("/reservas")
def reservas():
    return render_template('reservas.html')

@app.route("/detalhe_reserva")
def detalhe_reserva():
    return render_template('reserva/detalhe-reserva.html')


