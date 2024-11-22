import oracledb
from oracledb import Connection
import os
from TipoFontes import TipoFonte

class TipoFontesRepositorioDB:
    def __init__(self):
        self.usuario = os.environ.get("FIAP_ORACLE_USER")
        self.senha = os.environ.get("FIAP_ORACLE_PASS")
        self.db_path = "oracle.fiap.com.br:1521/orcl"
    
    def gerar_conexao(self) -> Connection:
        con = oracledb.connect(
            user = self.usuario,
            password = self.senha,
            dsn = self.db_path
        )
        return con
    
    def cadastrarFonte(self, tipofonte : TipoFonte) -> bool:
        conexao = self.gerar_conexao()
        cursor = conexao.cursor()
        sql = """INSERT INTO Tipo_Fontes (id_tipo_fonte, nome) VALUES (:1, :2)"""
        try:
            cursor.execute(sql, (tipofonte.id_tipo_fonte, tipofonte.nome))
            conexao.commit()
        except Exception:
            conexao.rollback()
            return False
        conexao.close()
        return True
    
    def pesquisar_por_nome(self, nome : str) -> list:
        conexao = self.gerar_conexao()
        cursor = conexao.cursor()
        sql = """SELECT * FROM Tipo_Fontes WHERE nome LIKE :1"""
        cursor.execute(sql, ("%" + nome + "%", ))
        resultado = []
        for dados in cursor:
            t1 = TipoFonte(id_tipo_fonte=dados[0],
                           nome= dados[1])
            resultado.append(t1)
        conexao.close()
        return resultado
    
    def remover(self, id_tipo_fonte : int) ->bool:
        conexao = self.gerar_conexao
        cursor = conexao.cursor()
        sql = """DELETE FROM Tipo_Fontes WHERE id_tipo_fonte = :1"""
        try:
            cursor.execute(sql, (id_tipo_fonte, ))
            conexao.commit()
        except Exception:
            conexao.rollback()
            return False
        conexao.close()
        return True
    
    def atualizar(self, id_tipo_fonte : int, tipofonte :TipoFonte) -> bool:
        conexao = self.gerar_conexao()
        cursor = conexao.cursor()
        sql = """UPDATE Tipo_Fontes SET nome = :1 WHERE id_tipo_fonte :2"""
        try:
            cursor.execute(sql, (tipofonte.nome, tipofonte.id_tipo_fonte))
            conexao.commit()
        except Exception:
            conexao.rollback()
            return False
        conexao.close()
        return True