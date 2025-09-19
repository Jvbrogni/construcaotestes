import sqlite3
import requests


def conectarbanco():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome TEXT)')
    return conn, cursor


def cadastrarusuario(nome):
    if not nome:
        raise ValueError("Nome não pode ser vazio ou None")

    conn, cursor = conectarbanco()
    cursor.execute('INSERT INTO usuarios (nome) VALUES (?)', (nome,))
    conn.commit()
    cursor.execute('SELECT * FROM usuarios WHERE nome = ?', (nome,))
    return cursor.fetchone()


def buscar_usuario_api(usuario_id):
    url = f"https://jsonplaceholder.typicode.com/users/{usuario_id}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Falha ao obter usuário da API")

    return response.json()
