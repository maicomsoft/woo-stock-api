# sync.py
from bling_api import BlingAPI
from woocommerce_api import WooCommerceAPI
import os
from dotenv import load_dotenv

load_dotenv()

def sync_estoque():
    bling = BlingAPI()

    # Teste de autenticação (opcional para debug)
    # test = requests.get("https://www.bling.com.br/Api/v3/usuarios/me", headers=bling.get_headers())
    # print("🔐 Teste de autenticação Bling:", test.status_code)
    # print("Resposta:", test.json())

    bling.refresh_access_token()
    woo = WooCommerceAPI()

# Lista de SKUs para sincronizar
sku_list = [
    "SONYP5MIDIAFISICA",
    "OL2ARARA60",
    "KTPT03PT6020",
    "KTNC3WCPT",
    "MESAESTUDO120X40PTTX",
    "MIVACUUMS10",
    "FIRETV4K3GD",
    "FIRETV4K2GD",
    "MESAESTUDO120X40BRTX",
    "ECHODOT5STPT",
    "ECHOPOP1STCZ",
    "ECHOPOP1STPT",
    "MONDIAL-LIQUID-L99-PT",
    "BARBEADOR-DRAGAO",
    "CADENCE-CHALEIRA-CEL388",
    "BRITANIA-CAFETEIRA-CP15",
    "BRITANIA-AIRFRYER-64001069",
    "BRITANIA-GRIL-64001069",
    "OR-PL21SC",
    "CADENCIA-SAPA-09PRAT-PT",
    "OR-PL610",
    "ROADSTARTRAVAELETRICA",
    "OL2-GUARDARP-02P-CZ",
    "METAL-TALITA-CHUVEIRO-3321-CROMADO",
    "METAL-TALITA-CHUVEIRO-3321-BLACK",
    "ROADSTARMP5RS401BRMIPLUS",
    "ROADSTARMP5RS815BRMIPLUS",
    "123456a",
    "ROADSTARCAMERARS201BR",
    "TENDACAMPING0AZUL2P",
    "ROADSTARBABA1020BR",
    "ELG-MOUSEPAD-SENSECONTROL",
    "ELG-MOUSEPAD-FLKMP002",
    "FN-EWTTO-AZ",
    "ELG-HEADSET-EXODUS",
    "ELG-CABO-USBC-ROSE",
    "ELG-CABO-USBC-DOURADO",
    "ELG-CABO-USBC-INOX",
    "ELG-CABO-MICROUSB-ROSE",
    "ELG-CABO-MICROUSB-GOLD",
    "ELG-CABO-MICROUSB-inox",
    "ELG-CABO-MICROUSB-SILVER",
    "ELG-ADAPT-P3",
    "KTNC2WCBR",
    "DISPENSERGRAOS6DIV",
    "VENT-ANX-PT-127",
    "VENT-ANX-PT-220",
    "ROADSTARMP5RS915BRMIPLUS",
    "PERFALHAMBRALOVELY80ML",
    "KTPT03BR6020",
    "ADAPTADOREUROPEU",
    "PERFLATTAFAKHALTAT100ML",
    "AMAZFIRE10332PT",
    "AVATTOIRRF",
     
    
]

deposit_sp = os.getenv("BLING_DEPOSIT_SP")
    deposit_foz = os.getenv("BLING_DEPOSIT_FOZ")

    for sku in sku_list:
        estoques = bling.get_stock_by_deposit(sku)
        sp_stock = estoques.get("SP", 0)
        foz_stock = estoques.get("FOZ", 0)
        woo.update_custom_fields(sku, sp_stock, foz_stock)
