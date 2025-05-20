from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables del archivo .env

google_oauth_json = os.getenv("GOOGLE_OAUTH_JSON")
