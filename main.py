# Importando o FastAPI
from fastapi import FastAPI

# Criando uma instância para o FastAPI
app = FastAPI()

# Criando o decorator de rota do operator get


@app.get('/')
def hello_root():  # Função da rota
    return {'message': 'hello world'}
