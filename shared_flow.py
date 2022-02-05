import requests
import json
from validate_jwt import validate_eve_jwt

def send_sso_request(form_values):

    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "login.eveonline.com",
    }

    res = requests.post(
            "https://login.eveonline.com/v2/oauth/token",
            data = form_values,
            headers = headers
            )

    return res

def handle_sso_token_response(sso_response):
    if sso_response.status_code != 200:
        print(sso_response.status_code)
    else:
        data = sso_response.json()
        access_token = data["access_token"]
        # jwt = validate_eve_jwt(access_token)
        # character_id = jwt["sub"].split(":")[2]
        # character_name = jwt["name"]
        # ledger_path = f'/corporations/{corporation_id}/wallets/{division}/journal/'
        # corp_wallet_path = 
        # return jwt
        return data