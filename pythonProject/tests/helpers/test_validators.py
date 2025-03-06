import pytest
import requests
from unittest.mock import patch
from fastapi import HTTPException
from helpers.validators import valida_cpf, valida_nome_completo, valida_endereco, valida_data_nasc, valida_email, \
    valida_telefone
from models.models import EnderecoCliente


# mock da resposta da api viacep em caso de erro de servidor
def mock_server_error_viacep_api(*args, **kwargs):
    raise requests.exceptions.RequestException("500 Server Error")


# tests valida_cpf
def test_valida_cpf_should_succeed():
    mock_cpf = "000.000.000-00"
    response = valida_cpf(mock_cpf)
    print(response)
    assert response[0] is True
    assert response[1] is None


def test_valida_cpf_should_fail():
    mock_cpf = "000.0A0.000-00"
    response = valida_cpf(mock_cpf)
    print(response)
    assert response[0] is False
    assert response[1] is not None


# tests valida_nome
def test_valida_nome_completo_should_succeed():
    mock_nome_completo = "Isabelle Bandeira"
    response = valida_nome_completo(mock_nome_completo)
    print(response)
    assert response[0] is True
    assert response[1] is None


def test_valida_nome_completo_should_fail():
    mock_nome_completo = "IsabelleBandeira"
    response = valida_nome_completo(mock_nome_completo)
    print(response)
    assert response[0] is False
    assert response[1] is not None


# tests valida_cep
def test_valida_endereco_should_succeed():
    mock_endereco = EnderecoCliente(
        cep="01001-000",
        rua="Praça da Sé",
        numero="1",
        bairro="Sé",
        cidade="São Paulo",
        estado="SP"
    )
    response = valida_endereco(mock_endereco)
    print(response)
    assert response[0] is True
    assert response[1] is None


def test_valida_endereco_should_fail():
    mock_endereco = EnderecoCliente(
        cep="0100A-000",
        rua="Praça da Sé",
        numero="1",
        bairro="Sé",
        cidade="São Paulo",
        estado="SP"
    )
    response = valida_endereco(mock_endereco)
    print(response)
    assert response[0] is False
    assert response[1] is not None


# Test case: Server error (500 response)
@patch("requests.get", side_effect=mock_server_error_viacep_api)
def test_valida_endereco_server_error(mock_get):
    endereco_mock = type("EnderecoMock", (object,), {"cep": "12345-678"})

    with pytest.raises(HTTPException) as exc_info:
        valida_endereco(endereco_mock)

    assert exc_info.value.status_code == 500  # Internal Server Error


# tests valida_data_nasc
def test_valida_data_nasc_should_succeed():
    mock_data_nasc = "09/02/2005"
    response = valida_data_nasc(mock_data_nasc)
    print(response)
    assert response[0] is True
    assert response[1] is None


def test_valida_data_nasc_should_fail():
    mock_data_nasc = "09/02/000000"
    response = valida_data_nasc(mock_data_nasc)
    print(response)
    assert response[0] is False
    assert response[1] is not None


def test_valida_data_nasc_should_fail_with_custom_message():
    mock_data_nasc = "09/02/1800"
    response = valida_data_nasc(mock_data_nasc)
    print(response)
    assert response[0] is False
    assert response[1] is not None
    assert "o Cliente teria" in response[1]


# tests valida_email
def test_valida_email_should_succeed():
    mock_email = "fulano.dasilva35@gmail.com"
    response = valida_email(mock_email)
    print(response)
    assert response[0] is True
    assert response[1] is None


def test_valida_email_should_fail():
    mock_email = "fulano.dasilva35@gm_ail.com"
    response = valida_email(mock_email)
    print(response)
    assert response[0] is False
    assert response[1] is not None


# tests valida_telefone
def test_valida_telefone_should_succeed():
    mock_telefone = "(00)000000000"
    response = valida_telefone(mock_telefone)
    print(response)
    assert response[0] is True
    assert response[1] is None


def test_valida_telefone_should_fail():
    mock_telefone = "000000000"
    response = valida_telefone(mock_telefone)
    print(response)
    assert response[0] is False
    assert response[1] is not None
