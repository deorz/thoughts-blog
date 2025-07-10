run:
	test -f .env || cp .env.example .env
	docker compose -f deploy/docker-compose.yml up --build -d

build:
	docker compose -f deploy/docker-compose.yml up --build backend --force-recreate backend -d

down:
	docker compose -f deploy/docker-compose.yml down -v

logs:
	docker compose -f deploy/docker-compose.yml logs -f backend

lint:
	uv run ruff check .

typecheck:
	uv run ty check .

test:
	uv run pytest tests/ -vv
