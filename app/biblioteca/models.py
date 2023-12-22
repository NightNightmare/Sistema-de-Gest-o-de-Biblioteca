from tortoise import fields, models

class Autor(models.Model):
    id = fields.IntField(pk=True)
    nome = fields.CharField(max_length=255)
    livros: fields.ReverseRelation["Livro"]

class Livro(models.Model):
    id = fields.IntField(pk=True)
    titulo = fields.CharField(max_length=255)
    autor = fields.ForeignKeyField("models.Autor", related_name="livros")
    ano_publicacao = fields.IntField()
    isbn = fields.CharField(max_length=17, unique=True)
    disponibilidade = fields.BooleanField(default=True)

