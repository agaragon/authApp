up:
	docker-compose up --build -d

down:
	docker-compose down --volumes

restart: down up

start-and-test: up
	sleep 10
	python3 request_testing.py
	make down

test:
	python3 request_testing.py

logs:
	docker-compose logs -f --tail=100 blogposts_app_1