import fnmatch
class PolicyGenerator:
    def __init__(self, scopes):
        self.scopes = scopes
    def validateTokenWithPolicy(self, path):
        policy = (self.generate_policy(path))
        if any(fnmatch.fnmatch(path, endpoint) for endpoint in policy['endpoints']):
            return True
        return False
    
    def generate_policy(self, path):
        endpoints = set()
        if "read.especific-pokemon" in self.scopes:
            endpoints.add("GET/pokemon/*")

        if "read.pokemon" in self.scopes:
            endpoints.add("GET/pokemon/*")
            endpoints.add("GET/pokemon/azar")
            endpoints.add("GET/pokemon")

        return {
            "endpoints": list(endpoints)
        }
