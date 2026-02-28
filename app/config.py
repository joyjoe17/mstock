import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")

OPENALGO_API_KEY = os.getenv("OPENALGO_API_KEY")
OPENALGO_HOST = os.getenv("OPENALGO_HOST")
OPENALGO_WS_URL = os.getenv("OPENALGO_WS_URL")

SCAN_INTERVAL_MINUTES = int(os.getenv("SCAN_INTERVAL_MINUTES", "5"))
INITIAL_SL_POINTS = float(os.getenv("INITIAL_SL_POINTS", "8"))
TRAIL_STEP_POINTS = float(os.getenv("TRAIL_STEP_POINTS", "2"))
TRAIL_GAP_POINTS = float(os.getenv("TRAIL_GAP_POINTS", "4"))
MAX_OPEN_TRADES = int(os.getenv("MAX_OPEN_TRADES", "3"))
