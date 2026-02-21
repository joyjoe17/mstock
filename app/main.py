import uuid
from datetime import datetime
from fastapi import FastAPI, WebSocket, HTTPException
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app.models import Signal, Trade
from app.scanner import run_scan
from app.execution import execute_trade, close_trade
from app.sl_engine import update_sl
from app.websocket_manager import ws_manager
from app.risk import validate_risk
from app.config import SCAN_INTERVAL_MINUTES, INITIAL_SL_POINTS

Base.metadata.create_all(bind=engine)

app = FastAPI()
scheduler = BackgroundScheduler()
scheduler.add_job(run_scan, "interval", minutes=SCAN_INTERVAL_MINUTES)
scheduler.start()


@app.get("/scan")
def get_signals():
    db = SessionLocal()
    signals = db.query(Signal).filter(Signal.status == "PENDING_CONFIRMATION").all()
    db.close()
    return signals


@app.post("/trade/confirm/{signal_id}")
def confirm_trade(signal_id: str):
    if not validate_risk():
        raise HTTPException(400, "Max open trades reached")

    db = SessionLocal()
    signal = db.query(Signal).filter(Signal.signal_id == signal_id).first()

    if not signal:
        raise HTTPException(404, "Signal not found")

    broker = execute_trade(signal.symbol, 1)

    trade = Trade(
        trade_id=uuid.uuid4().hex[:12],
        signal_id=signal_id,
        symbol=signal.symbol,
        side=signal.side,
        quantity=1,
        entry_price=broker["average_price"],
        sl_price=broker["average_price"] - INITIAL_SL_POINTS,
        status="OPEN",
        opened_at=datetime.utcnow()
    )

    signal.status = "CONSUMED"
    db.add(trade)
    db.commit()
    db.close()

    return {"trade_id": trade.trade_id}


@app.websocket("/ws/trades")
async def ws_trades(websocket: WebSocket):
    await ws_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except:
        await ws_manager.disconnect(websocket)