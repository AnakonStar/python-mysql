from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("DATABASE_HOST", "")
user = os.getenv("DATABASE_USER", "")
password = os.getenv("DATABASE_PASSWORD", "")
schema = os.getenv("DATABASE_SCHEMA", "")

DB_CONFIG = {
    'host': host,
    'user': user,
    'password': password,
    'database': schema,
    'port': 3306,
}
