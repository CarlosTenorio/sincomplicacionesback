collectstatic:
	docker-compose run --rm gulp
	docker-compose run --rm web collectstatic --noinput
	docker-compose run --rm web compress
makemigrations:
	docker-compose run --rm --service-ports web makemigrations
migrate:
	docker-compose run --rm --service-ports web migrate
create-superuser:
	docker-compose run --rm --service-ports web createsuperuser
devel:
	docker-compose run --rm --service-ports dev
rebuild-web:
	docker-compose up --build web
rebuild-dev:
	docker-compose up --build dev
rebuild-gunicorn:
	docker-compose up --build gunicorn

# Deployment
check-deploy:
	docker-compose run --rm --service-ports web check --deploy
deploy:
	docker-compose run -d --rm --service-ports nginx

# DB
connect-db:
	docker exec -i -t web_db_1 /bin/bash
connect-gunicorn:
	docker exec -i -t web_gunicorn_1 /bin/bash
connect-dev:
	docker exec -i -t web_dev_run_1 /bin/bash

# Load
load-db-devel:
	docker-compose run --rm --service-ports web load_db_devel
load-category:
	docker-compose run --rm --service-ports web load_category
load-city:
	docker-compose run --rm --service-ports web load_city
load-province:
	docker-compose run --rm --service-ports web load_province
load-country:
	docker-compose run --rm --service-ports web load_country

# Delete
delete-category:
	docker-compose run --rm --service-ports web delete_category
delete-city:
	docker-compose run --rm --service-ports web delete_city
delete-province:
	docker-compose run --rm --service-ports web delete_province

stop-rm:
	cd tasks && \
	./stop-rm-Dockers.sh
