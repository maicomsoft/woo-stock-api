from fastapi import FastAPI

app = FastAPI()

@app.get("/estoque")
def get_estoque():
    # Aqui você pode pegar os dados do estoque de onde quiser, por exemplo, Google Sheets ou banco de dados
    return {"estoque": "dados de estoque aqui"}

