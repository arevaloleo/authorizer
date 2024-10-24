import requests
from authlib.jose import JsonWebKey
import os
from dotenv import load_dotenv

load_dotenv()

AUTH0_JWKS_URL = os.getenv('AUTH0_JWKS_URL')

class JWKSFetcher:
    def __init__(self, url=AUTH0_JWKS_URL):
        self.url = url

    def fetch_jwks(self):
        response = requests.get(self.url)
        print("firma del token", response)
        if response.status_code == 200:
            jwks_data = response.json()
            return JsonWebKey.import_key_set(jwks_data)
        raise Exception("Unable to fetch JWKS")
