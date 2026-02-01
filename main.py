import os
import base64
from fastapi import FastAPI, File, UploadFile, HTTPException
from openai import OpenAI

# FastAPI app
app = FastAPI()

# OpenAI client (API key Render env'den gelir)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@app.get("/")
def root():
    return {"status": "Coffee Fortune API is running ☕"}


@app.post("/fortune")
async def fortune(file: UploadFile = File(...)):
    try:
        # 1️⃣ Fotoğrafı byte olarak oku
        image_bytes = await file.read()

        # 2️⃣ Base64'e çevir
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        # 3️⃣ Fal prompt'u
        prompt = """
Sen deneyimli bir Türk kahvesi falcısısın.

Kurallar:
- Türkçe yaz
- Pozitif ve umut verici ol
- Aşk, para, yol ve haber konularına değin
- Geleceğe dair tahminlerde bulun
- Tavsiye ver
- Kültürel fal dili kullan
- Kısa ama etkileyici olsun

Kahve fincanını dikkatle incele ve fal yorumunu yap.
"""

        # 4️⃣ OpenAI Vision çağrısı
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": prompt},
                        {
                            "type": "input_image",
                            "image_base64": image_base64
                        }
                    ],
                }
            ],
            max_output_tokens=300,
        )

        # 5️⃣ AI cevabını al
        fortune_text = response.output_text

        return {
            "fortune": fortune_text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
