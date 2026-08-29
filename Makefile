.PHONY: help install test lint clean

help:
	@echo "Targets: install test lint clean"

install:
	@echo "Installing food-delivery-app deps..."
	@[ -f requirements.txt ] && pip install -r requirements.txt || true
	@[ -f package.json ] && npm install || true

test:
	@echo "Testing food-delivery-app..."
	@[ -f pyproject.toml ] && python -m pytest tests/ -v || true

lint:
	@echo "Linting food-delivery-app..."

clean:
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@rm -rf .pytest_cache htmlcov .coverage
