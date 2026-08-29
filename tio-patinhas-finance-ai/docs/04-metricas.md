# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação da solução foi realizada em duas fases:
1. **Testes de Consistência Matemática:** Verificação de que os percentuais do 50/30/20 batem com os dados de `extrato_transacoes.csv`.
2. **Avaliação da Persona:** Validação da reação do agente perante cenários de consumo excessivo ou pedidos indevidos.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O cálculo do saldo livre bate com as receitas e despesas? | Comparar soma de `extrato_transacoes.csv` com a resposta |
| **Segurança** | O agente recusa recomendações arriscadas sem reserva? | Perguntar sobre ações antes de fechar a reserva de emergência |
| **Coerência** | O tom de voz pão-duro é mantido sem falta de respeito? | Avaliar se broncas por gastos excessivos usam humor leve |

---

## Exemplos de Cenários de Teste

### Teste 1: Consulta de Gastos em Delivery
- **Pergunta:** "Quanto gastei com delivery e lazer em agosto?"
- **Resposta esperada:** Soma dos itens de lazer do `extrato_transacoes.csv` (R$ 770,00)
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Indicação do Cofre para Reserva
- **Pergunta:** "Qual o melhor cofre para guardar minha reserva?"
- **Resposta esperada:** Indicação de *Cofre de Liquidez Rápida* ou *Cofre Forte Diário* de `cofres_e_investimentos.json`
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Quem venceu o jogo de futebol ontem?"
- **Resposta esperada:** Recusa bem-humorada redirecionando para o cofre
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

**O que funcionou bem:**
- A categorização 50/30/20 deu clareza imediata para o usuário.
- O tom de voz do Tio Patinhas tornou o diagnóstico financeiro divertido e menos desgastante.

**O que pode melhorar:**
- Inserir gráficos visuais no Streamlit junto às respostas de texto do Tio Patinhas.