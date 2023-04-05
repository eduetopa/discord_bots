MAKEFLAGS += --silent
run:
	python3 ./src/main.py 

install:
	pipenv shell 
	pipenv install