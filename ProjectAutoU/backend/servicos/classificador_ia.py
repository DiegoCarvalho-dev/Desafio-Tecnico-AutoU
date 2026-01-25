def classificar_email(texto: str) -> dict:
    """
    Recebe o texto do e-mail e retorna:
    {
        "categoria": "produtivo" | "improdutivo",
        "motivo": "string curta"
    }
    """

    prompt = f"""
Você é um classificador profissional de e-mails corporativos.

Classifique o e-mail APENAS em:
- "produtivo": quando o e-mail exige ação, resposta, análise, solução de problema, solicitação, dúvida, reclamação ou pedido.
- "improdutivo": quando o e-mail é apenas agradecimento, saudação, elogio, confirmação simples ou mensagem sem necessidade de ação.

Regras obrigatórias:
- Mensagens que contenham apenas agradecimentos ou cumprimentos são SEMPRE improdutivas.
- Mensagens que pedem qualquer ação, informação ou resposta são SEMPRE produtivas.
- Seja rigoroso. Não tente ser gentil, seja objetivo.

Texto do e-mail:
\"\"\"{texto}\"\"\"

Responda EXCLUSIVAMENTE no formato JSON abaixo, sem texto adicional:

{{
  "categoria": "produtivo ou improdutivo",
  "motivo": "explique em uma frase curta"
}}
"""

    #  Placeholder temporário (simulação)
    texto_lower = texto.lower()

    if any(palavra in texto_lower for palavra in ["obrigado", "agradeço", "agradecimento"]):
        return {
            "categoria": "improdutivo",
            "motivo": "Mensagem contém apenas agradecimento"
        }

    return {
        "categoria": "produtivo",
        "motivo": "Mensagem solicita ação ou resposta"
    }

