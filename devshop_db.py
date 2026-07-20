
from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title = "DevShop DB")

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "learning"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT", "5432"),
      
    )
    
# @app.get("/courses")
# def get_courses():
#     conn = get_db_connection() 
#     cur=conn.cursor(cursor_factory=RealDictCursor)
#     cur.execute("SELECT  id, name, price, active FROM courses")
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return rows

@app.get("/courses")
def get_courses(max_price: int = None, active: bool = None):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    query = "SELECT id, name, price, active FROM courses WHERE 1=1"
    params = []
    
    if max_price is not None:
        query += " AND price <= %s"
        params.append(max_price)
        
    if active is not None:
        query += " AND active = %s"
        params.append(active)
        
    cur.execute(query,tuple(params))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
    


@app.get("/courses/{courses_id}")  
def get_courses_id(courses_id: int):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
        "SELECT id, name, price, active FROM courses WHERE id = %s",
        (courses_id,)
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row is None:
        return{"Error": "Not Found"}
    return row
    
    
    
    
class Course(BaseModel):
    name: str
    price: int
    active: bool
@app.post("/courses")
def create_course(course: Course):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute (
    "INSERT INTO courses (name,price,active) VALUES (%s, %s, %s) RETURNING id, name, price, active",
    (course.name, course.price, course.active)
    
    )
    new_course = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return new_course

    
    
@app.delete("/courses/{courses_id}")
def  delete_course(courses_id: int):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
        "DELETE FROM courses WHERE id = %s RETURNING id",
        (courses_id,),
    )
    deleted = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if deleted is None:
        return {"Error": "Not Found"}
    return {"message": deleted}




@app.put("/courses/{courses_id}")
def update_course(courses_id: int, update: Course):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
        """UPDATE courses
        SET name = %s, price = %s, active = %s
        WHERE id = %s
        RETURNING id, name, price, active """,
        (update.name, update.price, update.active, courses_id),
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if row is None:
        return{"Error": "Not found"}
    return row

    
    
