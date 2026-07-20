from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title = "DevShop")

courses = [
    {"id": 1, "name": "Python Basics", "price": 99, "active": True},
    {"id": 2, "name": "FastAPI Intro", "price": 149, "active": True},
    {"id": 3, "name": "Old Django", "price": 49, "active": False},
]
"""
@app.get("/courses")
def get_courses():
    return couses 
"""

@app.get("/courses")
def get_courses(max_price: int = None, active: bool = None):
    if max_price is None and active is None:
        return courses
    result = []
    for course in courses:
        if max_price is not None and course["price"] > max_price:
            continue
        if active is not None and course["active"] != active:
            continue
        result.append(course)
    return result


@app.get("/courses/{courses_id}")
def get_courses_id (courses_id: int):
    for course in courses:
        if course["id"] == courses_id:
            return course
    return {"courses": "Not found"}


class Course(BaseModel):
    name: str
    price: int
    active: bool
    
@app.post("/courses")
def create_course(course: Course):#можно назвать не только Course 
    new_course = {
        "id": len(courses) + 1,
        "name": course.name,
        "price": course.price,
        "active": course.active
    }
    courses.append(new_course)
    return new_course

@app.delete("/courses/{courses_id}")
def delete_course(courses_id: int):
    for course in courses:
        if course ["id"] == courses_id:
            courses.remove(course)
            return{"message" :"deleted"}
    return{"error": "Not found"}


@app.put("/courses/{courses_id}")# пометка: класс уже создан он выше,заново писать не нужно 
def update_course(courses_id: int, update: Course):
    for course in courses:
        if course ["id"] == courses_id:
           course["name"] = update.name
           course["price"] = update.price
           course["active"]= update.active
           return course
    return{"Error": "Not Found"}
   



   
    
      
         
         
