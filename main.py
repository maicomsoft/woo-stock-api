<<<<<<< HEAD
from fastapi import FastAPI
from sync import sync_estoque

app = FastAPI()

@app.get("/estoque")
def atualizar_estoque():
    resultado = sync_estoque()
    return {"status": "ok", "dados": resultado}
=======
from fastapi import FastAPI
from sync import sync_estoque

app = FastAPI()

@app.get("/estoque")
def atualizar_estoque():
    sync_estoque()
    return {"status": "ok", "mensagem": "Estoque atualizado no WooCommerce"}
>>>>>>> be237b2 (Adiciona arquivos da API: sync, bling, woocommerce)
