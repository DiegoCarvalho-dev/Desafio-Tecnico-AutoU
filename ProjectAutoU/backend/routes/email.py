from fastapi import APIRouter
from pydantic import BaseModel

from backend.servicos.email_service import analisar_email

router = APIRouter(prefix="/email", tags=["Email"])


class EmailEntrada(BaseModel):
    texto: str


class EmailResposta(BaseModel):
    categoria: str
    resposta_sugerida: str


@router.post("/analisar", response_model=EmailResposta)
def analisar(email: EmailEntrada):
    categoria, resposta = analisar_email(email.texto)

    return {
        "categoria": categoria,
        "resposta_sugerida": resposta
    }
