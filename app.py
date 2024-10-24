from flask import Flask
from src.controllers.authorizer_controller import authorizer

app = Flask(__name__)

@app.route("/authorizer", methods=["POST"])
def authorize():
    return authorizer()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4200)
