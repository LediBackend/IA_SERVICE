from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
TOKEN_DE_TATI = os.getenv("GITHUB_TOKEN_TATI")#  Expira el 25 de Julio
TOKEN_DE_SELENE = os.getenv("GITHUB_TOKEN_SELENE")# Expira el 25 de Julio
# TOKEN_DE_LUCAS = os.getenv("")
# TOKEN_DE_JAQUI = os.getenv("")
# TOKEN_DE_AYELEN = os.getenv("")

ENDPOINT = os.getenv("ENDPOINT")
MODEL = os.getenv("MODEL")

if not TOKEN or not TOKEN_DE_TATI or not  ENDPOINT or not MODEL:
    raise ValueError("Falta una variable de entorno requerida.")
