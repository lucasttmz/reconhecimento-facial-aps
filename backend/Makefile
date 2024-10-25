.PHONY: run

run:
	fastapi dev sistema_escolar/main.py

lint:
	ruff format
	ruff check --fix

test:
	pytest -v

test_fast:
	pytest -v -m "no slow"

format:
	ruff format

initdb:
	sqlite3 sistema_escolar/dal/db/aps.db < sistema_escolar/dal/db/init.sql

createdb:
	sqlite3 sistema_escolar/dal/db/aps.db < sistema_escolar/dal/db/schema.sql
