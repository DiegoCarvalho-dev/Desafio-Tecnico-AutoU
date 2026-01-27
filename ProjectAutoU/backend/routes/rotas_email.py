from fastapi import APIRouter, Body
from backend.servicos.ai_service import analisar_email_com_ia

router = APIRouter(prefix="/email", tags=["Email"])

@router.post("/analisar")
def analisar_email(payload: dict = Body(...)):
    texto = payload.get("texto")

    if not texto:
        return {"error": "Campo 'texto' é obrigatório"}

    resultado = analisar_email_com_ia(texto)
    return resultado
