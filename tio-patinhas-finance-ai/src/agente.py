import json
import pandas as pd
from config import PATH_PERFIL, PATH_TRANSACOES, PATH_COFRES

def carregar_dados():
    """Carrega os dados da pasta data."""
    try:
        with open(PATH_PERFIL, "r", encoding="utf-8") as f:
            perfil = json.load(f)
        with open(PATH_COFRES, "r", encoding="utf-8") as f:
            cofres = json.load(f)
        transacoes = pd.read_csv(PATH_TRANSACOES)
        return perfil, transacoes, cofres
    except Exception as e:
        return None, None, None

def calcular_regra_50_30_20(perfil, transacoes):
    """Calcula os totais e percentuais do orçamento."""
    renda = perfil.get("renda_mensal", 0)
    
    essenciais = transacoes[transacoes["classificacao"] == "Essencial"]["valor"].abs().sum()
    desejos = transacoes[transacoes["classificacao"] == "Desejo"]["valor"].abs().sum()
    futuro = transacoes[transacoes["classificacao"] == "Futuro"]["valor"].abs().sum()
    
    pct_essenciais = (essenciais / renda * 100) if renda > 0 else 0
    pct_desejos = (desejos / renda * 100) if renda > 0 else 0
    pct_futuro = (futuro / renda * 100) if renda > 0 else 0
    
    saldo_livre = renda - (essenciais + desejos + futuro)
    
    return {
        "renda": renda,
        "essenciais": essenciais,
        "pct_essenciais": pct_essenciais,
        "desejos": desejos,
        "pct_desejos": pct_desejos,
        "futuro": futuro,
        "pct_futuro": pct_futuro,
        "saldo_livre": saldo_livre
    }

def gerar_system_prompt(perfil, resumo_financeiro, cofres):
    """Gera o System Prompt completo do Tio Patinhas com os dados injetados."""
    return f"""Você é o Tio Patinhas, um mentor de educação financeira pessoal esperto, extremamente econômico, levemente "mão de vaca" e focado em proteger o cofre do usuário.

DADOS ATUAIS DO USUÁRIO ({perfil['nome']}):
- Renda Mensal: R$ {resumo_financeiro['renda']:.2f}
- Reserva de Emergência Atual: R$ {perfil['reserva_emergencia_atual']:.2f} de R$ 15.000,00 (Meta Principal)
- Gastos Essenciais (50% ideal): R$ {resumo_financeiro['essenciais']:.2f} ({resumo_financeiro['pct_essenciais']:.1f}%)
- Gastos com Desejos (30% ideal): R$ {resumo_financeiro['desejos']:.2f} ({resumo_financeiro['pct_desejos']:.1f}%)
- Aportes no Cofre (20% ideal): R$ {resumo_financeiro['futuro']:.2f} ({resumo_financeiro['pct_futuro']:.1f}%)
- Saldo Livre Restante: R$ {resumo_financeiro['saldo_livre']:.2f}

COFRES DISPONÍVEIS PARA RECOMENDAÇÃO:
{json.dumps(cofres, ensure_ascii=False, indent=2)}

REGRAS OBRIGATÓRIAS DE RESPOSTA:
1. NUNCA invente números ou dados financeiros.
2. Use analogias de cofre, moedas salvas e proteção contra desperdícios.
3. Mantenha o tom bem-humorado, mão de vaca e educativo.
4. Responda SEMPRE seguindo a estrutura abaixo:

📊 Raio-X Financeiro
🏆 Nota de Saúde Financeira (0 a 100)
🌱 Nível de Maturidade Financeira (Sobrevivência, Organização, Estabilidade, Crescimento ou Liberdade)
⚠️ Alertas do Cofre
💡 Dicas do Tio Patinhas
🎯 Missão dos Próximos 30 Dias
"""