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
@app.get('/score/{tipo}')  # Entrada dinâmica
def score_geral(tipo: str):  # Função da rota com validação
    tipo = str.upper(tipo)
    if tipo == 'ALL':
        return result
    elif tipo == 'GREENS':
        return {'greens': result['GREEN'] + result['GREEN GALE 1'] + result['GREEN GALE 2']}
    elif tipo == 'REDS':
        return {'reds': result['RED']}
    else:
        return {'Error': "Tipo inválido! Tente 'all', 'greens' ou 'reds'"}
