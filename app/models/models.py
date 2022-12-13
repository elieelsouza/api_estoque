from app.db.configDataBase import Base, db
from sqlalchemy_serializer import SerializerMixin


class TipoProduto(Base, SerializerMixin):
    __tablename__ = "tbTIPO_PRODUTO"
    id = db.Column(db.Integer, primary_key=True)
    nmTipoProduto = db.Column(db.String(40), nullable=False)
    TipoProduto_ = db.relationship(
        'Modelo', backref='tbTIPO_PRODUTO', lazy=True)

    # declaração de relacionamento com outras tabelas
    Estoque_ = db.relationship('Estoque', backref='tbTIPO_PRODUTO', lazy=True)
    BaixaPeca_ = db.relationship(
        'BaixaPeca', backref='tbTIPO_PRODUTO', lazy=True)

    def __init__(self, id, nmTipoProduto):
        self.id = id
        self.nmTipoProduto = nmTipoProduto


class Marca(Base, SerializerMixin):
    __tablename__ = "tbMARCA"
    id = db.Column(db.Integer, primary_key=True)
    nmMarca = db.Column(db.String(40), nullable=False)

    # declaração de relacionamento com outras tabelas
    Marca_ = db.relationship('Modelo', backref='tbMARCA', lazy=True)
    Estoque_ = db.relationship('Estoque', backref='tbMARCA', lazy=True)
    BaixaPeca_ = db.relationship('BaixaPeca', backref='tbMARCA', lazy=True)

    def __init__(self, id, nmMarca):
        self.id = id
        self.nmMarca = nmMarca


class Modelo(Base, SerializerMixin):
    __tablename__ = 'tbMODELO'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    idTipoProduto = db.Column(db.Integer, db.ForeignKey('tbTIPO_PRODUTO.id'))
    idMarca = db.Column(db.Integer, db.ForeignKey('tbMARCA.id'))
    nmModelo = db.Column(db.String(40), nullable=False)
    vidaUtilEmAno = db.Column(db.Integer, nullable=False)

    # declaração de relacionamento com outras tabelas
    Estoque_ = db.relationship('Estoque', backref='tbMODELO', lazy=True)
    BaixaPeca_ = db.relationship('BaixaPeca', backref='tbMODELO', lazy=True)

    def __init__(self, id, idTipoProduto, idMarca, nmModelo, vidaUtilEmAno):
        self.id = id
        self.idTipoProduto = idTipoProduto
        self.idMarca = idMarca
        self.nmModelo = nmModelo
        self.vidaUtilEmAno = vidaUtilEmAno


class Bandeira(Base, SerializerMixin):
    __tablename__ = 'tbBANDEIRA'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nmBandeira = db.Column(db.String(60), nullable=False)

    # declaração de relacionamento com outras tabelas
    Estoque_ = db.relationship('Estoque', backref='tbBANDEIRA', lazy=True)
    Loja_ = db.relationship('Loja', backref='tbBANDEIRA', lazy=True)
    BaixaPeca_ = db.relationship('BaixaPeca', backref='tbBANDEIRA', lazy=True)

    def __init__(self, id, nmBandeira):
        self.id = id
        self.nmBandeira = nmBandeira


class CampoTi(Base, SerializerMixin):
    __tablename__ = 'tbCAMPO_TI'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nmCampo = db.Column(db.String(100), nullable=False)

    # declaração de relacionamento com outras tabelas
    Loja_ = db.relationship("Loja", backref='tbCAMPO_TI', lazy=True)

    def __init__(self, id, nmCampo):
        self.id = id
        self.nmCampo = nmCampo


class CoordCampoTi(Base, SerializerMixin):
    __tablename__ = 'tbCOORD_CAMPO'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nmCoordCampo = db.Column(db.String(100), nullable=False)

    # declaração de relacionamento com outras tabelas
    Loja_ = db.relationship("Loja", backref='tbCOORD_CAMPO', lazy=True)

    def __init__(self, id, nmCoordCampo):
        self.id = id
        self.nmCoordCampo = nmCoordCampo


class TipoLoja(Base, SerializerMixin):
    __tablename__ = 'tbTIPO_LOJA'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tipoLoja = db.Column(db.String(25), nullable=False)

    # declaração de relacionamento com outras tabelas
    Loja_ = db.relationship('Loja', backref='tbTIPO_LOJA', lazy=True)

    def __init__(self, id, tipoLoja):
        self.id = id
        self.tipoLoja = tipoLoja


class ModalidadeLoja(Base, SerializerMixin):
    __tablename__ = 'tbMODALIDADE_LOJA'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nmModalidade = db.Column(db.String(25), nullable=False)

    # declaração de relacionamento com outras tabelas
    Loja_ = db.relationship('Loja', backref='tbMODALIDADE_LOJA', lazy=True)

    def __init__(self, id, nmModalidade):
        self.id = id
        self.nmModalidade = nmModalidade


class Loja(Base, SerializerMixin):
    __tablename__ = 'tbLOJA'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nmLoja = db.Column(db.String(25), nullable=False)
    cnpjLoja = db.Column(db.String(18), nullable=False)
    enderecoLoja = db.Column(db.String(70), nullable=False)
    bairroLoja = db.Column(db.String(35), nullable=False)
    cidadeLoja = db.Column(db.String(35), nullable=False)
    estadoLoja = db.Column(db.String(15), nullable=False)
    cepLoja = db.Column(db.String(9), nullable=False)
    idCoordCampoTi = db.Column(db.Integer, db.ForeignKey('tbCOORD_CAMPO.id'))
    idCampoTi = db.Column(db.Integer, db.ForeignKey('tbCAMPO_TI.id'))
    tipoLoja = db.Column(db.Integer, db.ForeignKey('tbTIPO_LOJA.id'))
    idModalidade = db.Column(db.Integer, db.ForeignKey('tbMODALIDADE_LOJA.id'))
    idBandeira = db.Column(db.Integer, db.ForeignKey('tbBANDEIRA.id'))

    # declaração de relacionamento com outras tabelas
    Estoque_ = db.relationship('Estoque', backref='tbLOJA', lazy=True)
    BaixaPeca_ = db.relationship('BaixaPeca', backref='tbLOJA', lazy=True)

    def __init__(
        self, id, nmLoja, cnpjLoja, enderecoLoja, bairroLoja,
        cidadeLoja, estadoLoja, cepLoja, idCoordCampoTi,
        idCampoTi, tipoLoja, idModalidade, idBandeira
    ):
        self.id = id
        self.nmLoja = nmLoja
        self.cnpjLoja = cnpjLoja
        self.enderecoLoja = enderecoLoja
        self.bairroLoja = bairroLoja
        self.cidadeLoja = cidadeLoja
        self.estadoLoja = estadoLoja
        self.cepLoja = cepLoja
        self.idCoordCampoTi = idCoordCampoTi
        self.idCampoTi = idCampoTi
        self.tipoLoja = tipoLoja
        self.idModalidade = idModalidade
        self.idBandeira = idBandeira

class StatusPeca(Base, SerializerMixin):
    __tablename__ = 'tbSTATUS_PECA'
    id = db.Column(db.Integer, primary_key=True, nullable=True, autoincrement=False)
    status = db.Column(db.String(10), nullable=False)

    # declaração de relacionamento com outras tabelas
    Estoque_ =  db.relationship('Estoque', backref='tbSTATUS_PECA', lazy=True)
    BaixaPeca_ = db.relationship('BaixaPeca', backref='tbSTATUS_PECA', lazy=True)

    def __init__(self, id, status):
        self.id = id
        self.stauts = status

class Estoque(Base, SerializerMixin):
    __tablename__ = 'tbESTOQUE'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    notaFiscal = db.Column(db.String(40), nullable=False)
    idBandeira = db.Column(db.Integer, db.ForeignKey(
        'tbBANDEIRA.id'), nullable=False)
    idTipoProduto = db.Column(db.Integer, db.ForeignKey(
        'tbTIPO_PRODUTO.id'), nullable=False)
    idMarca = db.Column(db.Integer, db.ForeignKey(
        'tbMARCA.id'), nullable=False)
    idModelo = db.Column(db.Integer, db.ForeignKey(
        'tbMODELO.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    valorUnitario = db.Column(db.Float, nullable=False)
    dataCompra = db.Column(db.Date)
    observacao = db.Column(db.Text)
    idStatus = db.Column(db.Integer, db.ForeignKey('tbSTATUS_PECA.id'))

    def __init__(self, id, idBandeira, notaFiscal, idModelo, valorUnitario, quantidade, dataCompra, observacao, idStatus):
        self.id = id
        self.idBandeira = idBandeira
        self.notaFiscal = notaFiscal
        self.idModelo = idModelo
        self.valorUnitario = valorUnitario
        self.quantidade = quantidade
        self.dataCompra = dataCompra
        self.observacao = observacao
        self.idStatus = idStatus

class TipoServico(Base, SerializerMixin):
    __tablename__ = 'tbTIPO_SERVICO'
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    nmServico = db.Column(db.String(30), nullable=False)

    BaixaPeca_ = db.relationship(
        'BaixaPeca', backref='tbTIPO_SERVICO', lazy=True)

    def __init__(self, id, nmServico):
        self.id = id
        self.nmServico = nmServico  
    
class BaixaPeca(Base, SerializerMixin):
    __tablename__ = 'tbBAIXA_PECA'
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    idBandeira = db.Column(db.Integer, db.ForeignKey(
        'tbBANDEIRA.id'), nullable=False)
    idLocalDestino = db.Column(
        db.Integer, db.ForeignKey('tbLOJA.id'), nullable=False)
    idTipoPeca = db.Column(db.Integer, db.ForeignKey(
        'tbTIPO_PRODUTO.id'), nullable=False)
    idMarca = db.Column(db.Integer, db.ForeignKey(
        'tbMARCA.id'), nullable=False)
    idModelo = db.Column(db.Integer, db.ForeignKey(
        'tbMODELO.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    idTipoServico = db.Column(db.Integer, db.ForeignKey(
        'tbTIPO_SERVICO.id'), nullable=False)
    observacao = db.Column(db.Text)
    idStatus = db.Column(db.Integer, db.ForeignKey('tbSTATUS_PECA.id'))


    def __init__(self, id, idBandeira, idLocalDestino, idTipoPeca, idMarca, idModelo, quantidade, idTipoServico, observacao):
        self.id = id
        self.idBandeira = idBandeira
        self.idLocalDestino = idLocalDestino
        self.idTipoPeca = idTipoPeca
        self.idMarca = idMarca
        self.idModelo = idModelo
        self.quantidade = quantidade
        self.idTipoServico = idTipoServico
        self.observacao = observacao


class User(Base, SerializerMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))
