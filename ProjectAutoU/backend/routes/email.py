from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from servicos.email_service import analisar_email

router = APIRouter()


class EmailRequest(BaseModel):
    texto: str


@router.post("/email/analisar")
def analisar(request: EmailRequest):
    try:
        resultado = analisar_email(request.texto)
        return resultado
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Erro ao analisar o e-mail"
        )
