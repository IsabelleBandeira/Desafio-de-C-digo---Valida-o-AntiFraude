import uuid
from argparse import Namespace
from datetime import datetime
from main import recebe_payload, avalia_grau_confiabilidade, define_detalhes
from models.models import Cliente, EnderecoCliente


# tests recebe_payload
def test_recebe_payload_should_succeed():
    mock_endereco = EnderecoCliente(
        cep="01001-000",
        rua="Praça da Sé",
        numero="1",
        bairro="Sé",
        cidade="São Paulo",
        estado="SP"
    )
    mock_data = Cliente(
        id="1234567890",
        cpf="000.000.000-00",
        nome_cliente="Isabelle Bandeira",
        telefone="11977515087",
        email="fulano@gmail.com",
        data_nasc="09/02/2005",
        endereco=mock_endereco,
        nome_mae="Ciclana Da Silva"
    )
    response = recebe_payload(mock_data)
    response_json = Namespace(**response)
    id_validacao = response_json.id_validacao
    data_hora = response_json.data_hora
    id_cliente = response_json.id_cliente
    grau_confiabilidade = response_json.grau_confiabilidade
    detalhes = response_json.detalhes
    assert uuid.UUID(id_validacao, version=4)
    assert data_hora == str(datetime.now())
    assert id_cliente == "1234567890"
    assert 0 <= int(grau_confiabilidade) <= 10
    assert detalhes == "Cliente validado com sucesso!"


def test_recebe_payload_should_fail():
    mock_endereco = EnderecoCliente(
        cep="0100A-000",
        rua="Praça da Sé",
        numero="1",
        bairro="Sé",
        cidade="São Paulo",
        estado="SP"
    )
    mock_data = Cliente(
        id="1234567890",
        cpf="000.000.000-00",
        nome_cliente="Isabelle Bandeira",
        telefone="11977515087",
        email="fulano@gmail.com",
        data_nasc="09/02/2005",
        endereco=mock_endereco,
        nome_mae="Ciclana Da Silva"
    )
    response = recebe_payload(mock_data)
    response_json = Namespace(**response)
    id_validacao = response_json.id_validacao
    data_hora = response_json.data_hora
    id_cliente = response_json.id_cliente
    grau_confiabilidade = response_json.grau_confiabilidade
    detalhes = response_json.detalhes
    assert uuid.UUID(id_validacao, version=4)
    assert data_hora == str(datetime.now())
    assert id_cliente == "1234567890"
    assert int(grau_confiabilidade) == 0
    assert detalhes == "ERRO! CEP inválido."


# tests avalia_grau_confiabilidade
def test_avalia_grau_confiabilidade_should_return_random_number():
    mock_is_valid_cpf = True
    mock_is_valid_nome_cliente = True
    mock_is_valid_telefone = True
    mock_is_valid_email = True
    mock_is_valid_data_nasc = True
    mock_is_valid_endereco = True
    mock_is_valid_nome_mae = True
    response = avalia_grau_confiabilidade(mock_is_valid_cpf, mock_is_valid_nome_cliente, mock_is_valid_telefone,
                                          mock_is_valid_email, mock_is_valid_data_nasc, mock_is_valid_endereco,
                                          mock_is_valid_nome_mae)
    assert 0 < response <= 10


def test_avalia_grau_confiabilidade_should_return_zero():
    mock_is_valid_cpf = True
    mock_is_valid_nome_cliente = False
    mock_is_valid_telefone = True
    mock_is_valid_email = True
    mock_is_valid_data_nasc = True
    mock_is_valid_endereco = True
    mock_is_valid_nome_mae = True
    response = avalia_grau_confiabilidade(mock_is_valid_cpf, mock_is_valid_nome_cliente, mock_is_valid_telefone,
                                          mock_is_valid_email, mock_is_valid_data_nasc, mock_is_valid_endereco,
                                          mock_is_valid_nome_mae)
    assert response == 0


# tests define_detalhes
def test_define_detalhes_should_return_default_message():
    mock_lista = [
        None,
        None,
        None
    ]
    response = define_detalhes(mock_lista)
    assert "Cliente validado com sucesso!" in response


def test_define_detalhes_should_return_custom_message():
    mock_lista = [
        "CPF é inválido.",
        None,
        None
    ]
    response = define_detalhes(mock_lista)
    assert "CPF é inválido." in response
