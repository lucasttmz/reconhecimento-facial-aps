.PHONY: run

run:
	fastapi dev sistema_escolar/main.py

lint:
	ruff format
	ruff check --fix

format:
	ruff format

initdb:
	sqlite3 sistema_escolar/dal/db/aps.db < sistema_escolar/dal/db/init.sql
