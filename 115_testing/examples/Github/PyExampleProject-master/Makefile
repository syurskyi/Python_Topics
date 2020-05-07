all: clean lint test

req:
	pip install -r requirements.txt

test:
	py.test

lint:
	pylint helloworld -r n

cov: coverage
coverage:
	coverage erase
	coverage run --source helloworld -m pytest
	coverage report

clean:
	find . -name \*.pyc -o -name \*.pyo -o -name __pycache__ -exec rm -rf {} +

