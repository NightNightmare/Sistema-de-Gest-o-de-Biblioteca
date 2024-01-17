from typing import List

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from app.biblioteca.crud import create_autor, get_autor, get_autor_by_id, update_autor, delete_autor
from app.biblioteca.schemas import AutorIn, Autor_Pydantic
from app.biblioteca.models import Autor

autor_endpoint = APIRouter()
livro_endpoint = APIRouter()

@autor_endpoint.post("", response_model=Autor_Pydantic)
async def create_autores(AutorIn: AutorIn):
    return await create_autor(AutorIn)

@autor_endpoint.get("", response_model=List[Autor_Pydantic])
async def get_autores():
    return await get_autor()

@autor_endpoint.get("/{id}", response_model=Autor_Pydantic)
async def get_autores_by_id(id: int):
    return await get_autor_by_id(id)

@autor_endpoint.put("/{id}", response_model=Autor_Pydantic)
async def update_autores(id: int, AutorIn: AutorIn):
    return await update_autor(id, AutorIn)

@autor_endpoint.delete("/{id}")
async def delete_autores(id: int):
    return await delete_autor(id)


from app.biblioteca.crud import create_livro, get_livro, get_livro_by_id, update_livro, delete_livro
from app.biblioteca.schemas import LivroIn, Livro_Pydantic

@livro_endpoint.post("", response_model=Livro_Pydantic)
async def create_livros(LivroIn: LivroIn):
    return await create_livro(LivroIn)

@livro_endpoint.get("", response_model=List[Livro_Pydantic])
async def get_livros():
    return await get_livro()

@livro_endpoint.get("/{id}", response_model=Livro_Pydantic)
async def get_livros_by_id(id: int):
    return await get_livro_by_id(id)

@livro_endpoint.put("/{id}", response_model=Livro_Pydantic)
async def update_livros(id: int, LivroIn: LivroIn):
    return await update_livro(id, LivroIn)

@livro_endpoint.delete("/{id}")
async def delete_livros(id: int):

    return await delete_livro(id)
