from decimal import Decimal
from Emissoes import EmissoesCarbono
from EmissoesRepositorioDB import EmissoesRepositorioDB

class EmissoesControl:
    repositorio = EmissoesRepositorioDB()

    def cadastrar(self, emissao: EmissoesCarbono):
        return self.repositorio.cadastrar_emissao(emissao)
    
    def pesquisar_por_tipo_fonte(self, id_tipo_fonte: int) -> list:
        return self.repositorio.pesquisar_por_tipo_fonte(id_tipo_fonte)
    
    def pesquisar_maior_emissao(self) -> list:
        return self.repositorio.pesquisar_maior_emissao()
    
    def pesquisar_menor_emissao(self) -> list:
        return self.repositorio.pesquisar_menor_emissao()
    
    def calcular_media_emissao(self) -> Decimal:
        return self.repositorio.calcular_media_emissao()
    
    def atualizar(self, id_emissao: int, emissao: EmissoesCarbono):
        return self.repositorio.atualizar(id_emissao, emissao)
    
    def remover(self, id_emissao: int):
        return self.repositorio.remover(id_emissao)