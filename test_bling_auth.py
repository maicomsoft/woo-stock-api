<<<<<<< HEAD
import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("BLING_CLIENT_ID")
client_secret = os.getenv("BLING_CLIENT_SECRET")
refresh_token = os.getenv("BLING_REFRESH_TOKEN")

url = "https://www.bling.com.br/Api/v3/oauth/token"

# Codifica client_id:client_secret em base64
auth_string = f"{client_id}:{client_secret}"
auth_base64 = base64.b64encode(auth_string.encode()).decode()

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Basic {auth_base64}"
}

data = {
    "grant_type": "refresh_token",
    "refresh_token": refresh_token
}

response = requests.post(url, headers=headers, data=data)

print("Status Code:", response.status_code)
print("Resposta JSON:")
print(response.json())
=======
import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("BLING_CLIENT_ID")
client_secret = os.getenv("BLING_CLIENT_SECRET")
refresh_token = os.getenv("BLING_REFRESH_TOKEN")

url = "https://www.bling.com.br/Api/v3/oauth/token"

# Codifica client_id:client_secret em base64
auth_string = f"{client_id}:{client_secret}"
auth_base64 = base64.b64encode(auth_string.encode()).decode()

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Basic {auth_base64}"
}

data = {
    "grant_type": "refresh_token",
    "refresh_token": refresh_token
}

response = requests.post(url, headers=headers, data=data)

print("Status Code:", response.status_code)
print("Resposta JSON:")
print(response.json())
>>>>>>> be237b2 (Adiciona arquivos da API: sync, bling, woocommerce)
