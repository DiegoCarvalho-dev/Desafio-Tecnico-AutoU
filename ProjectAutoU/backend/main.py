from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.rotas_email import router as rotas_email

app = FastAPI(
    title = "Classificador de Emails com IA",
    description="API para classificar emails como produtivos ou improdutivos e sugerir respostas automáticas",
    version = "1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rotas_email)
