import uuid
from datetime import datetime
from app.database import SessionLocal
from app.models import Signal

def run_scan():
    db = SessionLocal()

    # Example dummy scanner
    signal = Signal(
        signal_id=uuid.uuid4().hex[:12],
        symbol="NIFTY",
        side="BUY",
        strength=0.85,
        status="PENDING_CONFIRMATION",
        generated_at=datetime.utcnow()
    )

    db.add(signal)
    db.commit()
    db.close()