from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Libera acesso para qualquer origem (Google Sheets, por exemplo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/estoque")
def get_estoque():
    # Aqui você pode colar sua lógica real do sync.py
    return {
        "SKU123": {"foz": 10, "sp": 4},
        "SKU456": {"foz": 0, "sp": 9}
    }
