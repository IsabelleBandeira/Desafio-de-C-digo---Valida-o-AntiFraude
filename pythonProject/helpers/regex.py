import re

# REGEXs para validação
REGEX_CPF = re.compile(r"([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})")
REGEX_NOME_COMPLETO = re.compile(r"^[A-ZÀ-ÖØ-Ÿ][a-zà-öø-ÿ]+(?: [A-ZÀ-ÖØ-Ÿa-zà-öø-ÿ'-]+)+$")
REGEX_TELEFONE = re.compile(r"^\+?([0-9]{2,3})?\s?\(?([0-9]{2})\)?\s?[0-9]{4,5}-?[0-9]{4}$")
REGEX_EMAIL = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
REGEX_CEP = re.compile(r"(\d){5}-?(\d){3}")