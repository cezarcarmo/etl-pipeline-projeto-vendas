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

- `data_generation/`: Contém o script de geração de dados fictícios de vendas.
  - [`generate_sales_data.py`](data_generation/generate_sales_data.py)
- `data_loading/`: Contém o script para carregar dados no BigQuery.
  - [`to_big_query.py`](data_loading/to_big_query.py)
- `data_transformation/`: Contém o script de transformação e os dados transformados.
  - [`transform_sales_data.py`](data_transformation/transform_sales_data.py)
  - `transformed_data/`: Contém os dados transformados.
    - [`transformed_sales_data.csv`](data_transformation/transformed_data/transformed_sales_data.csv)
- [`sales_data.csv`](sales_data.csv): Dados de vendas brutos fictícios.
- [`README.md`](README.md): Documentação do projeto.
- [`requirements.txt`](requirements.txt): Dependências do projeto.

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/etl-pipeline-projeto-vendas.git
   cd etl-pipeline-projeto-vendas
   ```
2. Crie e ative um ambiente virtual:
   ```py
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
  	```

## Uso

1. Geração de Dados Fictícios:
   ```sh
   python data_generation/generate_sales_data.py
   ```
2. Transformação de Dados
   ```sh
   python data_transformation/transform_sales_data.py
   ```
3. Carregamento de Dados
   ```sh
   python data_loading/to_big_query.py
   ```
   
## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Responsável Técnico

Claro! Aqui está a atualização do seu 

README.md

 com seu nome e email incluídos como responsável pelo projeto:

```markdown
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

- `data_generation/`: Contém o script de geração de dados fictícios de vendas.
  - [`generate_sales_data.py`](data_generation/generate_sales_data.py)
- `data_loading/`: Contém o script para carregar dados no BigQuery.
  - [`to_big_query.py`](data_loading/to_big_query.py)
- `data_transformation/`: Contém o script de transformação e os dados transformados.
  - [`transform_sales_data.py`](data_transformation/transform_sales_data.py)
  - `transformed_data/`: Contém os dados transformados.
    - [`transformed_sales_data.csv`](data_transformation/transformed_data/transformed_sales_data.csv)
- [`sales_data.csv`](sales_data.csv): Dados de vendas brutos fictícios.
- [`README.md`](README.md): Documentação do projeto.
- [`requirements.txt`](requirements.txt): Dependências do projeto.

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/etl-pipeline-projeto-vendas.git
   cd etl-pipeline-projeto-vendas
   ```

2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Uso

1. Geração de Dados Fictícios:
   ```sh
   python data_generation/generate_sales_data.py
   ```
2. Transformação de Dados:
   ```sh
   python data_transformation/transform_sales_data.py
   ```
3. Carregamento de Dados:
   ```sh
   python data_loading/to_big_query.py
   ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Responsável

Projeto mantido por **Cézar Augusto Meira Carmo.** 

Para mais informações: **dataengineercezar@egmail.com**


