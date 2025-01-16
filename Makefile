install:
	@echo "Installing dependencies..."
	poetry install

run-server:
	@echo "Running server..."
	poetry run python -m portfolio-backend.manage runserver

migrate:
	@echo "Migrating..."
	poetry run python -m portfolio-backend.manage migrate

migrations:
	@echo "Making migrations..."
	poetry run python -m portfolio-backend.manage makemigrations

super-user:
	@echo "Creating super user..."
	poetry run python -m portfolio-backend.manage createsuperuser

update: install migrations migrate ;
	



