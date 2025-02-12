from fastapi import FastAPI,Depends
import mysql.connector
from pydantic import BaseModel
import openai
from database import engine, SessionLocal, init_db, Supplier, Product
from sqlalchemy.orm import Session

app = FastAPI()

init_db()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Sample route to fetch suppliers
@app.get("/suppliers/")
def get_suppliers(db: Session = Depends(get_db)):
    return db.query(Supplier).all()

# Sample route to fetch products
@app.get("/products/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
# OpenAI API
openai.api_key = "your-api-key"

class QueryRequest(BaseModel):
    query: str


@app.post("/query/")
async def chatbot_query(request: QueryRequest):
    user_query = request.query.lower()
    
    if "brand" in user_query:
        brand = user_query.split("brand")[-1].strip()
        results = get_products(brand)
    else:
        results = "Query not recognized."

    return {"response": results}
