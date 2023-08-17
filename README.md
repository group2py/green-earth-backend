# Projeto: Aplicação para ONGs ambientais.

# Como começar a contribuir?

#### Materiais de apoio:

https://opensource.guide/pt/how-to-contribute/#como-submeter-uma-contribui%C3%A7%C3%A3o

https://docs.github.com/pt/get-started/quickstart/contributing-to-projects

### Configurando seu ambiente de desenvolvimento

    Fork este repositório (Clique no botão Fork no canto superior direito desta página)


### backend
``git clone git@github.com:group2py/green-earth-frontend.git``

``cd green-earth-backend``

`` git checkout -b nome_da_nova_branch ``

``python -m venv .venv``

 #### linux
 
 ``cp contrib/env-sample .env``
    
``source .venv/bin/activate``

#### windows

`` você deve copiar o arquivo env-sample e colar na raiz do projeto com o nome de .env ``

``.venv\Scripts\Activate ``

#### Instalando dependências

`` pip install -r requirements-dev.txt``

#### aplicando migrações e rodando projeto

``python manage.py makemigrations``

``python manage.py migrate``

``python manage.py runserver``


#### Faça suas mudanças
Commit e push

    git add .
    git commit -m 'Commit message'
    git push origin branch-name

cria um pull request seu repositório forkado (Clica no botão New Pull Request localizado no topo do seu repositório)

espere seu PR review e merge serem aprovados!

### E o mais importante: Divirta-se

