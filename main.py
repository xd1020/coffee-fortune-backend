from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Coffee Fortune API is running ☕"}
