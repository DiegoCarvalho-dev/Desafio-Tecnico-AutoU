const form = document.getElementById("request-form");
const textBtn = document.getElementById("text-btn");
const fileBtn = document.getElementById("file-btn");
const textField = document.getElementById("text-field");
const fileField = document.getElementById("file-field");
const textarea = document.getElementById("message");
const charCount = document.getElementById("char-count");
const fileInput = document.getElementById("file");
const fileLabel = document.getElementById("file-label");
const fileName = document.getElementById("file-name");
const removeFileBtn = document.getElementById("remove-file");
const categorySpan = document.getElementById("category");
const categoryResult = document.getElementById("category-result");
const suggestedResponse = document.getElementById("suggested-response");
const copyBtn = document.getElementById("copy-btn");
const submitBtn = document.querySelector(".submit-btn");
const modal = document.getElementById("message-modal");
const modalText = document.getElementById("modal-text");
const modalClose = document.getElementById("modal-close");

const resultsSection = document.getElementById("results");

textBtn.addEventListener("click", () => {
    textBtn.classList.add("active");
    fileBtn.classList.remove("active");

    textField.classList.remove("hidden");
    fileField.classList.add("hidden");
});

fileBtn.addEventListener("click", () => {
    fileBtn.classList.add("active");
    textBtn.classList.remove("active");

    fileField.classList.remove("hidden");
    textField.classList.add("hidden");
});

textarea.addEventListener("input", () => {
    charCount.textContent = textarea.value.length;
});

fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
        fileLabel.textContent = "Arquivo selecionado";
        fileLabel.classList.add("selected");
        fileName.textContent = fileInput.files[0].name;
        removeFileBtn.classList.remove("hidden");
    }
});

removeFileBtn.addEventListener("click", () => {
    fileInput.value = "";
    fileLabel.textContent = "Selecionar Arquivo";
    fileLabel.classList.remove("selected");
    fileName.textContent = "Nenhum arquivo selecionado";
    removeFileBtn.classList.add("hidden");
});

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    limparResultado();
    submitBtn.classList.add("loading");

    let textoEmail = "";

    /* Texto direto */
    if (textBtn.classList.contains("active")) {
        textoEmail = textarea.value.trim();

        if (!textoEmail) {
            mostrarModal("Digite o conteúdo do e-mail para análise.");
            finalizarLoading();
            return;
        }
    }

    if (fileBtn.classList.contains("active")) {
        if (!fileInput.files.length) {
            mostrarModal("Selecione um arquivo para análise.");
            finalizarLoading();
            return;
        }

        const file = fileInput.files[0];

        if (!file.name.endsWith(".txt")) {
            mostrarModal("No momento, apenas arquivos .txt são suportados.");
            finalizarLoading();
            return;
        }

        textoEmail = await file.text();
    }

    if (textoEmail.length < 10) {
        mostrarModal("O conteúdo do e-mail é muito curto para análise.");
        finalizarLoading();
        return;
    }

    try {
        const response = await fetch(`${CONFIG.API_BASE_URL}/email/analisar`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ texto: textoEmail })
        });

        if (!response.ok) {
            const erro = await response.json();
            throw new Error(erro.detail || "Erro ao processar a solicitação.");
        }

        const data = await response.json();

        resultsSection.scrollIntoView({ behavior: "smooth" });

        categorySpan.textContent = data.categoria;
        suggestedResponse.textContent = data.resposta_sugerida;
        copyBtn.disabled = false;

        const categoria = data.categoria.toLowerCase().trim();

        if (categoria === "produtivo") {
            categoryResult.classList.add("produtivo");
            mostrarFeedback("E-mail classificado como produtivo.", "success");
        } else if (categoria === "improdutivo") {
            categoryResult.classList.add("improdutivo");
            mostrarFeedback("E-mail classificado como improdutivo.", "warning");
        } else {
            mostrarFeedback("Categoria não reconhecida.", "error");
        }

    } catch (error) {
        mostrarFeedback(error.message || "Erro ao se comunicar com a API.", "error");
    } finally {
        finalizarLoading();
    }
});

copyBtn.addEventListener("click", () => {
    navigator.clipboard.writeText(suggestedResponse.textContent);
    mostrarModal("Resposta copiada com sucesso!");
});

function mostrarModal(mensagem) {
    modalText.textContent = mensagem;
    modal.classList.remove("hidden");
}

modalClose.addEventListener("click", () => {
    modal.classList.add("hidden");
});

function finalizarLoading() {
    submitBtn.classList.remove("loading");
}

function limparResultado() {
    categorySpan.textContent = "Analisando...";
    categoryResult.className = "category-result";
    suggestedResponse.textContent = "Processando resposta...";
    copyBtn.disabled = true;
}

function mostrarFeedback(texto, tipo) {
    const feedback = document.createElement("div");
    feedback.className = `feedback ${tipo}`;
    feedback.textContent = texto;

    resultsSection.prepend(feedback);

    setTimeout(() => feedback.remove(), 4000);
}
