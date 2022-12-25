import os
from dotenv import load_dotenv


dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

SAVE_FILENAME = os.getenv("SAVE_FILENAME") or "save.bin"
SAVE_FILE_PATH = os.path.join(dirname, "..", "data", SAVE_FILENAME)

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "highscores.db"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)
