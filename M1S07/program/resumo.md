# Relatório Final - Análise CLAMED Healthcare Dataset

**Projeto:** Mini Projeto CLAMED
**Data:** 2025
**Analista:** Marcos Godinho

---

## 1. Resumo Executivo

Este relatório apresenta os principais insights obtidos da análise exploratória do dataset de saúde CLAMED, composto originalmente por **55.500 registros** de pacientes. Após limpeza (remoção de duplicados e outliers), trabalhamos com **54.966 registros válidos**.

**Principais descobertas:**
- Todas as condições médicas têm custos próximos (~25.5k dólares, CV=0.87%)
- Correlação praticamente inexistente entre 'Idade' vs 'Custo Total' (r = -0.0034)
- Diferença insignificante entre custo de internações emergenciais e eletivas (0.42%)
- Adultos (18+) correspondem a 99.79% dos registros

---

## 2. Principais Padrões Identificados

### 2.1. Custo por Condição Médica (Figura 1)

**Observações:**
- **Todas** as doenças têm valores muito próximos (CV = 0.87%)
- Obesity lidera com média de $25,804
- Variação total entre condições: apenas $652 (2.5%)

**Hipótese:** O dataset pode estar balanceado artificialmente ou os custos são padronizados por convênios médicos.

**Recomendação:** Investigar protocolos de precificação das seguradoras.

### 2.2. Relação Idade × Custo (Figura 2)

**Observações:**
- A correlação idade-custo é **praticamente inexistente** (r = -0.0034, p > 0.05)
- Admissões **Emergency** mostram maior dispersão de custos
- Tendências lineares são horizontais em todos os tipos

**Comportamento inesperado:**
Esperava-se maior custo com o aumento da idade, mas não foi observado padrão claro.

**Hipótese:** O tipo de condição médica influencia mais que a idade. Crianças internadas tendem a ter casos mais graves/complexos, o que explica custos elevados mesmo com poucos casos.

### 2.3. Custos por Gênero e Faixa Etária (Figura 3)

**Observações:**
- **Crianças** apresentam mediana de custo 15% **superior** a adultos ($30,050 vs $25,537)
- Diferença entre gêneros é **mínima** (0.55%)
- Maior variabilidade de custos ocorre em adultos (CV = 55.64%)

**Recomendação:**
- Investigar causas dos custos elevados em pediatria
- Analisar alta variabilidade de custos em adultos (outliers ou casos complexos)

---

## 3. Comportamentos Inesperados

1. **Ausência de correlação idade-custo:** Contraria a expectativa de aumento de custos com envelhecimento
2. **Homogeneidade entre gêneros:** Custos praticamente idênticos entre homens e mulheres (0.55%)
3. **Custos pediátricos superiores:** Crianças têm custos 15% maiores que adultos
4. **Homogeneidade entre condições:** Todas as doenças têm custos semelhantes (CV < 1%)

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
| 2 | Analisar causas de custos elevados em pediatria | Alta | Diretoria Médica |
| 3 | Desenvolver modelo preditivo de custos | Média | Equipe Data Science |
| 4 | Revisar variabilidade de custos em adultos | Média | Auditoria Médica |
| 5 | Validar qualidade dos dados coletados | Alta | TI/Qualidade |

---

## 6. Conclusão

A análise revelou padrões **surpreendentemente homogêneos** nos custos:
- Idade, gênero e tipo de condição têm impacto limitado
- Crianças apresentam custos superiores, contrariando expectativas
- A padronização de custos sugere forte influência de protocolos de seguradoras

Recomenda-se focar esforços em:

1. **Validação de dados** (homogeneidade pode indicar limitações no dataset)
2. **Análise pediátrica** (compreender custos elevados)
3. **Modelagem preditiva** com variáveis adicionais (tempo de internação, procedimentos)

---

**Artefatos Gerados:**
- `data/processed/healthcare_cleaned.csv` - Dataset limpo e enriquecido
- `data/figures/relatorio_fig*.png` - Visualizações chave
- `mini_projeto_clamed.ipynb` - Notebook completo com análises