class TipoFonte:
    id_tipo_fonte : int
    nome : str

    def __init__(self, id_tipo_fonte : int = 0, nome : str = ""):
        self.id_tipo_fonte = id_tipo_fonte
        self.nome = nome

    def __str__(self):
        return f"ID: {self.id_tipo_fonte}\tNome: {self.nome}"
    
    def from_dict(self, dicionario_tipo):
        self.id_tipo_fonte = dicionario_tipo.get("id", "")
        self.nome = dicionario_tipo.get("nome","")
    
    def to_dict(self) -> dict:
        dicionario_tipo = {}
        dicionario_tipo["id"] = self.id_tipo_fonte
        dicionario_tipo["nome"] = self.nome
        return dicionario_tipo

if __name__ == "__main__":
    t1 = TipoFonte()
    t1.from_dict( {"id": 0, "nome": "Carvão"} )
    print (f"TipoFonte: {t1.to_dict()}")