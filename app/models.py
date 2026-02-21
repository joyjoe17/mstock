from sqlalchemy import Column, String, Float, DateTime, Integer
from datetime import datetime
from app.database import Base

class Signal(Base):
    __tablename__ = "signals"

    signal_id = Column(String, primary_key=True, index=True)
    symbol = Column(String)
    side = Column(String)
    strength = Column(Float)
    status = Column(String)
    generated_at = Column(DateTime, default=datetime.utcnow)


class Trade(Base):
    __tablename__ = "trades"

    trade_id = Column(String, primary_key=True, index=True)
    signal_id = Column(String)
    symbol = Column(String)
    side = Column(String)
    quantity = Column(Integer)
    entry_price = Column(Float)
    sl_price = Column(Float)
    status = Column(String)
    opened_at = Column(DateTime, default=datetime.utcnow)
    closed_at = Column(DateTime, nullable=True)