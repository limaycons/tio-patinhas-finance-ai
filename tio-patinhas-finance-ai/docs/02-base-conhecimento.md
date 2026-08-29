# Base de Conhecimento

## Dados Utilizados

A base de conhecimento do Tio Patinhas utiliza dados mockados organizados na pasta `data/`:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `perfil_usuario.json` | JSON | Contém renda, patrimônio, meta atual e saldo guardado |
| `cofres_e_investimentos.json` | JSON | Catálogo de produtos para reserva e renda fixa com descrições educativas |
| `extrato_transacoes.csv` | CSV | Registros detalhados de despesas essenciais, supérfluos e receitas |
| `historico_consultas.json` | JSON | Contextualiza conversas anteriores e conselhos já fornecidos ao usuário |

---

## Adaptações nos Dados

Os dados originais foram adaptados para refletir a linguagem e as regras do Tio Patinhas:
- **`extrato_transacoes.csv`:** Incluiu a coluna `classificacao` (`Essencial`, `Desejo`, `Entrada`, `Futuro`) para automatizar a leitura da regra 50/30/20.
- **`cofres_e_investimentos.json`:** Os produtos financeiros foram batizados como "Cofres" (ex: *Cofre de Liquidez Rápida*, *Cofre Forte Diário*, *Cofre Blindado*) com foco em liquidez e isenção de impostos.

---

## Estratégia de Integração

### Como os dados são carregados?
No início da execução da aplicação (Streamlit), o arquivo `perfil_usuario.json` e o histórico do `extrato_transacoes.csv` são lidos via `pandas` e estruturados em memória.

### Como os dados são usados no prompt?
Os dados calculados (total de entradas, % de necessidades, % de desejos e saldo livre) são injetados diretamente no contexto do System Prompt antes de chamar a LLM, garantindo que o Tio Patinhas responda com base nos números exatos do usuário.

---

## Exemplo de Contexto Montado

```text
Dados do Cliente:
- Nome: João Silva
- Renda Mensal: R$ 5.000,00
- Reserva Atual: R$ 10.000,00 de R$ 15.000,00 (Meta: Blindar a Reserva)

Resumo das Transações do Mês:
- Receita: R$ 5.000,00
- Gastos Essenciais (Moradia, Alimentação, Contas): R$ 3.280,00 (65.6%)
- Gastos com Desejos (Lazer, Delivery): R$ 770,00 (15.4%)
- Aportes no Cofre: R$ 500,00 (10.0%)