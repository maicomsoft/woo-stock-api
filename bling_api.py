import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()

class BlingAPI:
    def __init__(self):
        self.client_id = os.getenv("BLING_CLIENT_ID")
        self.client_secret = os.getenv("BLING_CLIENT_SECRET")
        self.refresh_token = os.getenv("BLING_REFRESH_TOKEN")
        self.access_token = os.getenv("BLING_ACCESS_TOKEN")
        self.token_url = "https://www.bling.com.br/Api/v3/oauth/token"
        self.base_url = "https://www.bling.com.br/Api/v3"
        self.deposit_sp = os.getenv("BLING_DEPOSIT_SP")
        self.deposit_foz = os.getenv("BLING_DEPOSIT_FOZ")

    def refresh_access_token(self):
        # Monta o header com client_id e client_secret codificados em Base64
        auth_string = f"{self.client_id}:{self.client_secret}"
        auth_base64 = base64.b64encode(auth_string.encode()).decode()

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {auth_base64}"
        }

        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token
        }

        response = requests.post(self.token_url, headers=headers, data=data)
        response.raise_for_status()

        token_data = response.json()
        self.access_token = token_data["access_token"]

        # Atualiza os tokens no .env
        with open(".env", "r") as f:
            lines = f.readlines()
        with open(".env", "w") as f:
            for line in lines:
                if line.startswith("BLING_ACCESS_TOKEN="):
                    f.write(f"BLING_ACCESS_TOKEN={self.access_token}\n")
                elif line.startswith("BLING_REFRESH_TOKEN="):
                    f.write(f"BLING_REFRESH_TOKEN={token_data['refresh_token']}\n")
                else:
                    f.write(line)

        return self.access_token

    def get_headers(self):
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        # Testa se o token atual é válido com um endpoint que o token tem permissão
        test_response = requests.get(
            f"{self.base_url}/estoques/saldos", 
            headers=headers,
            params={"codigos[]": "MESATD9050BR"}  # SKU de teste
        )

        if test_response.status_code in [401, 403]:
            print("🔄 Token expirado ou sem permissão. Renovando com refresh_token...")
            self.refresh_access_token()
            headers["Authorization"] = f"Bearer {self.access_token}"

        return headers

    def get_stock_by_deposit(self, sku):
        estoques = {}

        for nome, deposito_id in [("SP", self.deposit_sp), ("FOZ", self.deposit_foz)]:
            url = f"{self.base_url}/estoques/saldos/{deposito_id}"
            params = {
                "codigos[]": sku
            }

            headers = {
                "Authorization": f"Bearer {self.access_token}",
                "Content-Type": "application/json"
            }

            try:
                response = requests.get(url, headers=headers, params=params)
                print(f"📦 Buscando estoque do SKU {sku} no depósito {nome} ({deposito_id})")
                print(f"🔗 URL requisitada: {response.url}")

                response.raise_for_status()
                data = response.json()
                produtos = data.get("data", [])

                for produto in produtos:
                    if produto.get("produto", {}).get("codigo") == sku:
                        saldo = produto.get("saldoFisicoTotal", 0)
                        print(f"✔️ Estoque encontrado para {sku} no depósito {nome}: {saldo}")
                        estoques[nome] = saldo
                        break
                else:
                    print(f"⚠️ SKU {sku} não encontrado no depósito {nome}")
                    estoques[nome] = 0

            except requests.exceptions.RequestException as e:
                print(f"❌ Erro ao buscar estoque de {sku} no depósito {nome}: {e}")
                estoques[nome] = 0

        return estoques


