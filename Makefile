.PHONY: run
run:
	export FLASK_APP=app.main
	export FLASK_ENV=development
	poetry python app/app.py

.PHONY: test
test:
	poetry run pytest

.PHONY: testcov
testcov:
	poetry run pytest --cov=app --cov-report=html --cov-report=term

.PHONY: lint
lint:
	poetry run flake8 .

.PHONY: clean
clean:
	find . -type d -name __pycache__ | xargs rm -rf {}
	rm -rf htmlcov
	rm -rf .pytest_cache
	rm .coverage
