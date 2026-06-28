# Bookstore

Bookstore APP from Backend Python course from EBAC

## Prerequisites

* Python 3.9>
* Poetry
* Docker && docker-compose

---

## Quickstart

### 1. Clone this project

```bash
git clone https://github.com/jpnune/exercicio-bookstore.git
```

### 2. Install dependencies:

```bash
cd exercicio-bookstore
poetry install
```

### 3. Run local dev server:

```bash
poetry run python manage.py migrate
poetry run python manage.py runserver
```

### 4. Run docker dev server environment:

```bash
docker-compose up -d --build
docker-compose exec web python manage.py migrate
```

### 5. Run tests inside of docker:

```bash
docker-compose exec web python manage.py test
```

---

## 🧪 Como Executar os Testes Localmente

### Rodar todos os testes com Pytest
```bash
poetry run pytest
```

### Rodar testes nativos do Django
```bash
poetry run python manage.py test
```

---

## 🔒 Autenticação

A rota de pedidos (`OrderViewSet`) requer autenticação. As rotas de produtos e categorias são públicas.

### Gerando Token para Usuário:
```bash
poetry run python manage.py drf_create_token <username>
```

### Cabeçalho de Autenticação (Headers):
* **Key:** `Authorization`
* **Value:** `Token <seu_token_gerado>`
