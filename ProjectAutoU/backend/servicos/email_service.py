def analisar_email(texto_email: str):
    texto_email = texto_email.strip().lower()

    if "obrigado" in texto_email or "feliz" in texto_email:
        categoria = "Improdutiva"
        resposta_sugerida = "Agradecemos seu contato! Tenha um ótimo dia!"
    else:
        categoria = "Produtivo"
        resposta_sugerida = "Fique no aguardo. Iremos retornar com mais informações."

    return categoria, resposta_sugerida
