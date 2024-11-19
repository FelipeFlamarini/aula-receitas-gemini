from flask_openapi3 import OpenAPI, Tag, Info, APIView
import google.generativeai as genai
import os

from schemas import *

info = Info(title="book API", version="1.0.0")
app = OpenAPI(__name__, info=info)
api_view_testing = APIView(url_prefix="/api/v1", view_tags=[Tag(name="testing")])
api_view_recipes = APIView(url_prefix="/api/v1", view_tags=[Tag(name="recipes")])
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


@api_view_testing.route("/testing")
class TesteAPIView:
    @api_view_testing.doc()
    def get(self):
        return {"Hello": "World"}

    @api_view_testing.doc()
    def post(self, form: TestingPostForm):
        return form.model_dump()


@api_view_recipes.route("/recipe")
class RecipesAPIView:
    prompt = """
    Baseado em uma lista de ingredientes fornecida pelo usuário, você será responsável por sugerir uma receita culinária que o usuário possa cozinhar.
    A receita deve usar SOMENTE os ingredientes fornecidos pelo usuário, e nada além disso.
    A receita deve usar o MÁXIMO de ingredientes possíveis, mas podem existir casos em que não é possível combinar todos os ingredientes do usuário.
    A receita deve usar quantidades dos ingredientes que sirvam o almoço de uma pessoa.
    Suponha que o usuário possui os equipamentos necessários para a culinária básica, como frigideira, panela de pressão, fogão, forno, microondas, entre outros.

    Segue a lista de ingredientes fornecida pelo usuário: 
    """
    chat = model.start_chat(history=[{"role": "user", "parts": [prompt]}])

    @api_view_recipes.doc()
    def post(self, form: RecipeForm):
        return self.chat.send_message(form.ingredientes).text


app.register_api_view(api_view_testing)
app.register_api_view(api_view_recipes)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
