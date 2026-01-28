# 📧 Classificador Inteligente de E-mails – AutoU

Este projeto é um sistema completo de **análise e classificação automática de e-mails**, desenvolvido como projeto técnico, integrando **Front-end**, **Back-end** e **Inteligência Artificial** para classificar mensagens em categorias **Produtivo** ou **Improdutivo**, além de sugerir respostas automáticas coerentes com o conteúdo analisado.

---

## 🚀 Funcionalidades

- 📌 Classificação automática de e-mails em:
  - **Produtivo** (exige ação ou resposta)
  - **Improdutivo** (não exige ação imediata)
- 🤖 Integração com IA para análise de texto
- ✉️ Geração de **resposta sugerida automática**
- 📝 Entrada de dados via:
  - Texto digitado
  - Upload de arquivo `.txt`
- 🎨 Interface moderna, responsiva e intuitiva
- 🟢 Feedback visual claro para cada classificação
- 🔁 Respostas variáveis da IA (não repetitivas)

---

## 🧠 Como funciona

1. O usuário insere o conteúdo do e-mail (texto ou arquivo).
2. O Front-end envia os dados para a API.
3. O Back-end processa o conteúdo e envia para a IA.
4. A IA analisa o contexto da mensagem.
5. O sistema retorna:
   - Categoria do e-mail
   - Resposta sugerida
6. O Front-end exibe o resultado com feedback visual adequado.

---

## 🛠️ Tecnologias Utilizadas

### Front-end
- HTML5
- CSS3
- JavaScript (Vanilla)

### Back-end
- Python
- FastAPI

### Inteligência Artificial
- Modelo de linguagem para análise semântica e contextual

---

## 📂 Estrutura do Projeto
```bash
/frontend
├── index.html
├── style.css
├── script.js
└── config.js

/backend
├── main.py
├── routes
├── services
└── requirements.txt
```
---
## ⚙️ Configuração do Ambiente

### Front-end
O arquivo `config.js` detecta automaticamente o ambiente:

```js
const CONFIG = {
  API_BASE_URL: window.location.hostname === "localhost"
    ? "http://127.0.0.1:8000"
    : "URL_DA_API_EM_PRODUCAO"
};
```
### Back-end

### Instale as dependências:
```bash 
pip install -r requirements.txt
```

### Execute o servidor:
```bash 
uvicorn main:app --reload
```

## 🧪 Testes

- Testes realizados com mensagens curtas, longas, formais e informais

- Validação de categorias e respostas

- Testes de integração Front-end ↔ Back-end ↔ IA

  ## 👨‍💻 Autor

**Desenvolvido por Diego Ricardo Carvalho**

Projeto **técnico focado em integração com IA e sistemas web modernos**.
