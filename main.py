from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Coffee Fortune API is running ☕"}

from fastapi import File, UploadFile

@app.post("/fortune")
async def fortune(file: UploadFile = File(...)):
    return {
        "message": "Fotoğraf alındı ☕ Fal yorumuna hazırız!"
    }
    
