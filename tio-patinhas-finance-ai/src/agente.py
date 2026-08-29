import json
import pandas as pd
import requests
from config import PATH_PERFIL, PATH_TRANSACOES, PATH_COFRES

def consultar_tio_patinhas_ollama(pergunta_usuario, perfil, resumo_financeiro, cofres, modelo="llama3"):
    """Envia a requisição direta para o servidor local do Ollama."""
    
    system_prompt = f"""Você é o Tio Patinhas, um mentor de finanças pessoais esperto, extremamente econômico, levemente "mão de vaca" e protetor do cofre.

DADOS DO USUÁRIO ({perfil.get('nome', 'Cliente')}):
- Renda Mensal: R$ {resumo_financeiro['renda']:.2f}
- Gastos Essenciais: R$ {resumo_financeiro['essenciais']:.2f} ({resumo_financeiro['pct_essenciais']:.1f}%)
- Gastos com Desejos: R$ {resumo_financeiro['desejos']:.2f} ({resumo_financeiro['pct_desejos']:.1f}%)
- Aportes no Cofre: R$ {resumo_financeiro['futuro']:.2f} ({resumo_financeiro['pct_futuro']:.1f}%)

FORMATO OBRIGATÓRIO DE RESPOSTA:
📊 Raio-X Financeiro
🏆 Nota de Saúde Financeira (0 a 100)
🌱 Nível de Maturidade Financeira
⚠️ Alertas do Cofre
💡 Dicas do Tio Patinhas
🎯 Missão dos Próximos 30 Dias
"""

    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": modelo,
        "system": system_prompt,
        "prompt": pergunta_usuario,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, timeout=60)
        if response.status_code == 200:
            return response.json().get("response", "Sem resposta do modelo.")
        else:
            return f"Erro no Ollama ({response.status_code}): Verifique se o servidor está ativo."
    except Exception as e:
        return f"Não foi possível conectar ao Ollama local. Certifique-se de ter executado 'ollama serve'. Erro: {str(e)}"
