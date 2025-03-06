import logging
from fastapi import HTTPException
from helpers.regex import REGEX_TELEFONE, REGEX_CEP, REGEX_EMAIL, REGEX_CPF, REGEX_NOME_COMPLETO
from datetime import datetime
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def valida_cpf(cpf):
    logging.info("Iniciando validação do CPF...")
    if REGEX_CPF.search(cpf):
        is_valid_cpf = True
        detalhes = None
    else:
        is_valid_cpf = False
        detalhes = "ERRO! CPF inválido."
    logging.info("CPF validado.")
    return is_valid_cpf, detalhes


def valida_nome_completo(nome_completo):
    logging.info("Iniciando validação de nome...")
    if REGEX_NOME_COMPLETO.search(nome_completo):
        is_valid_nome_completo = True
        detalhes = None
    else:
        is_valid_nome_completo = False
        detalhes = f"ERRO! Nome '{nome_completo}' inválido."
    logging.info("Nome validado.")
    return is_valid_nome_completo, detalhes


def valida_telefone(telefone):
    logging.info("Iniciando validação de Telefone...")
    if REGEX_TELEFONE.search(telefone):
        is_valid_telefone = True
        detalhes = None
    else:
        is_valid_telefone = False
        detalhes = "ERRO! Telefone inválido."
    logging.info("Telefone validado.")
    return is_valid_telefone, detalhes


def valida_email(email):
    logging.info("Iniciando validação de Email...")
    if REGEX_EMAIL.search(email):
        is_valid_email = True
        detalhes = None
    else:
        is_valid_email = False
        detalhes = "ERRO! Email inválido."
    logging.info("Email validado.")
    return is_valid_email, detalhes


def valida_data_nasc(data_nasc):
    logging.info("Iniciando validação da Data de Nascimento...")
    try:
        # formata data de nascimento
        data_nasc_formatada = datetime.strptime(data_nasc, "%d/%m/%Y")
        current_year = datetime.now().year
        idade_cliente = current_year - data_nasc_formatada.year

        # valida idade do cliente
        if idade_cliente < 150:
            is_valid_data_nasc = True
            detalhes = None
        else:
            is_valid_data_nasc = False
            detalhes = f"ERRO! Data de Nascimento inválida: o Cliente teria {idade_cliente} anos."
    except ValueError as err:
        logging.error(err)
        is_valid_data_nasc = False
        detalhes = "ERRO! Data de Nascimento inválida."
    logging.info("Data de Nascimento validada.")
    return is_valid_data_nasc, detalhes


def valida_endereco(endereco):
    logging.info("Iniciando validação de Endereço...")

    is_valid_endereco = False
    detalhes = "ERRO! CEP inválido."

    # formata CEP
    cep = endereco.cep
    if REGEX_CEP.search(cep):
        if "-" in cep:
            cep = cep.replace("-", "")
        try:
            # procura CEP na API
            response = requests.get(url="https://viacep.com.br/ws/" + cep + "/json/", timeout=5)
            if response.status_code == 200 and "erro" not in response.json():
                is_valid_endereco = True
                detalhes = None
        except requests.exceptions.RequestException as err:
            logging.error(f"Erro ao acessar ViaCEP: {err}")
            raise HTTPException(status_code=500, detail="Erro ao consultar CEP. Tente novamente mais tarde.")
    else:
        is_valid_endereco = False
        detalhes = "ERRO! CEP inválido."
    logging.info("Endereço validado.")
    return is_valid_endereco, detalhes
