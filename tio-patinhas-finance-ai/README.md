# 🦆 Tio Patinhas – Assistente Financeiro Inteligente com IA Generativa

## Contexto

A educação financeira ainda é um desafio para milhões de pessoas. Mesmo com aplicativos bancários e planilhas disponíveis, muitos usuários têm dificuldade para entender para onde o dinheiro está indo, identificar excessos de gastos e planejar objetivos financeiros.

O **Tio Patinhas** foi criado para atuar como um mentor financeiro virtual, utilizando Inteligência Artificial Generativa para transformar dados financeiros em orientações simples, práticas e personalizadas.

Diferente de assistentes tradicionais, o Tio Patinhas não apenas responde perguntas. Ele ajuda o usuário a compreender sua realidade financeira, identificar oportunidades de melhoria e desenvolver hábitos financeiros saudáveis.

### Principais Objetivos

* 📊 Organizar receitas, despesas e entradas do extrato;
* 💰 Aplicar automaticamente a metodologia 50/30/20;
* 🎯 Auxiliar no planejamento e blindagem de metas nos cofres;
* 🚨 Identificar excessos de gastos (lazer/delivery) e riscos ao cofre;
* 🏦 Incentivar a criação de reserva de emergência em produtos seguros;
* 📈 Acompanhar a evolução da saúde e maturidade financeira do usuário.

> [!TIP]
> O Tio Patinhas utiliza uma abordagem educativa, direta e bem-humorada ("mão de vaca") para tornar a educação financeira mais acessível e menos intimidadora.

---

# O Que Este Projeto Entrega

## 1. Documentação do Agente

Define o comportamento, propósito e arquitetura do assistente virtual.

### Caso de Uso
O agente auxilia pessoas físicas na organização financeira pessoal, oferecendo diagnósticos, análises e recomendações com base nas informações fornecidas pelo usuário.

### Problemas Resolvidos
* Falta de controle financeiro e fuga de moedas com supérfluos;
* Ausência de planejamento para reserva de emergência;
* Gastos excessivos acima dos 30% recomendados pela regra 50/30/20;
* Dificuldade em escolher onde guardar o dinheiro com segurança;
* Dificuldade em atingir metas financeiras de médio e longo prazo.

### Persona
O Tio Patinhas é um mentor financeiro virtual experiente, econômico, protetor do cofre e bem-humorado.

### Tom de Voz
Amigável, educativo e levemente "mão de vaca".

Exemplos:
> *"Nosso cofre levou um susto com esse gasto com delivery!"*  
> *"Gostei dessa economia! Mais moedas protegidas no Tesouro Selic."*  
> *"Será que precisamos mesmo de mais uma saída no fim de semana?"*

### Segurança e Anti-Alucinação
O agente segue regras rígidas para evitar alucinações:
* Nunca inventar valores numéricos;
* Solicitar dados ausentes antes de emitir o parecer;
* Explicar detalhadamente os cálculos realizados (regra 50/30/20);
* Informar limitações quando necessário;
* Não fornecer aconselhamento financeiro profissional de alto risco sem reserva de emergência blindada.

📄 **Documento:** `docs/01-documentacao-agente.md`

---

## 2. Base de Conhecimento

A base de conhecimento é responsável por fornecer contexto financeiro real e estruturado ao agente.

### Dados Utilizados

| Arquivo | Formato | Descrição |
| :--- | :--- | :--- |
| `perfil_usuario.json` | JSON | Cadastro do usuário, renda mensal, metas e saldo guardado no cofre |
| `cofres_e_investimentos.json` | JSON | Catálogo de produtos/cofres seguros (Selic, CDB, LCI, Fundos) com descrições didáticas |
| `extrato_transacoes.csv` | CSV | Extrato com histórico de transações e classificação (Essencial, Desejo, Futuro) |
| `historico_consultas.json` | JSON | Registro de atendimentos anteriores e conselhos já fornecidos |

### Conhecimentos Incorporados
* Regra 50/30/20 (50% Necessidades, 30% Desejos, 20% Futuro);
* Conceito de Reserva de Emergência (6 meses de custo fixo);
* Alocação em Cofres de Baixo Risco e Liquidez Imediata;
* Diagnóstico de Saúde e Maturidade Financeira.

📄 **Documento:** `docs/02-base-conhecimento.md`

---

## 3. Prompts do Agente

Define o comportamento e as regras que orientam a Inteligência Artificial.

### Prompt Principal
O agente deve:
* Solicitar informações faltantes quando necessário;
* Analisar entradas e saídas do extrato;
* Classificar gastos automaticamente;
* Gerar diagnósticos financeiros embasados;
* Aplicar a regra 50/30/20;
* Emitir alertas sobre desperdícios e recomendar cofres seguros.

### Estrutura Obrigatória das Respostas
Sempre apresentar:
* 📊 Raio-X Financeiro
* 🏆 Nota de Saúde Financeira (0 a 100)
* 🌱 Nível de Maturidade Financeira (Sobrevivência, Organização, Estabilidade, Crescimento ou Liberdade)
* ⚠️ Alertas do Cofre
* 💡 Dicas do Tio Patinhas
* 🎯 Missão dos Próximos 30 Dias

📄 **Documento:** `docs/03-prompts.md`

---

## 4. Aplicação Funcional

Protótipo funcional desenvolvido em Python para interação em tempo real com o usuário.

### Funcionalidades
* Dashboard visual com cards de métricas (Renda, 50/30/20, Saldo Livre);
* Tabela interativa para visualização e filtragem do extrato financeiro;
* Chat financeiro inteligente com diagnósticos instantâneos do Tio Patinhas;
* Recomendações personalizadas de cofres baseadas no perfil do cliente.

### Tecnologias Utilizadas
* **Python 3.10+**
* **Streamlit** (Interface Web Interativa)
* **Pandas** (Manipulação e Análise de Dados)
* **OpenAI API / Google Gemini API** (LLM Generativa)
* **Python-Dotenv** (Gerenciamento de Variáveis de Ambiente)

📁 **Código:** `src/app.py` | `src/agente.py` | `src/config.py` | `src/requirements.txt`

---

## 5. Avaliação e Métricas

O projeto avalia a qualidade e a segurança das respostas geradas pelo agente.

### Métricas de Qualidade

| Métrica | Objetivo |
| :--- | :--- |
| **Precisão** | Cálculos e percentuais da regra 50/30/20 totalmente coerentes com o extrato |
| **Clareza** | Facilidade de entendimento sem uso de jargões bancários complexos |
| **Utilidade** | Capacidade de gerar ações práticas para os próximos 30 dias |
| **Segurança** | Ausência total de informações inventadas ou promessas irrealistas |
| **Consistência** | Manutenção contínua da personalidade pão-duro e educativa do Tio Patinhas |

### Critérios de Aprovação
* Resposta financeiramente coerente com os dados de `data/`;
* Cálculos matemáticos 100% corretos;
* Recomendações justificadas por dados reais;
* Linguagem acessível e motivadora.

📄 **Documento:** `docs/04-metricas.md`

---

## 6. Pitch (3 minutos)

Apresentação resumida do projeto, proposta de valor e demonstração da solução.

### O Problema
Grande parte das pessoas não possui controle financeiro adequado, acumula gastos supérfluos sem perceber e enfrenta dificuldades para organizar despesas e criar uma reserva de emergência.

### A Solução
O Tio Patinhas atua como um mentor financeiro virtual baseado em IA, capaz de analisar dados financeiros reais e fornecer orientações personalizadas de forma simples, prática e divertida.

### Diferenciais
Além da análise financeira tradicional, o agente possui uma personalidade única e entrega:
* Raio-X Financeiro Inteligente;
* Nota de Saúde Financeira (0 a 100);
* Sistema de Nível de Maturidade Financeira;
* Alertas do Cofre em tempo real;
* Missão Prática de 30 Dias.

📄 **Documento:** `docs/05-pitch.md`

---

# Arquitetura da Solução

```mermaid
flowchart TD
    A[Usuário / Cliente] -->|Consulta & Perguntas| B[Interface Streamlit / app.py]
    B --> C[Motor de Análise / agente.py]
    C --> D[Base de Conhecimento / data/]
    D --> E[Cálculo Regra 50/30/20 & Contexto]
    E --> F[Processamento LLM]
    F --> G[Validação Anti-Alucinação]
    G --> H[Raio-X + Diagnóstico + Missão 30 Dias]

    tio-patinhas-finance-ai/
├── 📄 README.md
│
├── 📁 data/
│   ├── 📄 perfil_usuario.json          # Dados do usuário, renda e metas
│   ├── 📄 cofres_e_investimentos.json  # Catálogo de cofres/produtos de investimento
│   ├── 📄 extrato_transacoes.csv       # Extrato com classificação de receitas e gastos
│   └── 📄 historico_consultas.json     # Histórico de conversas e orientações passadas
│
├── 📁 docs/
│   ├── 📄 01-documentacao-agente.md    # Persona, tom de voz e regras de segurança
│   ├── 📄 02-base-conhecimento.md      # Descrição e integração da base de dados
│   ├── 📄 03-prompts.md                # System prompt e exemplos de cenários
│   ├── 📄 04-metricas.md               # Critérios de teste, qualidade e segurança
│   └── 📄 05-pitch.md                  # Roteiro do vídeo de apresentação (3 min)
│
└── 📁 src/
    ├── 📄 app.py                       # Interface principal web em Streamlit
    ├── 📄 agente.py                    # Lógica de cálculo 50/30/20 e integração LLM
    ├── 📄 config.py                    # Configuração de caminhos e chaves de API
    └── 📄 requirements.txt             # Dependências da aplicação Python
