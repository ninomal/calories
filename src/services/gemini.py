import json
import google.generativeai as genai
from src.config import GEMINI_API_KEY

class GeminiService:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def analisar_calorias(self, nome_comida: str):
        print(f"Service: Analisando '{nome_comida}'...")

        prompt = f"""
        Aja como um nutricionista técnico.
        Analise o alimento: "{nome_comida}".
        
        Retorne APENAS um objeto JSON (sem aspas de markdown ```json ... ```) com as informações nutricionais estimadas para uma porção média comum ou 100g.
        
        O formato do JSON deve ser estritamente este:
        {{
            "alimento": "nome formatado",
            "porcao_ref": "ex: 100g ou 1 unidade",
            "calorias": 0,
            "proteinas_g": 0.0,
            "carboidratos_g": 0.0,
            "gorduras_g": 0.0,
            "resumo": "Uma breve frase sobre se é saudável ou não."
        }}
        Se o alimento não existir ou for inválido, retorne o JSON com valores zerados e resumo "Alimento não identificado".
        """

        try:
            response = self.model.generate_content(prompt)
            
            # Limpeza do texto cru
            texto_limpo = response.text.replace("```json", "").replace("```", "").strip()
            
            # Converte para dict
            return json.loads(texto_limpo)

        except Exception as e:
            print(f"Erro no Gemini Service: {e}")
            # Em caso de erro, retornamos um dict vazio ou lançamos o erro para o controller tratar
            raise e