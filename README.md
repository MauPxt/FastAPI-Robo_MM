# FastAPI-Robô_MM

Criando uma API utilizando o framework FastAPI no Python. Essa API faz requisições em um banco de dados e retorna informações sobre o robô mm blaze.

## Feito com:

 <p align="left">
 <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
 <a href="https://fastapi.tiangolo.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/fastapi.svg" alt="FastAPI" width="40" height="40"/> </a>
</p>

## Requisitos:

Python

FastAPI

MySql

# Instruções de instalação:

```sh
1 - Realize o download dos arquivos. Você pode fazer isso da seguinte forma:
    1.1 - Baixar esse repositório em formato .zip e por fim extrair os arquivos para uma pasta de sua preferência.
    1.2 - Clonar esse repositório através do git com o seguinte comando: "$ git clone https://github.com/MauPxt/FastAPI-Aprendendo".
2 - Utilizar o comando "$ pip install -r requirements.txt"
3 - Criar/Usar um banco de dados no MySQL para fazer a conexão de requisição
4 - Alterar o código de modo que combine com a query do seu banco de dados
5 - Python-Decouple - Criar um arquivo com nome ".env" e colocar dados no padrão do mysql connector "host, database, user, password"
6 - Iniciar o uvicorn inserindo o comando no terminal "$ uvicorn main:app --reload":
7 - Com o servidor local criado, já é possível utilizar a API
```

# Instruções de uso:

Após a instalação e execução do código, para utilizar a API faça as seguintes requisições

- Acesse o link http://127.0.0.1:8000/score/all para obter todos os resultados
- Acesse o link http://127.0.0.1:8000/score/greens para obter os resultados de green
- Acesse o link http://127.0.0.1:8000/score/reds para obter os resultados de red

<br>

Extra:

- Acesse o link http://127.0.0.1:8000/score/docs para acessar a documentação
- Acesse o link http://127.0.0.1:8000/score/redoc para acessar outro tipo de documentação
