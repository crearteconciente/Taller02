import re

def validar_telefono(telefono):

    patron = r'^\+\d{2}-\d{3}-\d{3}-\d{4}$'
    return re.match(patron, telefono) is not None