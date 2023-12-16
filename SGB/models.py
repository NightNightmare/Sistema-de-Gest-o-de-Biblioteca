from tortoise import fields 
from tortoise.models import Model

class Livro(Model):
    id = fields.IntField(pk=True)
    titulo = fields.CharField(max_length=100)
    autor = fields.CharField(max_length=100)
    anode_publicacao = fields.IntField()
    isbn = fields.CharField(max_length=13, unique=True)
    disponibilidade = fields.BooleanField(default=True)

    #def __str__(self):
     #   return self.titulo