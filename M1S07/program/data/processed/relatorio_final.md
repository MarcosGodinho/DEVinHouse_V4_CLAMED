
# Relatório Final - Análise CLAMED Healthcare Dataset

**Projeto:** Mini Projeto CLAMED**Data:** 2025**Analista:** Marcos Godinho

---

## 1. Resumo Executivo

Este relatório apresenta os principais insights obtidos da análise exploratória do dataset de saúde CLAMED, composto originalmente por **55.500 registros** de pacientes. Após limpeza (remoção de duplicados e outliers), trabalhamos com **54,966 registros válidos**.

**Principais descobertas:**
- Todas as condições médicas têm custos próximos (CV=0.33%)
- Correlação muito fraca (praticamente inexistente) entre 'Idade' vs 'Custo Total' (r = -0.0034)
- Diferença entre custo de internações emergenciais e eletivas: -0.42%
- Adultos (18+) correspondem a 99.79% dos registros

---

## 2. Principais Padrões Identificados

### 2.1. Custo por Condição Médica (Figura 1)

**Observações:**
- **Todas** as doenças têm valores muito próximos (CV = 0.33%)
- Obesity lidera com média de $26k
- Variação total entre condições: apenas $652

**Hipótese:** O dataset pode estar balanceado artificialmente ou os custos são padronizados por convênios médicos.

**Recomendação:** Investigar protocolos de precificação das seguradoras.

### 2.2. Relação Idade × Custo (Figura 2)

**Observações:**
- A correlação idade-custo é **muito fraca (praticamente inexistente)** (r = -0.0034, p = 4.2176e-01)
- Admissões **Emergency** mostram menor dispersão de custos
- Tendências lineares são horizontais em todos os tipos

**Comportamento inesperado:**
Esperava-se maior custo com o aumento da idade, mas não foi observado padrão claro.

**Hipótese:** A idade não é um fator determinante para os custos. O tipo de condição médica tem maior influência.

### 2.3. Custos por Gênero e Faixa Etária (Figura 4)

**Observações:**
- **Adultos** apresentam mediana de custo 15.02% **inferior** a crianças
- Diferença entre gêneros é **mínima** (0.55%)
- Menor variabilidade de custos ocorre em adultos

**Recomendação:**
- Investigar causas dos custos diferenciados em pediatria
- Analisar baixa variabilidade de custos entre gêneros

---

## 3. Comportamentos Inesperados

1. **Ausência de correlação idade-custo:** Contraria a expectativa de aumento de custos com envelhecimento
2. **Homogeneidade entre gêneros:** Custos praticamente idênticos entre homens e mulheres (0.55%)
3. **Custos pediátricos inferiores:** Crianças têm custos 15.02% menores que adultos
4. **Homogeneidade entre condições:** Todas as doenças têm custos semelhantes (CV 0.33%)

---

## 4. Hipóteses para Investigações Futuras

### 4.1. Modelagem Preditiva
- Desenvolver modelo de **regressão** para prever custos com base em:
  - Condição médica
  - Tipo de admissão
  - Tempo de internação
  - Resultado de testes

### 4.2. Análise de Segmentação
- Aplicar **clustering** para identificar perfis de pacientes de alto custo
- Segmentar por combinações de condições médicas

### 4.3. Análise Temporal
- Investigar sazonalidade nos custos (por mês/trimestre)
- Avaliar tempo de internação vs custo total

### 4.4. Análise de Seguradoras
- Comparar custos médios entre Insurance Providers
- Identificar discrepâncias e oportunidades de negociação

---

## 5. Action Items e Recomendações

| # | Ação | Prioridade | Responsável Sugerido |
|---|------|-----------|---------------------|
| 1 | Investigar padrão de precificação das seguradoras | Alta | Financeiro |
| 2 | Analisar causas de custos diferenciados em pediatria | Média | Diretoria Médica |
| 3 | Desenvolver modelo preditivo de custos | Média | Equipe Data Science |
| 4 | Revisar variabilidade de custos em adultos | Média | Auditoria Médica |
| 5 | Validar qualidade dos dados coletados | Alta | TI/Qualidade |

---

## 6. Conclusão

A análise revelou padrões **surpreendentemente homogêneos** nos custos:
- Idade não apresenta correlação significativa com custos
- Adultos e crianças têm custos similares
- A padronização de custos sugere forte influência de protocolos de seguradoras

Recomenda-se focar esforços em:

1. **Validação de dados** (homogeneidade pode indicar limitações no dataset)
2. **Análise pediátrica** (validar padrões encontrados)
3. **Modelagem preditiva** com variáveis adicionais (tempo de internação, procedimentos)

---

**Estatísticas-Chave:**
- Total de registros analisados: 54,966
- Correlação idade-custo: r = -0.0034 (MUITO FRACA (praticamente inexistente))
- CV entre condições: 0.33%
- Diferença Emergency vs Elective: -0.42%
- Diferença Adult vs Children: -15.02%
- Diferença entre gêneros: 0.55%

**Artefatos Gerados:**
- `data/processed/healthcare_cleaned.csv` - Dataset limpo e enriquecido
- `data/figures/relatorio_fig*.png` - Visualizações chave
- `mini_projeto_clamed.ipynb` - Notebook completo com análises
