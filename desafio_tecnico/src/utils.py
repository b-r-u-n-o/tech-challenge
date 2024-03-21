import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv, find_dotenv


class ConnectMySQL:
    """
    Esta classe é responsável por estabelecer uma conexão com o banco de dados MySQL.
    """

    def __init__(self, db_name: str, user_name: str, password: str, host: str, port: int):
        """
        Inicializa a conexão com os parâmetros fornecidos.
        
        :param db_name: Nome do banco de dados.
        :param user_name: Nome de usuário para a conexão.
        :param password: Senha para a conexão.
        :param host: Host do servidor do banco de dados.
        :param port: Porta de conexão com o banco de dados.
        """
        self.db_name = db_name
        self.user_name = user_name
        self.password = password
        self.host = host
        self.port = port
    
    def engine(self):
        """
        Cria uma engine de conexão com o banco de dados.

        :return: Engine de conexão.
        """
        con = create_engine(f'mysql://{self.user_name}:{self.password}@{self.host}:{self.port}/{self.db_name}')
        return con
    

class ReadMySQL:
    """
    Esta classe é responsável pela leitura de dados do banco de dados MySQL.
    """

    def __init__(self, con: object):
        """
        Inicializa o objeto com a conexão fornecida.

        :param con: Conexão com o banco de dados.
        """
        self.con = con
    
    def read_query(self, query: str):
        """
        Executa uma consulta SQL e retorna os resultados em um DataFrame.

        :param query: Consulta SQL a ser executada.
        :return: DataFrame contendo os resultados da consulta.
        """
        df = pd.read_sql(query, self.con)
        return df
    

class WriteMySQL:
    """
    Esta classe é responsável pela escrita de dados no banco de dados MySQL.
    """

    def __init__(self, con: object):
        """
        Inicializa o objeto com a conexão fornecida.

        :param con: Conexão com o banco de dados.
        """
        self.con = con
    
    def write_table(self, df: pd.DataFrame, table_name: str):
        """
        Escreve um DataFrame no banco de dados em uma tabela específica.

        :param df: DataFrame a ser escrito no banco de dados.
        :param table_name: Nome da tabela onde o DataFrame será escrito.
        """
        df.to_sql(table_name, self.con, if_exists='replace', index=False)
    

class DotEnvVars:
    """
    Esta classe é responsável por carregar e obter variáveis de ambiente usando o arquivo .env.
    """

    def __init__(self):
        """
        Inicializa o objeto carregando as variáveis do arquivo .env.
        """
        self.load = load_dotenv(find_dotenv())

    def get_var(self, var_name: str):
        """
        Obtém o valor de uma variável de ambiente.

        :param var_name: Nome da variável de ambiente a ser obtida.
        :return: Valor da variável de ambiente.
        """
        var = os.getenv(var_name)
        return var
