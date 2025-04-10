# skyvault_core/engine.py

from flask import Blueprint
from apscheduler.schedulers.background import BackgroundScheduler
import random

roi_engine = Blueprint('roi_engine', __name__)

profit = 0.0
vault_threshold = 50000

def simulate_roi_cycle():
    global profit
    earning = random.uniform(1500, 3500)  # Simulates real profits between $1,500-$3,500 every cycle
    profit += earning
    print(f"[SkyVault ROI] Generated profit: ${earning:.2f}, Total: ${profit:.2f}")

scheduler = BackgroundScheduler()
scheduler.add_job(simulate_roi_cycle, 'interval', seconds=15)
scheduler.start()

@roi_engine.route('/vault-status')
def vault_status():
    global profit
    return {
        "profit": f"${profit:,.2f}",
        "next_threshold": f"${vault_threshold:,.2f}",
        "status": "🔁 Compounding Active",
        "wallet_connected": True,
        "roi": "Engine Active"
    }
