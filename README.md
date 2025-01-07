# ETL Pipeline: Projeto de Vendas

Este repositório contém um pipeline ETL (Extract, Transform, Load) desenvolvido para processar dados de vendas. O objetivo é extrair os dados brutos, transformá-los conforme as regras de negócios e carregá-los em um banco de dados na nuvem, utilizando ferramentas modernas e escaláveis.

## Objetivo do Projeto

O objetivo deste projeto é construir um pipeline ETL robusto para processar e analisar dados de vendas. Ele cobre todas as etapas do ETL:

1. **Extração**: Coleta de dados de um arquivo CSV com informações de vendas.
2. **Transformação**: Aplicação de cálculos e categorização dos dados, incluindo:
   - Cálculo de receita total por venda.
   - Classificação dos preços em categorias ("Low", "Medium", "High").
3. **Carregamento**: Armazenamento dos dados transformados em um banco de dados na nuvem (Google BigQuery).

## Tecnologias Utilizadas

- **Python**: Linguagem principal para o desenvolvimento do pipeline.
- **Apache Spark**: Processamento distribuído de grandes volumes de dados.
- **Pandas**: Manipulação de dados em memória.
- **Google BigQuery**: Armazenamento e análise de dados na nuvem.
- **Git**: Controle de versão do código.
- **VSCode**: Ambiente de desenvolvimento integrado.

## Estrutura do Repositório

- `data_generation/`: Contém o script de para ageração de dados ficitícios de vendas.
- `data_loading/`: Contém o script para carregar dados no BigQuery.
- `data_transformation/`: Contém o script de transformação e os dados transformados.
- `sales_data.csv`: Dados de vendas brutos fictícios.
- `README.md`: Documentação do projeto.
