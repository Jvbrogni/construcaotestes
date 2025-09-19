import pytest
from servico import cadastrarusuario, buscar_usuario_api


def testcadastrousuario():
    resultado = cadastrarusuario("João")
    assert resultado[1] == "João"


def testcadastroinvalido():
    with pytest.raises(ValueError):
        cadastrarusuario(None)


def test_buscar_usuario_api():
    usuario = buscar_usuario_api(1)
    assert usuario["id"] == 1
    assert "username" in usuario
    assert "email" in usuario
