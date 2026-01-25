from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/email", tags=["Email"])


class EmailRequest(BaseModel):
    texto: str


class EmailResponse(BaseModel):
    categoria: str
    resposta_sugerida: str


@router.post("/analisar", response_model=EmailResponse)
def analisar_email(dados: EmailRequest):
    texto = dados.texto.lower()

    if any(palavra in texto for palavra in ["solicito", "problema", "erro", "status", "suporte"]):
        categoria = "Produtivo"
        resposta = "Recebemos sua solicitação e ela será analisada em breve."
    else:
        categoria = "Improdutivo"
        resposta = "Agradecemos sua mensagem!"

    return {
        "categoria": categoria,
        "resposta_sugerida": resposta
    }
