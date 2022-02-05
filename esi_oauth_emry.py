from email import header
import hashlib
from urllib import request
from wsgiref import headers
import base64
import secrets
from random import randbytes
from shared_flow import send_sso_request
from shared_flow import handle_sso_token_response


client_id = "9916e227ce8e45faa1091e7331d06c3f"
random = base64.urlsafe_b64encode(secrets.token_bytes(32))
m = hashlib.sha256()
m.update(random)
d = m.digest()
code_challenge = base64.urlsafe_b64encode(d).decode().replace("=", "")

redirect_url = f'https://login.eveonline.com/v2/oauth/authorize/?response_type=code&redirect_uri=https%3A%2F%2Flocalhost%2Fcallback%2F&client_id={client_id}&scope=esi-wallet.read_corporation_wallets.v1%20esi-industry.read_character_mining.v1&{code_challenge}&code_challenge_method=S256&state=playground'

print(redirect_url)

auth_code = input()
code_verifier = random

form_values = {
    "grant_type": "authorization_code",
    "client_id": client_id,
    "code": auth_code,
    "code_verifier": code_verifier
}

res = send_sso_request(form_values)

data = handle_sso_token_response(res)


# f"grant_type=authorization_code&code={auth_code}&client_id={client_id}&code_verifier={code_verifier}"
# if send_req.status_code == 200:
#     data = send_req.json()
#    access_token = data["access_token"]

# print(send_req)

print(data)