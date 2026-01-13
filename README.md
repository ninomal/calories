# 🍎 CaloriesIA - Backend

API de inteligência artificial capaz de identificar alimentos e estimar suas informações nutricionais (Calorias, Proteínas, Carboidratos e Gorduras) utilizando o modelo **Gemini 2.5 Flash** do Google.

Projeto desenvolvido em Python com FastAPI, seguindo arquitetura modular.

## 🚀 Tecnologias

- [Python 3.12+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) (Framework Web)
- [Google Generative AI](https://ai.google.dev/) (Inteligência Artificial)
- [Pytest](https://docs.pytest.org/) (Testes Automatizados)

## 📦 Como rodar o projeto

### 1. Clone o repositório
```bash
git clone [https://github.com/SEU_USUARIO/caloriesIa.git](https://github.com/SEU_USUARIO/caloriesIa.git)
cd caloriesIa

2. Crie e ative o Ambiente Virtual
Windows:

Bash

python -m venv venv
.\venv\Scripts\activate
Linux/Mac:

Bash

python3 -m venv venv
source venv/bin/activate
3. Instale as dependências
Bash

pip install -r requirements.txt
4. 🔑 Configuração da API Key (Importante)
Para que a IA funcione, você precisa de uma chave gratuita do Google.

Acesse o Google AI Studio.

Faça login e clique em "Get API key".

Clique em "Create API key" e copie o código.

Na raiz do projeto, renomeie o arquivo .env.example para .env (ou crie um novo).

Cole sua chave dentro dele assim:

Ini, TOML

GEMINI_API_KEY=Cole_Sua_Chave_Aqui
5. Execute o Servidor
Bash

python app.py
O servidor rodará em: http://localhost:8000 A documentação interativa (Swagger) estará em: http://localhost:8000/docs

🧪 Rodando os Testes
Para garantir que a integração com o Gemini está funcionando e descobrir qual o modelo:

Bash

pytest -v -s

🛠️ Estrutura do Projeto
caloriesIa/
├── app.py              # Launcher do servidor
├── src/
│   ├── main.py         # Rotas e Controller da API
│   ├── config.py       # Configurações de ambiente
│   ├── schemas.py      # Modelos de dados (Input/Output)
│   └── services/
│       └── gemini.py   # Lógica de comunicação com a IA
└── tests/              # Testes automatizados