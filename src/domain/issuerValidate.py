class IssuerValidator:
    def __init__(self):
        self.issuer_data = [
            {
                "issuer": {
                    "url": "https://dev-up6y0744.us.auth0.com/",
                    "audiences": ["https://pokemon-go.com/api"]
                }
            },
            {
                "issuer": {
                    "url": "https://dev-222222.us.auth0.com/",
                    "audiences": ["https://pokeemon-go.com/api"]
                }
            }
        ]

    def is_audience_valid(self, issuer, audience):
        for item in self.issuer_data:
            if item["issuer"]["url"] == issuer:
                if audience in item["issuer"]["audiences"]:
                    return True
        return False
