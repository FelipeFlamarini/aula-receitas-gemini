from pydantic import BaseModel, Field


class TestingPostForm(BaseModel):
    string: str = Field("")


class RecipeForm(BaseModel):
    ingredientes: str = Field(
        ...,
        description="Os ingredientes que você pretende usar",
        examples=[
            "Arroz, frango, batata doce, alface, tomate, azeite, pasta de amendoim"
        ],
    )
