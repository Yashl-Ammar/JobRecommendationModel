run:
	docker run -p 5000:5000 flask-app

stop:
	docker stop $(docker ps -aq --filter ancestor=flask-app)

clean:
	docker system prune --force

install:
	pip install -r requirements.txt

test:
	python -m pytest test.py

build:
	docker build -t flask-app .
