import uuid
from app.config import INITIAL_SL_POINTS

def execute_trade(symbol: str, quantity: int):
    # Replace with real OpenAlgo call
    return {
        "order_id": uuid.uuid4().hex[:10],
        "average_price": 200.0
    }

def close_trade(symbol: str, quantity: int):
    return {
        "exit_order_id": uuid.uuid4().hex[:10]
    }