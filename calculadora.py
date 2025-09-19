# calculadora.py

def soma(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Os valores devem ser numéricos.")
    return a + b


def subtracao(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Os valores devem ser numéricos.")
    return a - b
