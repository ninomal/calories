from pydantic import BaseModel

class ComidaRequest(BaseModel):
    nome_comida: str

# (Opcional) Podemos tipar a resposta também para gerar documentação melhor
class ComidaResponse(BaseModel):
    alimento: str
    porcao_ref: str
    calorias: int | float
    proteinas_g: int | float
    carboidratos_g: int | float
    gorduras_g: int | float
    resumo: str