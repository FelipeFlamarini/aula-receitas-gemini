from pydantic import BaseModel, Field


class RecipeForm(BaseModel):
    ingredientes: str = Field(
        ...,
        description="Os ingredientes que você pretende usar",
    )
