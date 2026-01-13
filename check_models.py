import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega a chave
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

print("--- PESQUISANDO MODELOS DISPONÍVEIS NA SUA CONTA ---")

try:
    # Lista todos os modelos
    for m in genai.list_models():
        # Filtra apenas os que geram texto (ignora os de apenas imagem/embedding)
        if 'generateContent' in m.supported_generation_methods:
            print(f"Nome: {m.name}")
            
except Exception as e:
    print(f"Erro ao listar: {e}")