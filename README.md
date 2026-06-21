# Bookstore API

Este é o projeto Bookstore API desenvolvido em Django Rest Framework (DRF) para o curso da EBAC. O projeto inclui funcionalidades de gerenciamento de produtos, categorias e pedidos (orders).

---

## 🚀 Como Configurar e Rodar o Projeto

### Pré-requisitos
Certifique-se de ter instalado em sua máquina:
1. **Python 3.12** ou superior.
2. **Poetry** (Gerenciador de dependências e ambientes virtuais para Python).

---

## 🛠️ Passo a Passo de Instalação

### 1. Clonar o Repositório e Acessar a Pasta
```bash
git clone https://github.com/jpnune/exercicio-bookstore.git
cd exercicio-bookstore
```

### 2. Instalar o Poetry (Caso não possua)
Caso você ainda não tenha o Poetry instalado, execute o comando abaixo no PowerShell (Windows):
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```
*(Para Linux/macOS, use: `curl -sSL https://install.python-poetry.org | python3 -`)*

### 3. Instalar Dependências do Projeto
Na raiz do projeto (onde está o arquivo `pyproject.toml`), execute:
```bash
poetry install --no-root
```

### 4. Rodar as Migrações do Banco de Dados
```bash
poetry run python manage.py migrate
```

### 5. Iniciar o Servidor de Desenvolvimento
```bash
poetry run python manage.py runserver
```
A API estará disponível em `http://127.0.0.1:8000/`.

---

## 🧪 Como Executar os Testes

### Rodar Todos os Testes com o Pytest
Para rodar a suíte completa de testes:
```bash
poetry run pytest
```

### Rodar Apenas os Testes Natividade Django
```bash
poetry run python manage.py test
```

---

## 📊 Estrutura de Testes Criada

Abaixo está o mapeamento dos novos arquivos de testes unitários integrados ao projeto:

| Tipo | Aplicativo (App) | Arquivo | O que valida |
| :--- | :--- | :--- | :--- |
| **Modelo** | `product` | [test_category_model.py](file:///c:/Users/jpnun/Desktop/ebac/product/tests/test_models/test_category_model.py) | Criação e atributos da categoria. |
| **Modelo** | `product` | [test_product_model.py](file:///c:/Users/jpnun/Desktop/ebac/product/tests/test_models/test_product_model.py) | Criação, preços e relacionamentos de produtos. |
| **Modelo** | `order` | [test_order_model.py](file:///c:/Users/jpnun/Desktop/ebac/order/test/test_models/test_order_model.py) | Relacionamento de pedido com usuários e produtos. |
| **Serializer** | `product` | [test_category_serializer.py](file:///c:/Users/jpnun/Desktop/ebac/product/tests/test_serializers/test_category_serializer.py) | Validação e campos de dados do serializer de Category. |
| **Serializer** | `product` | [test_product_serializer.py](file:///c:/Users/jpnun/Desktop/ebac/product/tests/test_serializers/test_product_serializer.py) | Criação de produto através de IDs das categorias associadas. |
| **Serializer** | `order` | [test_order_serializer.py](file:///c:/Users/jpnun/Desktop/ebac/order/test/test_serializers/test_order_serializer.py) | Cálculo correto do total do pedido e amarração de chaves. |
