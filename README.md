# Trees Everywhere - Teste YouShop


## Instalação

Usa o servidor de desenvolvimento Django padrão.

1. Renomeie *.env.dev-sample* para *.env.dev*.
2. Atualize as variáveis ​​de ambiente nos arquivos *docker-compose.yml* e *.env.dev*.
3. Construa as imagens e execute os contêineres:

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


## web
Para rodar via web:


[http://localhost:8000](http://localhost:8000)


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
  --header 'Authorization: Token {token}' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/8.4.5'
```
feito por Daviny Letícia