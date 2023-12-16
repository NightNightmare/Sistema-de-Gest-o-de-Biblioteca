from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from database import init_db
from models import Livro

app = FastAPI(title='fastapi')
init_db(app)


@app.get("/", response_class=HTMLResponse)
def healthcheck():
    return "<h1> ALL good! </h1>"

class CreateLivroPayload(BaseModel):
    titulo: str
    autor: str
    anode_publicacao: int
    isbn: str
    disponibilidade: bool
    

#@app.get("/livros")

@app.post("/livros")
async def create_livro(payload: CreateLivroPayload):
    livro = await Livro.create(**payload.model_dump())
    return {"message": f"Livro criado com sucesso com o ID {livro.id}"}

#@app.get("/livros")

#@app.put("/livros")

#@app.delete("/livros")

