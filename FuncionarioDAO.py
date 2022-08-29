from flask_restful import Resource

# Criar os endpoints de Funcionario: GET, POST, PUT, DELETE
class Funcionario(Resource):
    def get(self, id):
        return {"msg": "get executado"}, 200
    def post(self, id):
        return {"msg": "post executado"}, 201
    def put(self, id):
        return {"msg": "put executado"}, 201
    def delete(self, id):
        return {"msg": "delete executado"}, 201