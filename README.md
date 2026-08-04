

# DevShop API



A learning project: REST API for an online course shop.

## Stack
- Python
- FastAPI
- Pydantic
- PostgreSQL
- psycopg2

## Files
- `devshop_courses.py` — CRUD with in-memory data
- `devshop_db.py` — CRUD with PostgreSQL
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


