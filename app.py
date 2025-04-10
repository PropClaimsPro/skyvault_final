from flask import Flask
from skyvault_core.engine import initialize_vault

app = Flask(__name__)

@app.route("/vault-status")
def vault_status():
    return initialize_vault()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)