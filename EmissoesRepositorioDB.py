import oracledb
from oracledb import Connection
import os
from decimal import Decimal
from Emissoes import EmissoesCarbono
from TipoFontes import TipoFonte

class EmissoesRepositorioDB:
    def __init__(self):
        self.usuario = os.environ.get("FIAP_ORACLE_USER")
        self.senha = os.environ.get("FIAP_ORACLE_PASS")
        self.db_path = "oracle.fiap.com.br:1521/orcl"
    
    def gerar_conexao(self) -> Connection:
        con = oracledb.connect(
            user=self.usuario,
            password=self.senha,
            dsn=self.db_path
        )
        return con

    def cadastrar_emissao(self, emissao: EmissoesCarbono) -> bool:
        conexao = self.gerar_conexao()
        cursor = conexao.cursor()
        sql = """INSERT INTO Emissoes_Carbono (id_emissao, id_tipo_fonte, emissao) VALUES (:1, :2, :3)"""
        try:
            cursor.execute(sql, (emissao.id_emissao, emissao.id_tipo_fonte, emissao.emissao))
            conexao.commit()
        except Exception:
            conexao.rollback()
            return False
        conexao.close()
        return True

    def pesquisar_por_tipo_fonte(self, id_tipo_fonte: int) -> list:
        conexao = self.gerar_conexao()
        cursor = conexao.cursor()
        sql = """SELECT * FROM Emissoes_Carbono WHERE id_tipo_fonte = :1"""
        cursor.execute(sql, (id_tipo_fonte,))
        resultado = []
        for dados in cursor:
            emissao = EmissoesCarbono(
                id_emissao=dados[0],
                tipo_fonte=TipoFonte(id_tipo_fonte=dados[1]),
                emissao=Decimal(dados[2])
            )
            resultado.append(emissao)
        conexao.close()
        return resultado
    
    def pesquisar_maior_emissao(self) -> list:
        conexao = self.gerar_conexao()
        cursor = conexao.cursor()
        sql = """
        SELECT * FROM Emissoes_Carbono 
        WHERE emissao = (SELECT MAX(emissao) FROM Emissoes_Carbono)
        """
        cursor.execute(sql)
        resultado = []
        for dados in cursor:
            emissao = EmissoesCarbono(
                id_emissao=dados[0],
                tipo_fonte=TipoFonte(id_tipo_fonte=dados[1]),
                emissao=Decimal(dados[2])
            )
            resultado.append(emissao)
        conexao.close()
        return resultado
    
    def pesquisar_menor_emissao(self) -> list:
        conexao = self.gerar_conexao()
        cursor = conexao.cursor()
        sql = """
        SELECT * FROM Emissoes_Carbono 
        WHERE emissao = (SELECT MIN(emissao) FROM Emissoes_Carbono)
        """
        cursor.execute(sql)
        resultado = []
        for dados in cursor:
            emissao = EmissoesCarbono(
                id_emissao=dados[0],
                tipo_fonte=TipoFonte(id_tipo_fonte=dados[1]),
                emissao=Decimal(dados[2])
            )
            resultado.append(emissao)
        conexao.close()
        return resultado
    
    def calcular_media_emissao(self) -> Decimal:
        conexao = self.gerar_conexao()
        cursor = conexao.cursor()
        sql = """SELECT AVG(emissao) FROM Emissoes_Carbono"""
        cursor.execute(sql)
        resultado = cursor.fetchone()
        conexao.close()
        if resultado and resultado[0] is not None:
            return Decimal(resultado[0])
        return Decimal("0")

    def remover(self, id_emissao: int) -> bool:
        conexao = self.gerar_conexao()
        cursor = conexao.cursor()
        sql = """DELETE FROM Emissoes_Carbono WHERE id_emissao = :1"""
        try:
            cursor.execute(sql, (id_emissao,))
            conexao.commit()
        except Exception:
            conexao.rollback()
            return False
        conexao.close()
        return True

    def atualizar(self, id_emissao: int, emissao: EmissoesCarbono) -> bool:
        conexao = self.gerar_conexao()
        cursor = conexao.cursor()
        sql = """UPDATE Emissoes_Carbono SET id_tipo_fonte = :1, emissao = :2 WHERE id_emissao = :3"""
        try:
            cursor.execute(sql, (emissao.id_tipo_fonte, emissao.emissao, emissao.id_emissao))
            conexao.commit()
        except Exception:
            conexao.rollback()
            return False
        conexao.close()
        return True