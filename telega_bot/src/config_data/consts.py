import os

ROOT_PATH = os.path.abspath(os.path.join(__file__, "..", "..", ".."))
DATA_PATH = os.path.join(ROOT_PATH, "data")
DATABASE_PATH = os.path.join(DATA_PATH, "database") + os.sep
FINDED_API_DB = "finded_api.db"
AUTH_CHOICE = ("Yes", "No", "OAuth", "apiKey")
