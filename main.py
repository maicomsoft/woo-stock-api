from fastapi import FastAPI
from sync import sync_estoque

app = FastAPI()

@app.get("/estoque")
def atualizar_estoque():
    sync_estoque()
    return {"status": "ok", "mensagem": "Estoque atualizado no WooCommerce"}
