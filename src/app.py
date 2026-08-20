from fastapi import FastAPI
from pathlib import Path
import sys

# Permite rodar com `py src/app.py`: coloca a raiz do projeto no sys.path
# para que os imports `from src import . ` funcionem corretamente
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

app = FastAPI(
    title= "Pokemon API",
    description="Projeto para batalhas de pokemons",
    version="0.1.0"
)

@app.get("/mensagem")
def mensagem():
    """ROta para uma mensagem de boas vindas"""
    return {"mensagem": "Olá mundo"}


# Query params: numero1 numero2
# http://localhost:8000/calculadora/somar?numero1=2&numero2=5
@app.get("/calculadora/somar")
def somar(numero1: int, numero2: int):
    soma = numero1 + numero2
    return {
        "resultado": soma
    }
# http://localhost:8000/calculadora/imc?peso=70&altura=1.50
@app.get("/calculadora/imc")
def calcular_imc(peso: float, altura: float):
    imc = peso / altura **2

    if imc < 18.5:
        classificacao = "abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "obesidade"

    return {
        "peso": peso,
        "altura": altura,
        "imc": round(imc, 2),
        "classificacao": classificacao
    }

@app.get("/concatenar")
def concatenar(nome: str, sobrenome: str):
    nome_completo = nome + sobrenome
    return {
        "nome_completo": nome_completo
    }

@app.get("/calcular/desconto")
def calcular_desconto(preco: float, percentual: float):
    desconto = preco * percentual
    preco_total = preco - desconto

    return {
        "preco": preco_total
    }


@app.get("/calcular/media")
def calcular_media(nota1, nota2, nota3, nota4):
    notas = [nota1, nota2, nota3, nota4]
    calcular_media = (nota1 + nota2 + nota3 + nota4) / 4

    return {
        "notas": notas,
        "media": calcular_media
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.app:app", host="127.0.0.1", port=8000, reload=True)