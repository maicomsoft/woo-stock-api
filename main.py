from fastapi import FastAPI
from sync import sync_estoque

app = FastAPI()

@app.get("/estoque")
def atualizar_estoque():
    estoque = sync_estoque()  # agora a função deve retornar os dados de estoque
    return {
        "status": "ok",
        "mensagem": "Estoque atualizado no WooCommerce",
        "estoque": estoque
    }
