.PHONY: install
install:
	@echo "Installing dependencies..."
	poetry install

.PHONY: run-server
run-server:
	@echo "Running server..."
	poetry run python -m portfolio_backend.manage runserver

.PHONY: migrate
migrate:
	@echo "Migrating..."
	poetry run python -m portfolio_backend.manage migrate

.PHONY: migrations
migrations:
	@echo "Making migrations..."
	poetry run python -m portfolio_backend.manage makemigrations

.PHONY: superuser
superuser:
	@echo "Creating super user..."
	poetry run python -m portfolio_backend.manage createsuperuser

.PHONY: update
update: install migrations migrate ;
	



