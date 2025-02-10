.PHONY: install
install:
	@echo "Installing dependencies..."
	poetry install


.PHONY: install-pre-commit
install-pre-commit:
	@echo "Installing pre-commit..."
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	@echo "Linting..."
	poetry run pre-commit run --all-files

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

.PHONY: up-dependencies-only
up-dependencies-only:
	test -f .env || touch .env
	docker compose -f docker-compose.dev.yml up --force-recreate db

.PHONY: update
update: install migrations migrate install-pre-commit;
