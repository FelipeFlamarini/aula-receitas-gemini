from flask_openapi3 import OpenAPI
import google.generativeai as genai
import os

from schemas import *

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
prompt = """
Baseado em uma lista de ingredientes fornecida pelo usuário, você será responsável por sugerir uma receita culinária que o usuário possa cozinhar.
Sua resposta deve conter apenas o título da receita, os ingredientes e suas quantidades.
Você pode considerar que o usuário possui ingredientes e temperos básicos e comuns residencialmente, como água e sal.
A receita deve usar SOMENTE os ingredientes fornecidos pelo usuário, e nada além disso.
A receita deve usar o MÁXIMO de ingredientes possíveis, mas podem existir casos em que não é possível combinar todos os ingredientes do usuário.
A receita deve usar quantidades dos ingredientes que sirvam o almoço de uma pessoa.
Suponha que o usuário possui os equipamentos necessários para a culinária básica, como frigideira, panela de pressão, fogão, forno, microondas, entre outros.

Segue a lista de ingredientes fornecida pelo usuário: 
"""


app = OpenAPI(__name__, doc_prefix="")


@app.get("/teste")
def hello_world():
    return {"Hello": "World"}


@app.post("/recipe")
def post_ingredientes(form: RecipeForm):
    content = model.generate_content(prompt + form.ingredientes)
    return content.text
