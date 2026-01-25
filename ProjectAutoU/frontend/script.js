const form = document.getElementById("request-form");

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const mensagem = document.getElementById("mensagem").value;

    const dados = {
        email: email,
        mensagem: mensagem
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/send-email", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(dados)
        });

        if (!response.ok) {
            throw new Error("Erro ao enviar solicitação");
        }

        const resultado = await response.json();
        alert(resultado.message || "Solicitação enviada com sucesso!");

        form.reset();
    } catch (error) {
        alert("Erro na comunicação com o servidor.");
        console.error(error);
    }
});
