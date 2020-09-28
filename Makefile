all: build install test

build:
	pip3 install --user -r requirements.txt
	pip3 install --user pytest
	python3 ./

install: build
	python3 ./setup.py install --force --user

test: install
	pytest tests/
