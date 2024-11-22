from TipoFontes import TipoFonte
from TipoFontesRepositorioDB import TipoFontesRepositorioDB

class TipoFontesControl:
    repositorio = TipoFontesRepositorioDB()

    def cadastrar (self, tipofonte : TipoFonte):
        return self.repositorio.cadastrarFonte( tipofonte )
    def pesquisar_por_nome(self, nome : str) -> list:
        return self.repositorio.pesquisar_por_nome( nome )
    def atualizar (self, id_tipo_fonte : int, tipofonte : TipoFonte):
        return self.repositorio.atualizar(id_tipo_fonte, tipofonte)
    def remover (self, id_tipo_fonte : int):
        return self.repositorio.remover(id_tipo_fonte)