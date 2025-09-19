import pytest
from calculadora import soma, subtracao


# ----------- Testes da função soma -----------

def test_soma_positivos():
    assert soma(2, 3) == 5


def test_soma_negativos():
    assert soma(-1, -1) == -2


def test_soma_zero():
    assert soma(0, 5) == 5


def test_soma_invalida():
    with pytest.raises(ValueError):
        soma("a", 2)


def test_soma_grandes_numeros():
    assert soma(1e10, 1e10) == 2e10


# ----------- Testes da função subtração -----------

def test_subtracao_positivos():
    assert subtracao(5, 3) == 2


def test_subtracao_negativos():
    assert subtracao(-5, -2) == -3


def test_subtracao_zero():
    assert subtracao(5, 0) == 5


def test_subtracao_invalida():
    with pytest.raises(ValueError):
        subtracao("a", 2)


def test_subtracao_grandes_numeros():
    assert subtracao(1e10, 1e5) == 9999900000.0
