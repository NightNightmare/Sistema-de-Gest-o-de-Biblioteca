from typing import List
from app.biblioteca.models import Autor
from app.biblioteca.schemas import AutorIn, Autor_Pydantic
from fastapi.exceptions import HTTPException

async def create_autor(autor: AutorIn) -> Autor_Pydantic:
    autor_obj = await Autor.create(nome=autor.nome)
    return await Autor_Pydantic.from_tortoise_orm(autor_obj)


async def get_autor()-> List[Autor_Pydantic]:
    return await Autor_Pydantic.from_queryset(Autor.all()) 

async def get_autor_by_id(id: int) -> Autor_Pydantic:
    if not (autor := await Autor.get_or_none(id=id)):
        raise HTTPException(status_code=404, detail="autor não encontrado!")
    return await Autor_Pydantic.from_queryset_single(Autor.get(id=id))

async def update_autor(id: int, autor: AutorIn) -> Autor_Pydantic:
    await Autor.filter(id=id).update(**autor.dict(exclude_unset=True)) 
    return await Autor_Pydantic.from_queryset_single(Autor.get(id=id))

async def delete_autor(id: int) -> dict:
    deleted_autor = await Autor.filter(id=id).delete()
    if not deleted_autor:
        raise HTTPException(status_code=404, detail="Autor não encontrado!")
    return {"message": f"Autor com ID {id} removido com sucesso!"}


from app.biblioteca.models import Livro
from app.biblioteca.schemas import LivroIn, Livro_Pydantic

async def create_livro(livro_in: LivroIn) -> Livro_Pydantic:
    autor = await Autor.get_or_none(id=livro_in.autor_id)
    if autor is None:
        raise HTTPException(status_code=404, detail="Autor não encontrado!")
    livro_obj = await Livro.create(autor=autor, **livro_in.dict(exclude={"autor_id"}) )
    return await Livro_Pydantic.from_tortoise_orm(livro_obj)

async def get_livro() -> List[Livro_Pydantic]:
    return await Livro_Pydantic.from_queryset(Livro.all())  

async def get_livro_by_id(id: int) -> Livro_Pydantic:
    if not (livro := await Livro.get_or_none(id=id)):
        raise HTTPException(status_code=404, detail="livro não encontrado!")
    return await Livro_Pydantic.from_queryset_single(Livro.get(id=id))

async def update_livro(id: int, livro: LivroIn) -> Livro_Pydantic:
    await Livro.filter(id=id).update(**livro.dict(exclude_unset=True)) 
    return await Livro_Pydantic.from_queryset_single(Livro.get(id=id))

async def delete_livro(id: int) -> dict:
    deleted_livro = await Livro.filter(id=id).delete()
    if not deleted_livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado!")
    return {"message": f"Livro com ID {id} removido com sucesso!"}