from helpers.utils import gera_grau_confiabilidade, gera_id_processo
from fastapi import FastAPI, HTTPException
from models.models import Cliente
from datetime import datetime
from helpers.validators import valida_cpf, valida_email, valida_endereco, valida_telefone, \
    valida_nome_completo, valida_data_nasc
import logging


app = FastAPI()


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@app.get("/")
def boas_vindas():
    return {"details": "Bem-vindo(a)! Para ver a documentação da API, coloque /docs depois da url"}


@app.post("/validacao")
def recebe_payload(data: Cliente):
    try:
        # chama métodos de validação
        logging.info("INICIO DAS VALIDACOES")

        is_valid_cpf = valida_cpf(data.cpf)
        is_valid_nome_completo = valida_nome_completo(data.nome_cliente)
        is_valid_telefone = valida_telefone(data.telefone)
        is_valid_email = valida_email(data.email)
        is_valid_data_nasc = valida_data_nasc(data.data_nasc)
        is_valid_endereco = valida_endereco(data.endereco)
        is_valid_nome_mae = valida_nome_completo(data.nome_mae)

        logging.info("Gerando grau de confiabilidade...")
        # avalia grau de confiabilidade
        grau_confiabilidade = avalia_grau_confiabilidade(is_valid_cpf[0], is_valid_nome_completo[0],
                                                         is_valid_telefone[0], is_valid_email[0], is_valid_data_nasc[0],
                                                         is_valid_endereco[0], is_valid_nome_mae[0])

        # define campo 'detalhes'
        lista_detalhes = is_valid_cpf[1], is_valid_nome_completo[1], is_valid_telefone[1], is_valid_email[1], \
            is_valid_data_nasc[1], is_valid_endereco[1], is_valid_nome_mae[1]
        detalhes = define_detalhes(lista_detalhes)

        logging.info("Gerando payload de resposta...")
        # gera json de resposta
        data_hora = datetime.now()
        id_cliente = data.id
        id_process = gera_id_processo()
        response = {
            "id_validacao": f"{id_process}",
            "data_hora": f"{data_hora}",
            "id_cliente": f"{id_cliente}",
            "grau_confiabilidade": f"{grau_confiabilidade}",
            "detalhes": f"{detalhes}"
        }
        logging.info("PROCESSO FINALIZADO.")
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro do servidor: {str(e)}")


# valida se algum dado é inválido
def avalia_grau_confiabilidade(is_valid_cpf, is_valid_nome_cliente, is_valid_telefone, is_valid_email,
                               is_valid_data_nasc, is_valid_endereco,
                               is_valid_nome_mae):
    if all([is_valid_cpf, is_valid_nome_cliente, is_valid_telefone, is_valid_email, is_valid_data_nasc,
            is_valid_endereco, is_valid_nome_mae]):
        grau_confiabilidade = gera_grau_confiabilidade()
        return grau_confiabilidade
    else:
        grau_confiabilidade = 0
        return grau_confiabilidade


# define campo 'detalhes'
def define_detalhes(lista):
    detalhes = "Cliente validado com sucesso!"
    for x in lista:
        if x is not None:
            print(x)
            detalhes = x
    return detalhes
