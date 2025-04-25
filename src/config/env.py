from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
ENDPOINT = os.getenv("ENDPOINT")
MODEL = os.getenv("MODEL")

if not TOKEN or not ENDPOINT or not MODEL:
    raise ValueError("Falta una variable de entorno requerida.")
