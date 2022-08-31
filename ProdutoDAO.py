from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Funcionario(BaseModel):
    nome: str
    descricao: str
    foto: int
    valor_unitario: int
    

# Criar os endpoints de produto: GET, POST, PUT, DELETE

@router.get("/produto/{id}", tags=["produto"])
def get_produto(id: int):
    return {"msg": "get executado"}, 200

@router.post("/produto/{id}", tags=["produto"])
def post_produto(id: int):
    return {"msg": "post executado"}, 200

@router.put("/produto/{id}", tags=["produto"])
def put_produto(id: int):
    return {"msg": "put executado"}, 201

@router.delete("/produto/{id}", tags=["produto"])
def delete_produto(id: int):
    return {"msg": "delete executado"}, 201