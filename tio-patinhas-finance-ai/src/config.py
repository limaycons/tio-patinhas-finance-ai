import os
from dotenv import load_dotenv

load_dotenv()

# Configurações globais do sistema
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Caminhos padrão dos arquivos da pasta data
DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))

PATH_PERFIL = os.path.join(DATA_PATH, "perfil_usuario.json")
PATH_TRANSACOES = os.path.join(DATA_PATH, "extrato_transacoes.csv")
PATH_COFRES = os.path.join(DATA_PATH, "cofres_e_investimentos.json")
PATH_HISTORICO = os.path.join(DATA_PATH, "historico_consultas.json")