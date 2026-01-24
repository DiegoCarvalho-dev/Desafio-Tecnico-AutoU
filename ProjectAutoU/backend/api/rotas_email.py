from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/email",
    tags=["Email"]
)

class EmailEntrada(BaseModel):
    texto: str


class EmailResposta(BaseModel):
    categoria: str
    resposta_sugerida: str


@router.post("/analisar", response_model=EmailResposta)
def analisar_email(email: EmailEntrada):

    if "obrigado" in email.texto.lower() or "feliz" in email.texto.lower():
        categoria = "Improdutivo"
        resposta = "Agradecemos o contato! Desejamos um ótimo dia."
    else:
        categoria = "Produtivo"
        resposta = "Recebemos sua solicitação e em breve retornaremos com mais informações."

    return {
        "categoria": categoria,
        "resposta_sugerida": resposta
    }
