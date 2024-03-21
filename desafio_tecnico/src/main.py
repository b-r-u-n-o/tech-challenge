from utils import (
    ConnectMySQL, 
    DotEnvVars, 
    ReadMySQL,
    WriteMySQL
)
from planner import DataWarehouseSql 

def run():
    
    try:
        # Carrega variáveis de ambiente
        env = DotEnvVars()

        # criar conexão para ler dados do mysql com sqlalchemy
        conn = ConnectMySQL(
            db_name= env.get_var('MYSQL_DATABASE'),
            user_name= env.get_var('MYSQL_USERNAME'),
            password= env.get_var('MYSQL_PASSWORD'),
            host= env.get_var('MYSQL_HOST'),
            port= env.get_var('MYSQL_PORT')
        ).engine()
    
    except Exception as e:
        print(f"Erro ao conectar ao MySQL: {e}")

    try:
        # Realiza a leitura dos dados para o DW
        print("Carregando dados do MySQL...")

        # ler dados das tabelas do mysql
        reader = ReadMySQL(con = conn)
        dw = DataWarehouseSql()

        df_dim_products = reader.read_query(dw.dim_products())
        df_dim_orders = reader.read_query(dw.dim_orders())
        df_dim_customers = reader.read_query(dw.dim_customers())
        df_dim_employees = reader.read_query(dw.dim_employees())
        df_dim_offices = reader.read_query(dw.dim_offices())
        df_dim_time = reader.read_query(dw.dim_time())
        df_fact_sales = reader.read_query(dw.fact_sales())

        print("Dados carregados com sucesso!")
    
    except Exception as e:
        print(f"Erro ao carregar dados do MySQL: {e}")

            
    try:
        print("Criação das tabelas do DW inicializada...")         
        writer = WriteMySQL(con = conn)
        
        # Dimensão de tempo
        writer.write_table(df = df_dim_time, table_name = 'dim_time')
        print("Tabela dim_time carregada com sucesso!")

        # Dimensão de produto
        writer.write_table(df = df_dim_products, table_name = 'dim_products')
        print("Tabela dim_products carregada com sucesso!")

        writer.write_table(df = df_dim_orders, table_name = 'dim_orders')
        print("Tabela dim_orders carregada com sucesso!")

        # Dimensão de clientes
        writer.write_table(df = df_dim_customers, table_name = 'dim_customers') 
        print("Tabela dim_customers carregada com sucesso!")

        # Dimensão de funcionários
        writer.write_table(df = df_dim_employees, table_name = 'dim_employees') 
        print("Tabela dim_employees carregada com sucesso!")

        # Dimensão de escritórios
        writer.write_table(df = df_dim_offices, table_name = 'dim_offices')
        print("Tabela dim_offices carregada com sucesso!")

        # Fato de vendas
        writer.write_table(df = df_fact_sales, table_name = 'fact_sales')
        print("Tabela fact_sales carregada com sucesso!")

        print("Tabelas do DW criadas com sucesso!")

    except Exception as e:
        print(f"Erro ao criar DW: {e}")
    
    print("Processo finalizado com sucesso!")

    

if __name__ == "__main__":
    run()