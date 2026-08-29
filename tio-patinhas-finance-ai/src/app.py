import streamlit as st
import pandas as pd
from agente import carregar_dados, calcular_regra_50_30_20, gerar_system_prompt

# Configuração da página Streamlit
st.set_page_config(
    page_title="Tio Patinhas - Mentor Financeiro",
    page_icon="🪙",
    layout="wide"
)

st.title("🪙 Tio Patinhas - Guardião do Seu Cofre")
st.subheader("Análise Financeira Inteligente & Regra 50/30/20")

# Carregando os dados da pasta data/
perfil, transacoes, cofres = carregar_dados()

if perfil is None:
    st.error("Erro ao carregar os arquivos da pasta 'data/'. Verifique se os arquivos existem!")
else:
    # Sidebar - Perfil do Usuário
    st.sidebar.header("👤 Perfil do Cliente")
    st.sidebar.write(f"**Nome:** {perfil['nome']}")
    st.sidebar.write(f"**Profissão:** {perfil['profissao']}")
    st.sidebar.write(f"**Renda Mensal:** R$ {perfil['renda_mensal']:.2f}")
    st.sidebar.write(f"**Reserva Atual:** R$ {perfil['reserva_emergencia_atual']:.2f}")

    # Processamento dos números
    resumo = calcular_regra_50_30_20(perfil, transacoes)

    # Exibição de Métricas em Cards
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Renda Mensal", f"R$ {resumo['renda']:.2f}")
    col2.metric("Necessidades (50%)", f"{resumo['pct_essenciais']:.1f}%", delta=f"R$ {resumo['essenciais']:.2f}")
    col3.metric("Desejos (30%)", f"{resumo['pct_desejos']:.1f}%", delta=f"R$ {resumo['desejos']:.2f}")
    col4.metric("Futuro / Cofre (20%)", f"{resumo['pct_futuro']:.1f}%", delta=f"R$ {resumo['futuro']:.2f}")

    st.divider()

    # Visualização do Extrato
    st.write("### 📜 Extrato de Transações Analisado")
    st.dataframe(transacoes, use_container_width=True)

    st.divider()

    # Chat / Interação com o Tio Patinhas
    st.write("### 💬 Conversar com o Tio Patinhas")
    pergunta_usuario = st.text_input("Faça uma pergunta sobre suas finanças ou peça um diagnóstico:", 
                                     placeholder="Ex: Como posso fechar minha reserva de emergência mais rápido?")

    if st.button("Consultar o Tio Patinhas"):
        if pergunta_usuario:
            prompt = gerar_system_prompt(perfil, resumo, cofres)
            
            st.info("🪙 **Tio Patinhas está contando suas moedas...**")
            
            # Resposta simulada/estruturada baseada nos dados exatos
            st.markdown(f"""
            ### 📊 Raio-X Financeiro
            * **Renda Mensal:** R$ {resumo['renda']:.2f}
            * **Necessidades:** R$ {resumo['essenciais']:.2f} ({resumo['pct_essenciais']:.1f}%)
            * **Desejos/Lazer:** R$ {resumo['desejos']:.2f} ({resumo['pct_desejos']:.1f}%)
            * **Aporte Atual no Cofre:** R$ {resumo['futuro']:.2f} ({resumo['pct_futuro']:.1f}%)

            🏆 **Nota de Saúde Financeira:** 75/100  
            🌱 **Nível de Maturidade Financeira:** Organização 📈

            ⚠️ **Alertas do Cofre:**
            * Seus gastos essenciais consomem {resumo['pct_essenciais']:.1f}% da sua renda. O ideal é manter em até 50%.
            * Seus aportes atuais de {resumo['pct_futuro']:.1f}% no cofre estão abaixo da meta ideal de 20%!

            💡 **Dicas do Tio Patinhas:**
            * Você gastou R$ {resumo['desejos']:.2f} em delivery e passeios este mês. Se cortar R$ 250 desse valor, conseguiremos dobrar seu aporte mensal!
            * Guarde suas moedas da reserva de emergência no **Cofre de Liquidez Rápida (Tesouro Selic)** ou no **Cofre Forte Diário (CDB 102%)**.

            🎯 **Missão dos Próximos 30 Dias:**
            1. Trocar 2 entregas de iFood na semana por comida caseira.
            2. Aumentar o aporte do cofre de R$ 500,00 para R$ 750,00 no próximo dia 1.
            """)
        else:
            st.warning("Por favor, digite uma pergunta para o Tio Patinhas!")