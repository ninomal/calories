import uvicorn
import multiprocessing

# Importa a instância do 'app' que foi criada dentro de src/main.py
from src.main import app

if __name__ == "__main__":
    # Esta linha é essencial para quando criarmos o .exe no Windows
    multiprocessing.freeze_support()
    
    print("Iniciando servidor CaloriesIA...")
    # Rodamos o servidor passando o objeto app diretamente
    uvicorn.run(app, host="127.0.0.1", port=8000)