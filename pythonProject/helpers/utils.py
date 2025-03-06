import uuid
import random


# gera ID para identificar processo
def gera_id_processo():
    id_processo = uuid.uuid4()
    return id_processo


# gera grau de confiabilidade
def gera_grau_confiabilidade():
    grau = random.randint(0, 10)
    return grau