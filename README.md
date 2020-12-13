Chess Pieces
================================================

Chess pieces é uma API onde é possível fazer um CRUD de peças de xadrez.


Além do CRUD, é possível fornecer uma posição do tabuleiro em [notação algébrica](https://en.wikipedia.org/wiki/Algebraic_notation_(chess))
junto com o ID de uma das peças existentes, **se a peça for um cavalo** ela fornecerá todos os movimentos possíveis para os próximos 2 turnos.

Índice
------

- [Pré-requisitos: Ambiente](#pré-requisitos-ambiente)
- [Pré-requisitos: Database](#pré-requisitos-database)
- [Testes Automatizados](#testes-automatizados)
- [Testes Manuais: EndPoints](#testes-manuais-endpoints)

---


Pré-requisitos: Ambiente
--------------

1. Clone o repositório

2. Crie um ambiente virtual com o virtualenv

* Instale
```bash
   [sudo] pip install virtualenv
```

* Após instalar, crie o seu ambiente virtual:
```bash
   virtualenv <nome_do_seu_ambiente>
```

* Ative o seu ambiente:
```bash
   source <nome_do_seu_ambiente>/bin/activate
```

* Se preferir, para usar o virtualenv com uma versão diferente do python
```bash
    virtualenv --python=usr/python3.6/nome_env
```
3. Instale os requirements de desenvolvimento ou os requirements apenas para execução:
```bash
   pip install -r requirements/dev.txt
```

Pré-requisitos: Database
--------------

1. Instale o docker

```bash
   sudo apt install docker
```

2. Instale o docker compose

```bash
   sudo apt install docker-compose
```

3. [Recomendado] Após a instalação do docker é interessante fornecer a permissão de super usuário, caso contrário você terá que usar "sudo" sempre que precisar usar qualquer comando do docker

```bash
   sudo groupadd docker
   sudo gpasswd -a $USER docker
```
> Será necessário fazer log out and log back

4. Diga ao compose para usar o arquivo desenvolvimento.yml

```bash
   docker-compose -f desenvolvimento.yml up -d
```

5. Pode ser necessário reiniciar o docker compose

```bash
   docker-compose -f desenvolvimento.yml restart -t 1
```

6. Execute as migrations

```bash
   src/python manage.py migrate
```

Testes Automatizados
--------------

1. Para executar os testes:

``` bash
    src/pytest
```

Testes Manuais: EndPoints
--------------

1. Suba o servidor local:

```bash
   src/python manage.py runserver
```

2. Para criar uma nova peça:

``` bash
   curl -X POST -d 'name={nome da peça}' -d 'color={cor da peça}' 'http://127.0.0.1:8000/'
```

3. Buscar uma peça por nome e cor:

``` bash
   curl "http://127.0.0.1:8000/?name={nome da peça}&color={cor da peça}"
```

4. Listar os movimentos possíveis de um cavalo para os próximos 2 turnos:


``` bash
   curl "http://127.0.0.1:8000/moves/?cell={celula em notação algebrica}&piece_id={id do cavalo}"
```


###### Demais Endpoints:

- Listar todas as peças existentes:

``` bash
   curl 'http://127.0.0.1:8000/'
```

- Buscar uma peça por ID:

``` bash
   curl 'http://127.0.0.1:8000/{id}/'
```

- Editar uma peça:

``` bash
   curl -X PUT -d 'name={novo nome}' -d 'color={nova cor}' 'http://127.0.0.1:8000/{id}/'
```

- Apagar um contato:

``` bash
   curl -X DELETE 'http://127.0.0.1:8000/{id}/'
```
