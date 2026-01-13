from fastapi import FastAPI, HTTPException
from src.schemas import ComidaRequest, ComidaResponse
from src.services.gemini import GeminiService

# Criação da aplicação
app = FastAPI(title="CaloriesIA API - Modular")

# Instancia o serviço
service = GeminiService()

@app.post("/analisar-alimento", response_model=ComidaResponse)
async def analisar_alimento(request: ComidaRequest):
    try:
        # O controller apenas repassa o trabalho para o Service
        resultado = service.analisar_calorias(request.nome_comida)
        return resultado
        
    except Exception as e:
        # Se der erro, devolve um erro HTTP 500
        raise HTTPException(status_code=500, detail=str(e))