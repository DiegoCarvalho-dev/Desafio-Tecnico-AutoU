from servicos.classificador_ia import classificar_email


def analisar_email(texto: str) -> dict:
    """
    Orquestra a análise do e-mail:
    - Classifica o e-mail
    - Retorna resultado padronizado para a API
    """

    resultado_classificacao = classificar_email(texto)

    return {
        "categoria": resultado_classificacao["categoria"],
        "motivo": resultado_classificacao["motivo"]
    }
