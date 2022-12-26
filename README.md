# estoque_cenco_server

Rotas da API:
// Consulta todos os itens contidos em estoque
127.0.0.1:8080/api/estoque

//Consulta todos os tipos peças cadastrados no banco
127.0.0.1:8080/api/tipospecas		

//Consulta todas as marcas cadastradas no banco
127.0.0.1:8080/api/marcas

//Consulta todas os modelos cadastrados no banco de dados 
127.0.0.1:8080/api/modelos		

//Cadastra um tipo de peça banco
127.0.0.1:8080/api/add/tipo
	Exemplo JSON:
		{
			"value": "Celular"
		}

//Cadastra uma marca no banco de dados
127.0.0.1:8080/api/add/marca	
	Exemplo JSON:
		{
			"value": "Phillips"
		}
		
//Cadastra um modelo em estoque
127.0.0.1:8080/api/add/modelo
	Exemplo JSON:
		{
			"id-tipo-produto": 1,
			"id-marca": 1,
			"nome-modelo": "Smart Things",
			"vida-util": 8
		}
		
//Cadastra uma peça no estoque
127.0.0.1:8080/api/add/pecaestoque
	Exemplo JSON:
		{
			"notaFiscal": "6756324789563",
			"idBandeira":7,
			"idTipoProduto": 1,
			"idMarca": 1,
			"idModelo": 4,
			"quantidade": 1,
			"valorUnitario": 45000.00,
			"dataCompra": "2022-08-12",
			"observacao": "teste de equipamenoto inativo - 2",
			"idStatus":0 
		}

			

