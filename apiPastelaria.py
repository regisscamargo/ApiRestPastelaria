from fastapi import FastAPI

import db
# import das classes de modelo de persistência
from mod_funcionario.FuncionarioModel import FuncionarioDB
from mod_cliente.ClienteModel import ClienteDB
from mod_produto.ProdutoDAO import ProdutoDB

# import das classes com as rotas/endpoints
from mod_funcionario import FuncionarioDAO
from mod_cliente import ClienteDAO
from mod_produto import ProdutoDAO


app = FastAPI()

# mapeamento das rotas/endpoints
app.include_router(FuncionarioDAO.router)
app.include_router(ClienteDAO.router)
app.include_router(ProdutoDAO.router)

# cria, caso não existam, as tabelas de todos os modelos importados

db.criaTabelas()