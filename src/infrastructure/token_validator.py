from authlib.jose import jwt, JoseError

class TokenValidator:
    def __init__(self, jwks):
        self.jwks = jwks

    def validate_token(self, token):
        try:
            print(self.jwks)
            claims = jwt.decode(token, self.jwks)
            claims.validate()
            return claims
        except JoseError:
            print(JoseError)
            return None
