from fastapi.testclient import TestClient
from src.main import app

# Cria um "cliente falso" que vai simular acessos ao nosso app
client = TestClient(app)

def test_deve_analisar_uma_banana():
    # 1. PREPARAR (Arrange)
    payload = {
        "nome_comida": "Banana Prata"
    }

    # 2. AGIR (Act)
    # Simula um POST na rota /analisar-alimento
    response = client.post("/analisar-alimento", json=payload)


   
    
    # Verifica se o servidor respondeu "OK" (código 200)
    assert response.status_code == 200, "O servidor deveria retornar código 200"

     # 3. VERIFICAR (Assert)
    if response.status_code != 200:
        print(f"\nERRO FATAL NO SERVIDOR: {response.text}")

    # Pega os dados que voltaram
    dados = response.json()

    # Verifica se os campos existem no JSON
    assert "calorias" in dados
    assert "proteinas_g" in dados
    
    # Verifica se o Gemini entendeu que é uma banana (pode variar o texto, checamos se contém 'Banana')
    assert "Banana" in dados["alimento"] or "banana" in dados["alimento"]
    
    # Imprime no terminal para a gente ver (opcional)
    print(f"\nRetorno da API: {dados}")

def test_deve_tratar_comida_inexistente():
    payload = {"nome_comida": "XyzWk99 Nao Existe"}
    response = client.post("/analisar-alimento", json=payload)
    
    assert response.status_code == 200
    dados = response.json()
    
    # Lembra que instruímos o prompt a devolver zerado se não existir?
    assert dados["calorias"] == 0