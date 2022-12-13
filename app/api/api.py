from app.db.configDataBase import dbConnect
from flask import jsonify, make_response, request

class api:
    def homepage():
        return "<h1>API Estoque CRA</h1>"

    def getTiposDePecas():
        cursor = dbConnect.cursor()
        cursor.execute("SELECT * FROM tbtipo_produto")
        db_tipos = cursor.fetchall()
        tipos = []
        for tipo in db_tipos:
            tipos.append(
                {
                    "id": tipo[0],
                    "value": tipo[1]
                }
            )
        cursor.close()
        return make_response(
            jsonify(
                tipos
            )
        )

    def getMarcas():
        cur = dbConnect.cursor()
        cur.execute("SELECT * FROM tbmarca")
        db_marcas = cur.fetchall()
        marcas = []
        for marca in db_marcas:
            marcas.append(
                {
                    "id": marca[0],
                    "value": marca[1]
                }
            )
        cur.close()
        return make_response(
            jsonify(marcas)
        )

    def getModelos():
        cur = dbConnect.cursor()
        cur.execute("SELECT * FROM tbmodelo")
        db_modelos = cur.fetchall()
        return make_response(
            jsonify(db_modelos)
        )

    def getEstoque():
        cur = dbConnect.cursor()
        cur.execute("""
            SELECT
                estoque.id, 
                produto.nmTipoProduto,
                modelo.nmModelo,
                marca.nmMarca, 
                bandeira.nmBandeira,
                estoque.notaFiscal,
                estoque.dataCompra,
                status.status 
            FROM 
                tbestoque as estoque
            INNER JOIN tbbandeira as bandeira
            on
                bandeira.id = estoque.idBandeira 
            INNER JOIN tbmodelo as modelo 
            on
                modelo.id = estoque.idModelo
            INNER JOIN tbtipo_produto as produto
            on
                produto.id = modelo.idTipoProduto 
            INNER JOIN tbmarca as marca
            on
                marca.id = modelo.idmarca
            inner join tbstatus_peca as status
            on
                status.id = estoque.idStatus
        """)
        estoque_db = cur.fetchall()
        itens = []
        for item in estoque_db:
            itens.append(
                {
                    "id": item[0],
                    "produto": item[1],
                    "modelo": item[2],
                    "marca": item[3],
                    "bandeira": item[4],
                    "nota_fiscal": item[5],
                    "data_compra": item[6],
                    "status": item[7]
                }
            )
        resp = make_response(jsonify(itens))
        resp.headers.set('content-type', 'text/plain')
        return resp

    #adiciona um tipo de produto no banco de dados
    def setTipoProduto():
        tipoProduto = request.json
        cursor = dbConnect.cursor()
        sql = f"INSERT INTO tbtipo_produto (nmTipoProduto) VALUES('{tipoProduto['value']}')"
        cursor.execute(sql)
        dbConnect.commit()
        cursor.close()
        return make_response(
            jsonify(
                tipo_Produto=tipoProduto,
                mensagem="Cadastrado com sucesso"
            )
        )

    #adiciona um tipo de marca no banco de dados
    def setMarca():
        marca = request.json
        cursor = dbConnect.cursor()
        sql = f"INSERT INTO tbmarca (nmMarca) VALUES('{marca['value']}')"
        cursor.execute(sql)
        dbConnect.commit()
        cursor.close()
        return make_response(
            jsonify(
                mensagem="Cadastrado com sucesso",
                marca=marca
            )
        )

    #adiciona um tipo de modelo no banco de dados
    def setModelo():
        modelo = request.json
        cursor = dbConnect.cursor()
        sql = f"INSERT INTO tbmodelo (nmModelo, idTipoProduto, idMarca, vidaUtilEmAno) VALUES('{modelo['nome-modelo']}', {modelo['id-tipo-produto']}, {modelo['id-marca']}, {modelo['vida-util']})"
        cursor.execute(sql)
        dbConnect.commit()
        cursor.close()
        return make_response(
            jsonify(
                mensagem="Cadastrado com sucesso",
                modelo=modelo
            )
        )

    #adiciona uma peça no banco de dados
    def setPecaEstoque():
        peca = request.json
        cur = dbConnect.cursor()
        sql = f"""
                INSERT INTO 
                    tbestoque (notaFiscal, idBandeira, idTipoProduto, idMarca, idModelo, quantidade, valorUnitario, dataCompra, observacao, idStatus) 
                VALUES(
                    '{peca['notaFiscal']}',
                    '{peca['idBandeira']}',
                    '{peca['idTipoProduto']}',
                    '{peca['idMarca']}',
                    '{peca['idModelo']}',
                    '{peca['quantidade']}',
                    '{peca['valorUnitario']}',
                    '{peca['dataCompra']}',
                    '{peca['observacao']}',
                    '{peca['idStatus']}'
                    )
                """
        cur.execute(sql)
        dbConnect.commit()
        cur.close()
        return make_response(
            jsonify(
                status="Peça cadastrada com sucesso!!",
                peca=peca
            )
        )
