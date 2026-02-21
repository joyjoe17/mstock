from app.config import TRAIL_STEP_POINTS, TRAIL_GAP_POINTS

def update_sl(current_price, entry_price, current_sl):
    move = current_price - entry_price
    if move >= TRAIL_STEP_POINTS:
        new_sl = current_price - TRAIL_GAP_POINTS
        return max(new_sl, current_sl)
    return current_sl