from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # <--- IMPORTANTE
from src.schemas import ComidaRequest, ComidaResponse
from src.services.gemini import GeminiService

app = FastAPI(title="CaloriesIA API - Modular")

# --- BLOCO NOVO: CONFIGURAÇÃO DO CORS ---
# Isso permite que o React (localhost:5173) converse com o Python
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ----------------------------------------

service = GeminiService()

@app.post("/analisar-alimento", response_model=ComidaResponse)
async def analisar_alimento(request: ComidaRequest):
    try:
        resultado = service.analisar_calorias(request.nome_comida)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))