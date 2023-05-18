# Authentication service
The following services are used: FastAPI, Nginx, Postgres, ElasticSearch, Kibana, Redis

## Example
- Login: http://localhost:8000/api/v1/oauth/login/yandex (no account, will fail)
- Signup: http://localhost:8000/api/v1/oauth/signup/yandex (will create account)
- Login again: http://localhost:8000/api/v1/oauth/login/yandex (will succeed)
- Use JaegerUI (in testing profile) and @trac decorator for tracing

## How to deploy
> 0. Fill in `.env`
> 1. `cd async_api/`
> 2. `make build_async_api`
> 3. `make start_async_api`
> 4. `cd ../auth_api/`
> 5. `make start_auth_api`
> 6. For stopping: </br>
        in `auth_api` folder - `make stop_auth_api`, </br>
        in `async_api` folder - `make stop_async_api`
> 7. Tests are also available from makefile in each folder