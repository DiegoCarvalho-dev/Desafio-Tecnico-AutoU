from transformers import pipeline
import re

classificador = pipeline(
    "text-classification",
    model="nlptown/bert-base-multilingual-uncased-sentiment",
    device=-1
)

PALAVRAS_IMPRODUTIVAS = [
    "obrigado", "obrigada", "agradeço", "parabéns", "feliz",
    "bom dia", "boa tarde", "boa noite", "cumprimentos",
    "boas festas", "natal", "ano novo"
]

PALAVRAS_PRODUTIVAS = [
    "urgente", "erro", "problema", "ajuda", "suporte",
    "falha", "bug", "prazo", "solicito", "necessito",
    "resolver", "corrigir", "análise", "relatório"
]


def analisar_email_com_ia(texto: str) -> dict:
    texto_lower = texto.lower()

    if any(p in texto_lower for p in PALAVRAS_IMPRODUTIVAS):
        categoria = "Improdutivo"
        resposta = "Agradecemos seu contato! Sua mensagem foi recebida com apreço."
        return _retorno(categoria, resposta, "Regra de palavras-chave")

    if any(p in texto_lower for p in PALAVRAS_PRODUTIVAS):
        categoria = "Produtivo"
        resposta = gerar_resposta_produtiva(texto_lower)
        return _retorno(categoria, resposta, "Regra de palavras-chave")

    resultado = classificador(texto[:500])[0]
    rating = int(resultado["label"][0])
    score = resultado["score"]

    categoria = "Produtivo" if rating >= 4 else "Improdutivo"
    resposta = (
        "Recebemos sua solicitação e retornaremos em breve."
        if categoria == "Produtivo"
        else "Agradecemos seu contato."
    )

    return {
        "categoria": categoria,
        "resposta_sugerida": resposta,
        "confianca": f"{score:.2%}",
        "rating_original": resultado["label"]
    }


def gerar_resposta_produtiva(texto: str) -> str:
    if "erro" in texto or "bug" in texto:
        return "Registramos seu problema técnico. Nossa equipe de suporte entrará em contato."
    if "urgente" in texto:
        return "Sua solicitação foi marcada como urgente. Retornaremos o quanto antes."
    return "Recebemos sua solicitação. Nossa equipe analisará e retornará em breve."


def _retorno(categoria, resposta, origem):
    return {
        "categoria": categoria,
        "resposta_sugerida": resposta,
        "confianca": "Alta",
        "rating_original": origem
    }
