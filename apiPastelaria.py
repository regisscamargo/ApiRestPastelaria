from flask import Flask
from flask_restful import Api

#Import das classes
from FuncionarioDAO import Funcionario

app = Flask(__name__)
api = Api(app)

# mapeamento dos endpoints
api.add_resource(Funcionario, "/funcionario/<int:id>", endpoint = 'funcionario')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)