import FuncionarioDAO
import ClienteDAO
import ProdutoDAO
from fastapi import FastAPI

app = FastAPI()

app.include_router(FuncionarioDAO.router)
app.include_router(ClienteDAO.router)
app.include_router(ProdutoDAO.router)