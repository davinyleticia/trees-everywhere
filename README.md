# Trees Everywhere - Teste YouShop


## API 

Obter token

```bash
curl --request POST \
  --url http://127.0.0.1:8000/api/login/ \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/8.4.5' \
  --data '{
	"username": "root",
	"password": "132"
}'
```

A lista

```bash
curl --request GET \
  --url http://127.0.0.1:8000/api/planted-trees/ \
  --header 'Authorization: Token 558c78dedd0e32b3ef2018160e8b652e91448138' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/8.4.5'
```

---


## Instalação

### Desenvolvimento

Usa o servidor de desenvolvimento Django padrão.

1. Renomeie *.env.dev-sample* para *.env.dev*.
1. Atualize as variáveis ​​de ambiente nos arquivos *docker-compose.yml* e *.env.dev*.
1. Construa as imagens e execute os contêineres:

    ```sh
    $ docker-compose up -d --build
    ```

    Teste em [http://localhost:8000](http://localhost:8000). A pasta "app" é montada no contêiner e as alterações no código são aplicadas automaticamente.


Código para fazer um migrate no banco de dados:

```bash
sudo docker-compose run web /usr/src/app/manage.py migrate
```
Código para criar um super usuário:

```bash
sudo docker-compose run web /usr/src/app/manage.py createsuperuser
```

### Produção

Usa gunicorn + nginx.

1. Renomeie *.env.prod-sample* para *.env.prod* e *.env.prod.db-sample* para *.env.prod.db*. Atualize as variáveis ​​de ambiente.
1. Construa as imagens e execute os contêineres:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Teste em [http://localhost:1337](http://localhost:1337). Nenhuma pasta montada. Para aplicar alterações, a imagem deve ser reconstruída.