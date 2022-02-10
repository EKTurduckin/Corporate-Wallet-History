import sys
import requests
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError, JWTClaimsError

def validate_eve_jwt(jwt_token):
    
    jwk_set_url = "https://login.eveonline.com/oauth/jwks"

    res = requests.get(jwk_set_url)
    res.raise_for_status()

    data = res.json()

    jwk_sets = data["keys"]
    
    jwk_set = next((item for item in jwk_sets if item["alg"] == "RS256"))

    return jwt.decode(
        jwt_token,
        jwk_set,
        algorithms=jwk_set["alg"],
        issuer="login.eveoline.com"
    )