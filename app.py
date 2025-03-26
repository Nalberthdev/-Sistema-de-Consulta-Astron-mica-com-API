from flask import Flask 
from astroquery.simbad import Simbad

app = Flask(__name__)


Simbad.add_votable_fields('ra', 'dec', 'main_id')


@app.route('/planetas/<string:corpo>')
def inicio(corpo):
    resultado = Simbad.query_object(corpo)
 
    dados = f"Dados de {corpo}: <br>"

    if resultado is None or len(resultado) == 0:
        return f"Corpo celeste '{corpo}' não encontrado no Simbad."

    dados = f"Dados de '{corpo}:<br> "
    for coluna in resultado.colnames:
        try:
            valor = resultado[coluna[0]]
            dados += f"{coluna}: {valor} <br>"
        except KeyError as e:
            dados += f"{coluna}: Erro ao acessar o valor ({e})<br>"

    return dados
    
if __name__ == "__main__":
    app.run(debug=True)

    

