import db
from sqlalchemy import Column, VARCHAR, DECIMAL, Integer, BLOB

# ORM
class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'
    id_produto = Column(Integer, primary_key=True,
                        autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    descricao = Column(VARCHAR(200), nullable=False)
    foto = Column(BLOB, nullable=True)
    valor_unitario = Column(VARCHAR(100), nullable=False)


def _init_(self, id_produto, nome, descricao, foto, valor_unitario):
    self.id_produto = id_produto
    self.nome = nome
    self.descricao = descricao
    self.foto = foto
    self.valor_unitario = valor_unitario