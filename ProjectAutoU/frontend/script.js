
const form = document.getElementById('request-form');
const textBtn = document.getElementById('text-btn');
const fileBtn = document.getElementById('file-btn');
const textField = document.getElementById('text-field');
const fileField = document.getElementById('file-field');
const messageInput = document.getElementById('message');
const charCount = document.getElementById('char-count');
const fileInput = document.getElementById('file');
const fileLabel = document.getElementById('file-label');
const fileName = document.getElementById('file-name');
const removeFileBtn = document.getElementById('remove-file');
const submitBtn = document.querySelector('.submit-btn');
const btnText = document.getElementById('btn-text');
const btnLoading = document.getElementById('btn-loading');
const results = document.getElementById('results');
const categorySpan = document.getElementById('category');
const categoryBox = document.getElementById('category-result');
const responseText = document.getElementById('suggested-response');
const copyBtn = document.getElementById('copy-btn');
const modal = document.getElementById('message-modal');
const modalText = document.getElementById('modal-text');
const modalClose = document.getElementById('modal-close');

textBtn.addEventListener('click', () => {
    textBtn.classList.add('active');
    fileBtn.classList.remove('active');

    textField.classList.remove('hidden');
    fileField.classList.add('hidden');
});

fileBtn.addEventListener('click', () => {
    fileBtn.classList.add('active');
    textBtn.classList.remove('active');

    fileField.classList.remove('hidden');
    textField.classList.add('hidden');
});

messageInput.addEventListener('input', () => {
    charCount.textContent = messageInput.value.length;
});

fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];

        fileName.textContent = file.name;
        fileLabel.textContent = 'Arquivo Selecionado';
        fileLabel.classList.add('selected');
        removeFileBtn.classList.remove('hidden');
    }
});

removeFileBtn.addEventListener('click', () => {
    fileInput.value = '';
    fileName.textContent = 'Nenhum arquivo selecionado';
    fileLabel.textContent = 'Selecionar Arquivo';
    fileLabel.classList.remove('selected');
    removeFileBtn.classList.add('hidden');
});

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const isTextMode = textBtn.classList.contains('active');
    const textValue = messageInput.value.trim();
    const fileValue = fileInput.files[0];

    if (isTextMode && !textValue) {
        showModal('Digite o conteúdo do e-mail para análise.');
        return;
    }

    if (!isTextMode && !fileValue) {
        showModal('Selecione um arquivo para análise.');
        return;
    }

    setLoading(true);
    resetResults();

    try {
        const response = await fakeApiRequest();

        renderResults(response);

    } catch (error) {
        showModal('Erro ao processar o e-mail. Tente novamente.');
    } finally {
        setLoading(false);
    }
});

function renderResults(data) {
    results.classList.remove('hidden');

    categorySpan.textContent = data.category;
    responseText.textContent = data.response;

    categoryBox.classList.remove('produtivo', 'improdutivo');
    categoryBox.classList.add(data.category.toLowerCase());

    copyBtn.disabled = false;
}

copyBtn.addEventListener('click', () => {
    const text = responseText.textContent;

    if (!text || text.includes('será gerada')) {
        showModal('Nenhuma resposta disponível para copiar.');
        return;
    }

    navigator.clipboard.writeText(text);
    showModal('Resposta copiada com sucesso!');
});

function setLoading(isLoading) {
    if (isLoading) {
        btnText.classList.add('hidden');
        btnLoading.classList.remove('hidden');
        submitBtn.disabled = true;
    } else {
        btnText.classList.remove('hidden');
        btnLoading.classList.add('hidden');
        submitBtn.disabled = false;
    }
}

function resetResults() {
    categorySpan.textContent = 'Aguardando análise...';
    responseText.textContent = 'A resposta será gerada após a análise.';
    copyBtn.disabled = true;
}

function showModal(message) {
    modalText.textContent = message;
    modal.classList.remove('hidden');
}

modalClose.addEventListener('click', () => {
    modal.classList.add('hidden');
});

function fakeApiRequest() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({
                category: 'Produtivo',
                response: 'Obrigado pelo contato. Sua solicitação foi recebida e será analisada em breve.'
            });
        }, 2000);
    });
}
