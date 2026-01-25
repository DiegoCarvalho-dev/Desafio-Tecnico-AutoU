from backend.servicos.email_service import analisar_email


def test_email_improdutivo():
    texto = "Muito obrigado pelo retorno!"
    categoria, resposta = analisar_email(texto)

    assert categoria == "Improdutiva"
    assert "Agradecemos" in resposta


def test_email_produtivo():
    texto = "Gostaria de saber mais informações sobre o serviço"
    categoria, resposta = analisar_email(texto)

    assert categoria == "Produtivo"
    assert "aguardo" in resposta.lower()
