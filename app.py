from flask import Flask 
from astroquery.simbad import Simbad
from flask import Flask, render_template

app = Flask(__name__)


Simbad.add_votable_fields('flux(V)', 'otype')


@app.route('/objetos/<string:corpo>')
def inicio(corpo):
    resultado = Simbad.query_object(corpo)
 
    dados = f"Dados de {corpo}: <br>"

    if resultado is None or len(resultado) == 0:
        return f"Corpo celeste '{corpo}' não encontrado no Simbad."

    dados = f"<h2>Dados de '{corpo}'</h2><table border='1'>"
    traducoes = {
                'MAIN_ID': 'Identificador Principal',
                'RA': 'Ascensão Reta',
                'DEC': 'Declinação',
                'FLUX_V': 'Magnitude Visual',
                'OTYPE': 'Tipo de Objeto',
                'RA_PREC': 'Precisão da Ascensão Reta',
                'DEC_PREC': 'Precisão da Declinação',
                'COO_ERR_MAJA': 'Erro nas Coordenadas (Eixo Maior)',
                'COO_ERR_MINA': 'Erro nas Coordenadas (Eixo Menor)',
                'COO_ERR_ANGLE': 'Ângulo do Erro nas Coordenadas',
                'COO_QUAL': 'Qualidade das Coordenadas',
                'COO_WAVELENGTH': 'Comprimento de Onda das Coordenadas',
                'COO_BIBCODE': 'Código Bibliográfico',
                'SCRIPT_NUMBER_ID': 'ID do Script'
                 }
    # Criar uma lista de dicionários com os dados
    dados_lista = []
    for coluna in resultado.colnames:
        try:
             valor = resultado[coluna]
             dados_lista.append({'campo': traducoes.get(coluna, coluna), 'valor': valor})
        except KeyError as e:
             dados_lista.append({'campo': traducoes.get(coluna, coluna), 'valor': f"Erro ({e})" })
             
    return render_template ('resultado.html', corpo = corpo, dados = dados_lista)
if __name__ == "__main__":
    app.run(debug=True)

    

