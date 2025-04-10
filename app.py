from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

wallet_address = os.getenv("WALLET_ADDRESS")
roi_env = os.getenv("SKYVAULT_ENV", "production")
debug_mode = os.getenv("DEBUG", "false")
compounding_enabled = os.getenv("ENABLE_COMPOUNDING", "true")
autoscale_strategy = os.getenv("AUTOSCALE_STRATEGY", "smart-streak")
max_containers = os.getenv("MAX_CONTAINERS", "5")
payout_threshold_usd = os.getenv("PAYOUT_THRESHOLD_USD", "50000")

@app.route("/vault-status")
def vault_status():
    return {
        "status": "LIVE",
        "roi": "Engine Active",
        "wallet_connected": bool(wallet_address),
        "wallet_address": wallet_address or "Not Set",
        "env": roi_env,
        "debug_mode": debug_mode,
        "compounding_enabled": compounding_enabled,
        "autoscale_strategy": autoscale_strategy,
        "max_containers": max_containers,
        "payout_threshold_usd": payout_threshold_usd
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=(debug_mode.lower() == "true"))
