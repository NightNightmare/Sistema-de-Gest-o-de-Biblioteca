from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from app.biblioteca.models import Livro, Autor

class AutorIn(BaseModel):
    nome: str

class LivroIn(BaseModel):
    titulo: str
    autor_id: int
    ano_publicacao: int
    isbn: str
    disponibilidade: bool

Livro_Pydantic = pydantic_model_creator(Livro, name="Livro")
Autor_Pydantic = pydantic_model_creator(Autor, name="Autor", exclude=("livros",))