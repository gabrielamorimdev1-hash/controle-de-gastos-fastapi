# Controle de Gastos API

API simples de controle de gastos criada para praticar desenvolvimento backend com Python e FastAPI.

## Tecnologias

- Python
- FastAPI
- Pydantic
- Pytest
- Git

## Funcionalidades

- Cadastrar gastos
- Listar gastos cadastrados
- Calcular o total de gastos
- Validação de dados com Pydantic
- Testes automatizados com Pytest

## Endpoints

### GET /gastos

Retorna todos os gastos cadastrados.

### POST /gastos

Cadastra um novo gasto.

Exemplo:

```json
{
  "descricao": "Internet",
  "valor": 100.0,
  "categoria": "Casa"
}