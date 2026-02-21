from app.config import MAX_OPEN_TRADES
from app.database import SessionLocal
from app.models import Trade

def validate_risk():
    db = SessionLocal()
    open_trades = db.query(Trade).filter(Trade.status == "OPEN").count()
    db.close()

    if open_trades >= MAX_OPEN_TRADES:
        return False
    return True