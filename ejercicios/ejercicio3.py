import re

def validar_email(email):
    patron = r'^[a-zA-Z0-9._`]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}$'
    return re.match(patron, email) is not None
