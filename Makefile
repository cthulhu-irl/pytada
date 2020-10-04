all: lint build install test

lint:
	flake8 tada/

build:
	pip3 install --user -r requirements.txt
	pip3 install --user pytest # dev

install: build
	python3 ./setup.py install --force --user

test: install
	pytest tests/

clean:
	rm -f .coverage
	rm -rf .*-cache/
	rm -rf build/ dist/ tada.egg-info/
