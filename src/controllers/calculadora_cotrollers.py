from fastapi import APIRouter


router = APIRouter()

@router.get("/mensagem")
def mensagem():
    """ROta para uma mensagem de boas vindas"""
    return {"mensagem": "Olá mundo"}


# Query params: numero1 numero2
# http://localhost:8000/calculadora/somar?numero1=2&numero2=5
@router.get("/calculadora/somar")
def somar(numero1: int, numero2: int):
    soma = numero1 + numero2
    return {
        "resultado": soma
    }


# http://localhost:8000/calculadora/imc?peso=70&altura=1.50
@router.get("/calculadora/imc")
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


@router.get("/concatenar")
def concatenar(nome: str, sobrenome: str):
    nome_completo = nome + sobrenome
    return {
        "nome_completo": nome_completo
    }


@router.get("/calcular/desconto")
def calcular_desconto(preco: float, percentual: float):
    desconto = preco * percentual
    preco_total = preco - desconto

    return {
        "preco": preco_total
    }


@router.get("/calcular/media")
def calcular_media(nota1, nota2, nota3, nota4):
    notas = [nota1, nota2, nota3, nota4]
    calcular_media = (nota1 + nota2 + nota3 + nota4) / 4

    return {
        "notas": notas,
        "media": calcular_media
    }