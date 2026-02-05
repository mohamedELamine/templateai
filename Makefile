.PHONY: help setup up down logs clean test health build push

help:
	@echo "TemplateAI Development System - Available Commands"
	@echo ""
	@echo "Setup & Installation:"
	@echo "  make setup          - Setup project (copy .env, build images)"
	@echo "  make build          - Build Docker images"
	@echo ""
	@echo "Running Services:"
	@echo "  make up             - Start services (development)"
	@echo "  make up-prod        - Start services (production)"
	@echo "  make down           - Stop services"
	@echo "  make restart        - Restart services"
	@echo ""
	@echo "Monitoring:"
	@echo "  make logs           - View service logs"
	@echo "  make health         - Check service health"
	@echo "  make ps             - Show running containers"
	@echo ""
	@echo "Development:"
	@echo "  make test           - Run tests"
	@echo "  make lint           - Run linter"
	@echo "  make clean          - Clean up containers and volumes"
	@echo ""
	@echo "Database:"
	@echo "  make db-backup      - Backup database"
	@echo "  make db-restore     - Restore database from backup"
	@echo "  make db-reset       - Reset database (WARNING: destructive)"
	@echo ""

setup:
	@echo "Setting up TemplateAI..."
	@cp .env.example .env || true
	@mkdir -p data/templates data/logs data/backups config/ssl
	@make build
	@echo "✓ Setup complete!"

build:
	@echo "Building Docker images..."
	docker-compose build

up:
	@echo "Starting services (development mode)..."
	docker-compose up -d
	@echo "✓ Services started!"
	@echo ""
	@make health

up-prod:
	@echo "Starting services (production mode)..."
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
	@echo "✓ Production services started!"
	@echo ""
	@make health

down:
	@echo "Stopping services..."
	docker-compose down
	@echo "✓ Services stopped!"

restart:
	@echo "Restarting services..."
	docker-compose restart
	@echo "✓ Services restarted!"

logs:
	docker-compose logs -f

ps:
	docker-compose ps

health:
	@echo "Checking service health..."
	@bash scripts/health-check.sh

test:
	@echo "Running tests..."
	docker-compose exec api-gateway pytest /app/tests
	@echo "✓ Tests complete!"

lint:
	@echo "Running linter..."
	docker-compose exec api-gateway flake8 /app --max-line-length=120
	docker-compose exec langgraph-orchestrator flake8 /app --max-line-length=120

clean:
	@echo "Cleaning up..."
	docker-compose down -v
	rm -rf data/logs/*
	rm -rf .pytest_cache
	rm -rf __pycache__
	find . -name "*.pyc" -delete
	@echo "✓ Cleanup complete!"

db-backup:
	@echo "Creating database backup..."
	@bash scripts/backup.sh
	@echo "✓ Backup complete!"

db-reset:
	@echo "WARNING: This will delete all data!"
	@read -p "Type 'yes' to continue: " confirm && [ "$$confirm" = "yes" ] && \
	docker-compose down -v && \
	docker-compose up -d && \
	echo "✓ Database reset complete!" || echo "Cancelled"

push:
	@echo "Pushing to GitHub..."
	git add .
	git commit -m "Update: TemplateAI improvements"
	git push origin main
	@echo "✓ Pushed to GitHub!"

