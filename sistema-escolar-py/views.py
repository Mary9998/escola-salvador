from main import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/professor/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("professor.html", nome_usuario=nome_usuario)

@app.route("/alunos")
def alunnos():
    return render_template("alunos.html")

@app.route("/materias")
def materias():
    return render_template("materias.html")

@app.route("/calendario")
def calendario():
    return render_template("calendario.html")

@app.route("/boletim")
def boletim():
    return render_template("boletim.html")

@app.route("/faltas")
def faltas():
    return render_template("faltas.html")

@app.route("/configuracao")
def configuracao():
    return render_template("configuracao.html")



