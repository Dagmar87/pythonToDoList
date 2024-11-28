# pythonToDoList
## Desenvolvimento de um Microserviço de To-Do List
- Desafio Técnico: Desenvolvimento de um Microserviço de To-Do List
- Empresa: Montseguro
- Vaga: Desenvolvedor Back End Phyton Pleno
- Nome: José Dagmar Florentino da Silva Sobrinho

## Descrição

Esse projeto consiste na criação de um microserviço para gerenciar uma lista de tarefas (to-do list), com as operações CRUD (Create, Read, Update, Delete) e alguns requisitos adicionais, utilizando a linguagem Python com o framework FastAPI.

## Linguagens e Tecnologias utilizadas

- Python
- HTML
- CSS
- Banco de Dados SQLite
- IDE VSCode 
- Bibliotecas Python (fastapi, uvicorn, jinja2, python-multipart, sqlalchemy)
- Docker

## Instruções para rodar o projeto

1. git clone https://github.com/Dagmar87/pythonToDoList.git
2. cd pythonToDoList
3. virtualenv venv (Criar o ambiente de trabalho Python)
4. venv\Scripts\activate (Ativar o ambiente)
5. pip install fastapi uvicorn jinja2 python-multipart sqlalchemy || pip install -r requirements.txt (Instalar as bibliotecas python do projeto)
6. uvicorn app:app --reload (Rodar o projeto)
7. Acessar o seguinte enderenço: http://127.0.0.1:8000/tasks/

+ Obs: python3 -m pip install --upgrade pip (Atualizar Pip, se for necessario)
+ Obs2: pip install virtualenv (Windows) || sudo pip install virtualenv (Linux) ==> (Caso não tenha o ambiente de trabalho Python instalado no computador)

## Instruções para rodar o projeto com Docker

1. git clone https://github.com/Dagmar87/pythonToDoList.git
2. cd pythonToDoList
3. virtualenv venv (Criar o ambiente de trabalho Python)
4. venv\Scripts\activate (Ativar o ambiente)
5. docker build -t pythonToDoList .
6. docker run --name pythonToDoList-container -p 80:80 pythonToDoList
7. docker run -d --name pythonToDoList-container -p 80:80 pythonToDoList
8. Acessar o seguinte enderenço: http://127.0.0.1:8000/tasks/

+ Obs: python3 -m pip install --upgrade pip (Atualizar Pip, se for necessario)
+ Obs2: pip install virtualenv (Windows) || sudo pip install virtualenv (Linux) ==> (Caso não tenha o ambiente de trabalho Python instalado no computador)
