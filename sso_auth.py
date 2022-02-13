from email import header
import imp
from urllib import request
from wsgiref import headers
from esipy import EsiClient
from esipy import EsiSecurity
from esipy import EsiApp
import webbrowser
import sqlite3

client_id = "9916e227ce8e45faa1091e7331d06c3f"
secret_key = "ZRvGn6KnCvWnY01KZQvyIdbtYtGz4wtRT0M7of45"
callback = "https://localhost/callback/"
email_header = {"User-Agent":"emry.kinney@gmail.com"}
scopes = ["esi-industry.read_character_mining.v1", "esi-wallet.read_corporation_wallets.v1"]

app = EsiApp().get_latest_swagger

security = EsiSecurity(
    redirect_uri=callback,
    client_id=client_id,
    secret_key=secret_key,
    headers=email_header
)

client = EsiClient(
    retry_requests=True,
    headers=email_header,
    security=security
)

webbrowser.open(security.get_auth_uri(state="playground", scopes=scopes))

auth_code = input()

tokens = security.auth(auth_code)
refresh_token = tokens["refresh_token"]

security.update_token({
    "access_token":"",
    "expires_in": -1,
    "refresh_token":refresh_token
})

tokens = security.refresh()

api_info = security.verify()

character_id = api_info['sub'].split(':')[-1]

op = app.op["get_characters_character_id_mining"](
    character_id = character_id
)

ledger = client.request(op)

print(ledger.data)