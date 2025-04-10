from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables from .env file (or platform-specific)
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Fetch environment variables securely
wallet_address = os.getenv("WALLET_ADDRESS")  # This is the sensitive wallet address (encrypted in platform)
roi_env = os.getenv("SKYVAULT_ENV")           # Environment: 'production' or 'staging'
debug_mode = os.getenv("DEBUG", "false")      # Debug mode (True/False), defaults to 'false'
compounding_enabled = os.getenv("ENABLE_COMPOUNDING", "true")  # If ROI compounding is enabled
autoscale_strategy = os.getenv("AUTOSCALE_STRATEGY", "smart-streak")  # Autoscaling strategy
max_containers = os.getenv("MAX_CONTAINERS", "5")  # Max number of containers (defaults to 5)
payout_threshold_usd = os.getenv("PAYOUT_THRESHOLD_USD", "50000")  # Payout threshold in USD (defaults to 50K)

@app.route("/vault-status")
def vault_status():
    """
    Endpoint to return current vault status and configuration details.
    """
    return {
        "status": "LIVE",
        "roi": "Engine Active",
        "wallet_connected": bool(wallet_address),  # If wallet address exists, it's connected
        "wallet_address": wallet_address if wallet_address else "Not Set",  # Display wallet address or "Not Set"
        "env": roi_env,
        "debug_mode": debug_mode,
        "compounding_enabled": compounding_enabled,
        "autoscale_strategy": autoscale_strategy,
        "max_containers": max_containers,
        "payout_threshold_usd": payout_threshold_usd
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=(debug_mode.lower() == "true"))
