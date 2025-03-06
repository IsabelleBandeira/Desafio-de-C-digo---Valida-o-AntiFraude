from typing import Optional
from pydantic import BaseModel

class EnderecoCliente(BaseModel):
    cep: str
    rua: Optional[str] = None
    numero: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None


class Cliente(BaseModel):
    id: str
    cpf: str
    nome_cliente: str
    telefone: str
    email: str
    data_nasc: str
    endereco: EnderecoCliente
    nome_mae: str
