

# DevShop API



A learning project: REST API for an online course shop.

## Stack
- Python
- FastAPI
- Pydantic
- PostgreSQL
- psycopg2

## Files
- `devshop_db.py` — main app (health check, includes routers)
- `database.py` — PostgreSQL connection
- `routers/courses.py` — course endpoints (APIRouter)
- `devshop_courses.py` — CRUD with in-memory data
- `course_example.json` — example JSON body for POST 


## Setup
1. Install dependencies:
'''pip install -r requirements.txt'''
2. Copy `.env.example` to `.env` and set your database password.
3. Create the `courses` table in PostgreSQL (see SQL in project notes or docs).

## Run
In-memory version:
'''uvicorn devshop_courses:app --reload'''




Database version:
uvicorn devshop_db:app --reload --port 8001


Open Swagger UI: http://127.0.0.1:8000/docs (or :8001 for DB version)

## Docker (PostgreSQL only)

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Copy `.env.example` to `.env` and set `DB_PASSWORD` (same values for API and Docker)
3. Start PostgreSQL: `docker compose up -d`
4. Create the `courses` table if needed, then run the API: `uvicorn devshop_db:app --reload --port 8001`

Passwords stay in `.env` (not committed to GitHub).

## Endpoints
- GET /health - API health check
- GET /courses — list courses
  - Filters: `max_price`, `active` (optional)
  - Pagination: `limit` (max rows), `offset` (skip rows; used together with `limit`)
  - Example: `/courses?limit=2&offset=0` — first 2 courses

- GET /courses/{id} — one course
- POST /courses — create course
- PUT /courses/{id} — update course
- DELETE /courses/{id} — delete course
- Missing course returns **404** (HTTPException)


