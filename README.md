# Projeto: Análise de Dados — DEVinHouse (SENAI)

Descrição
- Projeto desenvolvido durante o curso DEVinHouse do SENAI para aprender técnicas básicas de análise de dados em Python.
- Processa entradas em `JSON` e `CSV`, faz limpeza e gera relatórios/exportações (ex.: `produtos.csv`, planilhas Excel).

Estrutura principal
- `M1S04/aula_17102025/desafio_final_semana/main.ipynb` — notebook principal com o fluxo de leitura, limpeza e integração.
- Arquivos de dados de exemplo: `dados.json`, `produtos.csv`, outros CSVs usados para vendas.

Como executar (Windows)
1. Criar ambiente virtual:
   - `python -m venv venv`
   - `venv\Scripts\activate`
2. Instalar dependências:
   - `pip install -r requirements.txt`
   - ou `pip install openpyxl` (se não houver `requirements.txt`)
3. Abrir `main.ipynb` no PyCharm ou Jupyter Notebook e executar as células.

Dependências principais
- `openpyxl`
- bibliotecas padrão: `json`, `csv`, `re`, `datetime`

Observações
- O notebook inclui funções de leitura (`ler_json`, `ler_csv`), limpeza de nomes (`limpar_nome_filiais`) e filtragem de registros inválidos.
- Verifique caminhos relativos quando executado no PyCharm para garantir que os arquivos gerados apareçam na pasta do projeto.

Licença
- Arquivo de licença não incluído. Adicionar `LICENSE` conforme desejado.
