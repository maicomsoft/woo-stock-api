from fastapi import FastAPI
from sync import sync_estoque

app = FastAPI()

@app.get("/estoque")
def atualizar_estoque():
    resultado = sync_estoque()
    return {"status": "ok", "dados": resultado}
