import os
from decimal import Decimal
from TipoFontes import TipoFonte
from TipoFontesControl import TipoFontesControl
from Emissoes import EmissoesCarbono
from EmissoesControl import EmissoesControl

class Boundary:

    tipo_fontes_control = TipoFontesControl()
    emissoes_control = EmissoesControl()

    def __init__(self):
        pass

    def cadastrar_tipo_fonte(self):
        fonte = self.pegar_dados_tipo_fonte()
        self.tipo_fontes_control.cadastrar(fonte)

    def pesquisar_tipo_fonte(self):
        nome = input("Informe o nome do tipo de fonte a ser pesquisado: ")
        lista_fontes = self.tipo_fontes_control.pesquisar_por_nome(nome)
        for fonte in lista_fontes:
            print(fonte)
            print("-" * 80)

    def atualizar_tipo_fonte(self):
        id_tipo_fonte = int(input("Informe o ID do tipo de fonte a ser atualizado: "))
        print("Informe os novos dados para o tipo de fonte:")
        fonte = self.pegar_dados_tipo_fonte()
        self.tipo_fontes_control.atualizar(id_tipo_fonte, fonte)

    def remover_tipo_fonte(self):
        id_tipo_fonte = int(input("Informe o ID do tipo de fonte a ser removido: "))
        self.tipo_fontes_control.remover(id_tipo_fonte)

    def pegar_dados_tipo_fonte(self):
        fonte = TipoFonte()
        valido = False
        while not valido:
            fonte.nome = input("Digite o nome do tipo de fonte: ")
            if fonte.nome == "":
                print("O nome precisa ser preenchido.")
                input("Tecle <ENTER> para continuar")
            else:
                valido = True
        return fonte

    def cadastrar_emissao(self):
        emissao = self.pegar_dados_emissao()
        self.emissoes_control.cadastrar(emissao)

    def pesquisar_emissoes_por_tipo_fonte(self):
        id_tipo_fonte = int(input("Informe o ID do tipo de fonte para pesquisar emissões: "))
        lista_emissoes = self.emissoes_control.pesquisar_por_tipo_fonte(id_tipo_fonte)
        for emissao in lista_emissoes:
            print(emissao)
            print("-" * 80)

    def mostrar_maior_emissao(self):
        maior_emissoes = self.emissoes_control.pesquisar_maior_emissao()
        for emissao in maior_emissoes:
            print(f"Maior Emissão: {emissao}")
            print("-" * 80)

    def mostrar_menor_emissao(self):
        menor_emissoes = self.emissoes_control.pesquisar_menor_emissao()
        for emissao in menor_emissoes:
            print(f"Menor Emissão: {emissao}")
            print("-" * 80)

    def mostrar_media_emissao(self):
        media = self.emissoes_control.calcular_media_emissao()
        print(f"Média das Emissões: {media}")

    def atualizar_emissao(self):
        id_emissao = int(input("Informe o ID da emissão a ser atualizada: "))
        print("Informe os novos dados para a emissão:")
        emissao = self.pegar_dados_emissao()
        self.emissoes_control.atualizar(id_emissao, emissao)

    def remover_emissao(self):
        id_emissao = int(input("Informe o ID da emissão a ser removida: "))
        self.emissoes_control.remover(id_emissao)

    def pegar_dados_emissao(self):
        tipo_fonte = TipoFonte(
            id_tipo_fonte=int(input("Digite o ID do tipo de fonte: ")),
            nome=None
        )
        emissao_valor = Decimal(input("Digite o valor da emissão: "))
        return EmissoesCarbono(tipo_fonte=tipo_fonte, emissao=emissao_valor)

    def mostrar_menu(self):
        opcao_valida = False
        while not opcao_valida:
            os.system("cls")
            print("M E N U  P R I N C I P A L")
            print("(1) Gerenciar Tipo Fontes")
            print("(2) Gerenciar Emissões")
            print("(0) Sair")
            opcao = input("Informe sua opção ==> ")
            if opcao.isdigit():
                escolha = int(opcao)
                match escolha:
                    case 1: self.mostrar_menu_tipo_fontes()
                    case 2: self.mostrar_menu_emissoes()
                    case 0:
                        print("Saindo...")
                        opcao_valida = True
                    case _:
                        print("Opção inválida.")
            else:
                print("Opção inválida.")
            input("Tecle <ENTER> para continuar")

    def mostrar_menu_tipo_fontes(self):
        opcao_valida = False
        while not opcao_valida:
            os.system("cls")
            print("M E N U  -  T I P O  F O N T E S")
            print("(1) Cadastrar um novo tipo de fonte")
            print("(2) Pesquisar tipos de fonte pelo nome")
            print("(3) Atualizar tipo de fonte pelo ID")
            print("(4) Remover tipo de fonte pelo ID")
            print("(0) Voltar")
            opcao = input("Informe sua opção ==> ")
            if opcao.isdigit():
                escolha = int(opcao)
                match escolha:
                    case 1: self.cadastrar_tipo_fonte()
                    case 2: self.pesquisar_tipo_fonte()
                    case 3: self.atualizar_tipo_fonte()
                    case 4: self.remover_tipo_fonte()
                    case 0: self.mostrar_menu()
                    case _:
                        print("Opção inválida.")
            else:
                print("Opção inválida.")
            input("Tecle <ENTER> para continuar")

    def mostrar_menu_emissoes(self):
        opcao_valida = False
        while not opcao_valida:
            os.system("cls")
            print("M E N U  -  E M I S S Õ E S")
            print("(1) Cadastrar uma nova emissão")
            print("(2) Pesquisar emissões pelo tipo de fonte")
            print("(3) Mostrar maior emissão")
            print("(4) Mostrar menor emissão")
            print("(5) Mostrar média das emissões")
            print("(6) Atualizar uma emissão pelo ID")
            print("(7) Remover uma emissão pelo ID")
            print("(0) Voltar")
            opcao = input("Informe sua opção ==> ")
            if opcao.isdigit():
                escolha = int(opcao)
                match escolha:
                    case 1: self.cadastrar_emissao()
                    case 2: self.pesquisar_emissoes_por_tipo_fonte()
                    case 3: self.mostrar_maior_emissao()
                    case 4: self.mostrar_menor_emissao()
                    case 5: self.mostrar_media_emissao()
                    case 6: self.atualizar_emissao()
                    case 7: self.remover_emissao()
                    case 0: self.mostrar_menu()
                    case _:
                        print("Opção inválida.")
            else:
                print("Opção inválida.")
            input("Tecle <ENTER> para continuar")
