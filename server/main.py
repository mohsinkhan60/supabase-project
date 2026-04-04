from fastapi import FastAPI
from decouple import config

url = config('SUPABASE_URL')
key = config('SUPABASE_KEY')
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"} 