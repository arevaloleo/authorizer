from flask import request, jsonify
from src.infrastructure.jwks_fetcher import JWKSFetcher
from src.infrastructure.token_validator import TokenValidator
from src.domain.policy import PolicyGenerator
from src.domain.formatPath import FormatPath
from src.domain.issuerValidate import IssuerValidator

jwks_fetcher = JWKSFetcher()
jwks = jwks_fetcher.fetch_jwks()
token_validator = TokenValidator(jwks)

def authorizer():
    data = request.get_json()
    
    format_path = FormatPath(data)
    
    path = format_path.formatter()
    token = (data["token"].split(' '))[1]
    
    #validar el ingreso del token
    if not token:
        return jsonify({'message': 'unathorized'}), 401
    
  
    #validación de vencimiento y firma del token
    claims = token_validator.validate_token(token)
    if not claims:
        return jsonify({"error": "Unauthorized"}), 401
    scopes = claims.get("scope", "").split()
    
      #validar issuer
    issuer_object = IssuerValidator()
    issuer = claims.get("iss")
    print('issuer', issuer)
    audience = claims.get("aud")
    if not issuer_object.is_audience_valid(issuer, audience):
        return jsonify({"error": "Unauthorized"}), 401
    
    #validación de policy generada
    policy_generator = PolicyGenerator(scopes)
    policy = policy_generator.validateTokenWithPolicy(path)
    if policy:
        return jsonify({'message': 'authorized'}), 200
    return jsonify({'message': 'unathorized'}), 401
