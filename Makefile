.PHONY: install install-dev test test-cov lint format clean train evaluate api \
        docker-build docker-build-dev docker-run docker-run-dev docker-run-prod \
        docker-stop docker-logs docker-clean download-data docs docs-build docs-all \
        docs-serve docs-clean docs-api docs-openapi

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

test:
	pytest tests/ -v

test-cov:
	pytest tests/ --cov=ml --cov=api --cov-report=html

lint:
	flake8 ml api tests
	mypy ml api

format:
	black ml api tests

clean:
	find . -type d -name __pycache__ -delete
	find . -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage

train:
	python scripts/train_model.py

evaluate:
	python scripts/evaluate_model.py

api:
	uvicorn api.main:app --reload

# Docker commands
docker-build:
	docker build -f docker/Dockerfile -t phishing-detector:latest .

docker-build-dev:
	docker build -f docker/Dockerfile.dev -t phishing-detector:dev .

docker-run:
	docker-compose -f docker/docker-compose.yml up

docker-run-dev:
	docker-compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml up

docker-run-prod:
	docker-compose -f docker/docker-compose.yml -f docker/docker-compose.prod.yml up -d

docker-stop:
	docker-compose -f docker/docker-compose.yml down

docker-logs:
	docker-compose -f docker/docker-compose.yml logs -f

docker-clean:
	docker-compose -f docker/docker-compose.yml down -v
	docker system prune -f

download-data:
	python scripts/download_datasets.py

# Documentation commands
docs:
	cd docs && make html

docs-build:
	python scripts/generate_docs.py --format html

docs-all:
	python scripts/generate_docs.py --format all --validate --readme

docs-serve:
	cd docs && make serve

docs-clean:
	cd docs && make clean

docs-api:
	cd docs && make api-docs

docs-openapi:
	python scripts/generate_openapi_docs.py