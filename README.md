# 📊 Data Warehouse Project

## 📝 Descrição

Este projeto tem como objetivo desenvolver um Data Warehouse para resolver um desafio técnico. É a solução perfeita para analisar, entender e descobrir insights a partir de grandes volumes de dados. 🚀

## 🏗 Estrutura do Projeto

### Tabelas de Dimensão 📐

- `dim_products`: Contém informações sobre os produtos, como código, nome, fornecedor e descrição. 📦
- `dim_customers`: Armazena dados dos clientes, incluindo número do cliente, nome, contato e endereço. 🧑‍💼
- `dim_employees`: Inclui detalhes dos empregados, como número do empregado, nome completo e cargo. 👨‍💼
- `dim_offices`: Registra informações sobre os escritórios, como código do escritório, cidade, estado e país. 🏢
- `dim_time`: Uma dimensão de tempo com detalhes até o nível de dia. ⏳

### Tabela Fato 📊

- `FactSales`: Tabela fato principal que registra as vendas, relacionando-se com as dimensões acima. Inclui métricas como receita do item, percentual de markup, taxa de conversão de estoque e variação de preço em relação ao MSRP. 💹

## 🛠 Tecnologias Utilizadas

- Banco de dados: MySQL
  - Microserviço:
    - Docker 🐳
    - Docker Compose
  - DBeaver Community 🦦
- Ferramenta ETL: Python 🐍
  - Pandas 🐼
  - SQLAlchemy
  - DuckDB
  - Dotenv

## ⚙️ Configuração e Instalação

1. **Banco de Dados**:
   - Instale o MySQL e crie um banco de dados chamado `ctbz`.

   ```bash   
   # Na raiz do projeto execute
   cd microservices
   docker-compose up -d  
   ``` 
2. **Python** 🐍:
   - Para instalar as dependências, você precisará do Poetry ou similar.

   ``` bash
   poetry install
   ```
   - Em seguida, execute com o Python o script `main.py` para criar as tabelas de dimensão e fato.


**Licença** 📜
Este projeto está sob a Licença MIT. Confira o arquivo LICENSE para mais detalhes.