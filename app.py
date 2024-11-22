from flask import Flask, request, jsonify
from flask_cors import CORS
from TipoFontes import TipoFonte
from TipoFontesControl import TipoFontesControl
from Emissoes import EmissoesCarbono
from EmissoesControl import EmissoesControl
from decimal import Decimal

app = Flask(__name__)
CORS(app) 

tipo_fontes_control = TipoFontesControl()
emissoes_control = EmissoesControl()

@app.route('/api/tipofontes', methods=['POST'])
def register_tipo_fonte():
    try:
        data = request.get_json()
        tipofonte = TipoFonte(
            id_tipo_fonte=data.get('id_tipo_fonte', 0),
            nome=data.get('nome', '')
        )
        success = tipo_fontes_control.cadastrar(tipofonte)
        if success:
            return jsonify({"message": "Tipo de Fonte cadastrado com sucesso!"}), 201
        else:
            return jsonify({"error": "Erro ao cadastrar Tipo de Fonte"}), 400
    except KeyError as e:
        return jsonify({"error": f"Campo faltando: {str(e)}"}), 400

@app.route('/api/tipofontes', methods=['GET'])
def get_tipo_fontes():
    nome = request.args.get('nome', '')
    try:
        tipos = tipo_fontes_control.pesquisar_por_nome(nome)
        tipos_dict = [tipo.to_dict() for tipo in tipos]
        return jsonify(tipos_dict), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/tipofontes/<int:id_tipo_fonte>', methods=['PUT'])
def update_tipo_fonte(id_tipo_fonte):
    try:
        data = request.get_json()
        tipofonte = TipoFonte(
            id_tipo_fonte=id_tipo_fonte,
            nome=data.get('nome', '')
        )
        success = tipo_fontes_control.atualizar(id_tipo_fonte, tipofonte)
        if success:
            return jsonify({"message": "Tipo de Fonte atualizado com sucesso!"}), 200
        else:
            return jsonify({"error": "Erro ao atualizar Tipo de Fonte"}), 400
    except KeyError as e:
        return jsonify({"error": f"Campo faltando: {str(e)}"}), 400

@app.route('/api/tipofontes/<int:id_tipo_fonte>', methods=['DELETE'])
def delete_tipo_fonte(id_tipo_fonte):
    try:
        success = tipo_fontes_control.remover(id_tipo_fonte)
        if success:
            return jsonify({"message": "Tipo de Fonte removido com sucesso!"}), 200
        else:
            return jsonify({"error": "Erro ao remover Tipo de Fonte"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/emissoes', methods=['POST'])
def register_emissao():
    try:
        data = request.get_json()
        tipo_fonte_data = data.get('tipo_fonte')
        tipo_fonte = TipoFonte(id_tipo_fonte=tipo_fonte_data['id_tipo_fonte'])
        
        emissao = EmissoesCarbono(
            id_emissao=data.get('id_emissao', 0),
            tipo_fonte=tipo_fonte,
            emissao=Decimal(data['emissao'])
        )
        success = emissoes_control.cadastrar(emissao)
        if success:
            return jsonify({"message": "Emissão cadastrada com sucesso!"}), 201
        else:
            return jsonify({"error": "Erro ao cadastrar emissão"}), 400
    except KeyError as e:
        return jsonify({"error": f"Campo faltando: {str(e)}"}), 400

@app.route('/api/emissoes/<int:id_tipo_fonte>', methods=['GET'])
def get_emissoes_by_tipo_fonte(id_tipo_fonte):
    try:
        lista_emissoes = emissoes_control.pesquisar_por_tipo_fonte(id_tipo_fonte)
        resultado = [emissao.to_dict() for emissao in lista_emissoes]
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/emissoes/<int:id_emissao>', methods=['PUT'])
def update_emissao(id_emissao):
    try:
        data = request.get_json()
        tipo_fonte_data = data.get('tipo_fonte')
        tipo_fonte = TipoFonte(id_tipo_fonte=tipo_fonte_data['id_tipo_fonte'])

        emissao = EmissoesCarbono(
            id_emissao=id_emissao,
            tipo_fonte=tipo_fonte,
            emissao=Decimal(data['emissao'])
        )
        success = emissoes_control.atualizar(id_emissao, emissao)
        if success:
            return jsonify({"message": "Emissão atualizada com sucesso!"}), 200
        else:
            return jsonify({"error": "Erro ao atualizar emissão"}), 400
    except KeyError as e:
        return jsonify({"error": f"Campo faltando: {str(e)}"}), 400

@app.route('/api/emissoes/<int:id_emissao>', methods=['DELETE'])
def delete_emissao(id_emissao):
    try:
        success = emissoes_control.remover(id_emissao)
        if success:
            return jsonify({"message": "Emissão removida com sucesso!"}), 200
        else:
            return jsonify({"error": "Erro ao remover emissão"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/emissoes/maior', methods=['GET'])
def get_maior_emissao():
    try:
        maior_emissoes = emissoes_control.pesquisar_maior_emissao()
        resultado = [emissao.to_dict() for emissao in maior_emissoes]
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/emissoes/menor', methods=['GET'])
def get_menor_emissao():
    try:
        menor_emissoes = emissoes_control.pesquisar_menor_emissao()
        resultado = [emissao.to_dict() for emissao in menor_emissoes]
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/emissoes/media', methods=['GET'])
def get_media_emissao():
    try:
        media = emissoes_control.calcular_media_emissao()
        return jsonify({"media_emissao": str(media)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)