import os
from dotenv import load_dotenv

# CARGAR VARIABLES DE ENTORNO
load_dotenv()
MAPON_BASE_URL = os.getenv('MAPON_BASE_URL')
MAPON_API_KEY = os.getenv('MAPON_API_KEY')
