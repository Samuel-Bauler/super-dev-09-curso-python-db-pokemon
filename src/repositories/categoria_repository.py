from typing import List
from src.schemas.categoria import Categoria

from src.database.conexao import conectar

def consultar_todos() -> List[Categoria]:
    # `with` garante que a conexao com o banco de dados seja fechada,
    # independente se deu algum erro ou não. Caso contrario cada requisição
    # deixaria uma conexao aberta
    with conectar() as conexao:
        with conexao.cursor() as cursor:

            cursor.execute("SELECT id, nome FROM categorias")
            registros = cursor.fetchall()
            
    categorias = []
    for registros in registros:
        categoria = categoria(id=registro["id"], nome=registro["nome"])
        categorias.append(categoria)
    return categorias

