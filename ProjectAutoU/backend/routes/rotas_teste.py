from fastapi import APIRouter

router = APIRouter()

@router.get("/teste-ia")
def teste_ia_produtivo():
    return {
        "categoria": "Produtivo",
        "resposta_sugerida": "Obrigado pelo contato, vamos analisar sua solicitação e responder em breve."
    }

@router.get("/teste-ia-improdutivo")
def teste_ia_improdutivo():
    return {
        "categoria": "Improdutivo",
        "resposta_sugerida": "Obrigado pela mensagem."
    }
