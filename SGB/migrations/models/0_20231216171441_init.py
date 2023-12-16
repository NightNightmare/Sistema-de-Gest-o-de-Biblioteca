from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "livro" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "titulo" VARCHAR(100) NOT NULL,
    "autor" VARCHAR(100) NOT NULL,
    "anode_publicacao" INT NOT NULL,
    "isbn" VARCHAR(13) NOT NULL UNIQUE,
    "disponibilidade" BOOL NOT NULL  DEFAULT True
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
