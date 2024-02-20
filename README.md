# Projeto de Gerenciamento de Árvores - Teste YouShop

Código para fazer um migrate no banco de dados:

```bash
sudo docker-compose run web /usr/src/app/manage.py migrate
```
Código para criar um super usuário:

```bash
sudo docker-compose run web /usr/src/app/manage.py createsuperuser
```


### Desenvolvimento

Usa o servidor de desenvolvimento Django padrão.

1. Renomeie *.env.dev-sample* para *.env.dev*.
1. Atualize as variáveis ​​de ambiente nos arquivos *docker-compose.yml* e *.env.dev*.
1. Construa as imagens e execute os contêineres:

    ```sh
    $ docker-compose up -d --build
    ```

    Teste em [http://localhost:8000](http://localhost:8000). A pasta "app" é montada no contêiner e as alterações no código são aplicadas automaticamente.

### Produção

Usa gunicorn + nginx.

1. Renomeie *.env.prod-sample* para *.env.prod* e *.env.prod.db-sample* para *.env.prod.db*. Atualize as variáveis ​​de ambiente.
1. Construa as imagens e execute os contêineres:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Teste em [http://localhost:1337](http://localhost:1337). Nenhuma pasta montada. Para aplicar alterações, a imagem deve ser reconstruída.