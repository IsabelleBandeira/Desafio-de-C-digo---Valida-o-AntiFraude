# Desafio-de-Código---Validação-AntiFraude

Essa é uma API que recebe dados pessoais, os valida e retorna uma nota representando a confiabilidade das informações

URL da API: http://127.0.0.1:8000/validacao

Exemplo de JSON esperado pela API:
  {
	"id": "2bdd41da-0875-4451-920a-e6c73f2b5b3",
	"cpf": "000.000.000-00",
	"nome_cliente": "Isabelle Bandeira",
	"telefone": "+55(11)00000-0000",
	"email": "fulano@gmail.com",
	"data_nasc": "19/12/1987",
	"endereco": {
		"cep": "01001-000",
		"rua": "Praça da Sé",
		"numero": "1",
		"bairro": "Sé",
		"cidade": "São Paulo",
		"estado": "SP"
	},
	"nome_mae": "Ciclana Da Silva"
}

DOC da API: http://127.0.0.1:8000/docs

---------------------------------------------

Essa solução usa Python3.11, um servidor uvicorn e o framework FastAPI para rodar.

Além dessas, algumas bibliotecas usadas foram:
pytest
request
pydantic
typing
re
