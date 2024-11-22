from decimal import Decimal
from TipoFontes import TipoFonte

class EmissoesCarbono:
    id_emissao: int
    id_tipo_fonte: int
    emissao: Decimal

    def __init__(self, id_emissao: int = 0, tipo_fonte: TipoFonte = None, emissao: Decimal = Decimal("0")):
        self.id_emissao = id_emissao
        self.id_tipo_fonte = tipo_fonte.id_tipo_fonte
        self.emissao = emissao

    def __str__(self):
        return f"Emissão ID: {self.id_emissao}\tTipo Fonte ID: {self.id_tipo_fonte}\tEmissão: {self.emissao}"

    def from_dict(self, dicionario_emissao: dict, tipo_fonte: TipoFonte = None) -> None:
        self.id_emissao = dicionario_emissao.get("id_emissao", 0)
        self.id_tipo_fonte = tipo_fonte.id_tipo_fonte if tipo_fonte else dicionario_emissao.get("id_tipo_fonte", 0)
        self.emissao = Decimal(dicionario_emissao.get("emissao", "0"))

    def to_dict(self) -> dict:
        return {
            "id_emissao": self.id_emissao,
            "id_tipo_fonte": self.id_tipo_fonte,
            "emissao": str(self.emissao)
        }

if __name__ == "__main__":
    tipo_fonte_example = TipoFonte(id_tipo_fonte=1, nome="Carvão")

    emissao = EmissoesCarbono(id_emissao=101, tipo_fonte=tipo_fonte_example, emissao=Decimal("1234.56"))
    print(emissao)

    print("Dicionário:", emissao.to_dict())
