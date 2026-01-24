from fastapi import FastAPI
from backend.api.rotas_email import router as rotas_email

app = FastAPI(
    title="API de Análise de Emails",
    description="API para classificar emails e sugerir respostas",
    version="1.0.0"
)

app.include_router(rotas_email)


@app.get("/")
def root():
    return {"status": "API rodando com sucesso 🚀"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
