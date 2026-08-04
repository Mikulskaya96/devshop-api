
from fastapi import FastAPI
from routers.courses import router as courses_router

app = FastAPI(title="Devshop DB")

@app.get("/health") 
def health():
    return {"status": "ok"}

app.include_router(courses_router)
    



    
    
    
    


    
    
