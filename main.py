# Importando o FastAPI
from fastapi import FastAPI
import mysql.connector
from decouple import config
import sys

# Conectando com o Banco de dados SQL
try:
    connection = mysql.connector.connect(
        host=config('host'),
        database=config('database'),
        user=config('user'),
        password=config('password')
    )
    cursor = connection.cursor()
    cursor.execute('''
SELECT 
resultado, COUNT(resultado)
FROM
score
GROUP BY resultado;
''')
    result = cursor.fetchall()
    result = dict(result)
except Exception as e:
    print(e)
    sys.exit()


# Criando uma instância para o FastAPI
app = FastAPI()


# Criando o decorator de rota do operator get
@app.get('/all')
def score_geral():  # Função da rota
    return result


@app.get('/green')
def score_green():
    return {'greens': result['GREEN'] + result['GREEN GALE 1'] + result['GREEN GALE 2']}


@app.get('/red')
def score_red():
    return {'reds': result['RED']}
