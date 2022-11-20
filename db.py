from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

STR_DATABASE = "sqlite:///pastelaria_db.db"

engine = create_engine(STR_DATABASE, future=True)
# , echo=True

Session = sessionmaker(bind=engine, future=True)

# para trabalhar com modelos/tabelas
Base = declarative_base()

# cria, caso não existam, as tabelas de todos os modelos importados
def criaTabelas():
    Base.metadata.create_all(engine)