import requests
import os
from dotenv import load_dotenv

load_dotenv()

class WooCommerceAPI:
    def __init__(self):
        self.api_url = os.getenv("WC_API_URL")
        self.consumer_key = os.getenv("WC_CONSUMER_KEY")
        self.consumer_secret = os.getenv("WC_CONSUMER_SECRET")

    def update_custom_fields(self, sku, sp_stock, foz_stock):
        product = self.get_product_by_sku(sku)
        if not product:
            print(f"Produto com SKU {sku} não encontrado.")
            return

        product_id = product["id"]
        meta_data = [
            {"key": "stock_center_sp", "value": sp_stock},
            {"key": "stock_center_foz", "value": foz_stock},
        ]

        response = requests.put(
            f"{self.api_url}/products/{product_id}",
            auth=(self.consumer_key, self.consumer_secret),
            json={"meta_data": meta_data}
        )

        if response.status_code == 200:
            print(f"Estoque atualizado para SKU {sku}")
        else:
            print(f"Erro ao atualizar SKU {sku}: {response.content}")

    def get_product_by_sku(self, sku):
        response = requests.get(
            f"{self.api_url}/products",
            auth=(self.consumer_key, self.consumer_secret),
            params={"sku": sku}
        )
        if response.status_code == 200 and response.json():
            return response.json()[0]
        return None
