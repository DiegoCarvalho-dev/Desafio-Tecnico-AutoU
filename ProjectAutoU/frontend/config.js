const CONFIG = {
    API_BASE_URL:
        window.location.protocol === "file:"
            ? "http://127.0.0.1:8000"
            : window.location.hostname === "localhost"
                ? "http://127.0.0.1:8000"
                : "https://SUA-API-AQUI"
};
