from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.rotas_email import router as rotas_email
from backend.routes.rotas_teste import router as rotas_teste
import os

app = FastAPI(
    title="API de Análise de Emails",
    description="API para classificar emails e sugerir respostas usando IA",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rotas_email)
app.include_router(rotas_teste)

@app.get("/")
def root():
    return {
        "app": "Classificador de Emails IA",
        "version": "1.0.0",
        "status": "online",
        "autor": "Seu Nome",
        "rotas_disponiveis": {
            "GET /": "Esta página",
            "GET /health": "Verificar saúde da API",
            "GET /teste": "Teste simples (COM 'E' NO FINAL)",
            "GET /teste-ia": "Teste com email produtivo",
            "GET /teste-ia-improdutivo": "Teste com email improdutivo",
            "POST /email/analisar": "Analisar email customizado"
        }
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "email-classifier"}

@app.get("/teste")
def teste_simples():
    return {"mensagem": "API está funcionando!", "teste": "ok", "rota": "/teste"}

if __name__ == "__main__":
    import uvicorn
    print("=" * 60)
    print(" CLASSIFICADOR DE EMAILS - SERVIDOR PRINCIPAL")
    print("=" * 60)
    print(" URLs para teste (COPIE E COLE NO NAVEGADOR):")
    print("   1. http://localhost:8000/")
    print("   2. http://localhost:8000/teste")
    print("   3. http://localhost:8000/teste-ia")
    print("   4. http://localhost:8000/teste-ia-improdutivo")
    print("   5. http://localhost:8000/health")
    print("=" * 60)
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
