### async api service
build_async_api:
	-docker network create videoserv_net
	-docker-compose -f cd docker-compose.stor.yml build
	-docker-compose build
	-docker-compose -f cd docker-compose.test.yml build

start_async_api:
# start Elasticsearch and Redis
	docker-compose -f docker-compose.stor.yml up -d 

# load data from dump for testing (take some time)
	docker-compose -f docker-compose.dump.yml run --rm load_elastic_dump

# start Async API service
	docker-compose up -d

stop_async_api:
	docker-compose -f docker-compose.stor.yml down
	docker-compose down

start_test_async_api:
	docker-compose -f docker-compose.test.yml up

stop_test_async_api:
	docker-compose -f docker-compose.test.yml down
