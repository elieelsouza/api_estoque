from flask import Flask

from app.api.api import api
from app.db import connect

app = Flask(__name__)
connect.init_app(app)

@app.route("/", methods=["GET"])
def homepage():
    return api.homepage()


@app.route("/api/tipospecas", methods=["GET"])
def getTiposDePecas():
    return api.getTiposDePecas()

@app.route("/api/marcas", methods=["GET"])
def getMarcas():
    return api.getMarcas()

@app.route("/api/modelos", methods=["GET"])
def getModelos():
    return api.getModelos()


@app.route("/api/estoque", methods=["GET"])
def getEstoque():
    return api.getEstoque()


@app.route("/api/add/tipo", methods=["POST"])
def setTipoProduto():
    return api.setTipoProduto()


@app.route("/api/add/marca", methods=["POST"])
def setMarca():
    return api.setMarca()


@app.route("/api/add/modelo", methods=["POST"])
def setModelo():
    return api.setModelo()


@app.route("/api/add/pecaestoque", methods=["POST"])
def setPecaEstoque():
    return api.setPecaEstoque()


if __name__ == "__main__":
    # from app.db.connection import db
    # db.create_all()
    app.run()
