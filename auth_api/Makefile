### auth service
start_auth_api:
# standard Flask app
	docker-compose up --build -d

start_auth_api_gevent:
# gevent-based Flask app
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build

stop_auth_api:
	docker-compose down -v

stop_auth_api_gevent:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml down

test_auth_api:
# running tests against the standard Flask app
	docker-compose --profile=testing up --build -d

test_auth_api_gevent:
# running tests against gevent-based Flask app
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml --profile=testing up --build -d

stop_test_auth_api:
	docker-compose --profile=testing down

stop_test_auth_api_gevent:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml --profile=testing down
