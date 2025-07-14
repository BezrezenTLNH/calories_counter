# 🥦 calories_counter

A simple app for calculating calories (calories, proteins, fats, carbohydrates) with the ability to add products and create recipes.

## 📌 Project Objective

To allow the user to:
- add products with the indication of the KBJU per 100 grams;
- create recipes from these products with weight;
- receive an automatic calculation of the total caloric value of the recipe.

## ⚙️ Technology Stack

**Backend:**
- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy 2.0 (async)](https://docs.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Pydantic v2](https://docs.pydantic.dev/)
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/)

**Frontend (coming later):**
- Vue 3 + TypeScript or React

**Tools:**
- pytest, ruff, mypy, black, isort
- GitHub Actions (CI)
- Prometheus + Grafana (monitoring)

## 🔍 Code Style and Linting

We use the following tools to maintain consistent code style and quality:

| | Tool | Purpose |00 |----------------|----------------------------------|
| **ruff** | Linting (replacing flake8 + pylint) |
| **black** | Autoformatting code |
| **isort** | Arranging imports |
| **mypy** | Type checking |
| **pre-commit** | Autorun linting on commit |

### 🛠️ Manual installation and startup:

```bash
# Install dependencies
poetry install

# Check linters manually
poetry run ruff check .
poetry run black --check .
poetry run isort --check-only .
poetry run mypy app

## 🚀 Quick Start (in development)

> ⚠️ Attention: the project is at an early stage and actively developing.

To run locally (after customization):
```bash
docker-compose up --build
