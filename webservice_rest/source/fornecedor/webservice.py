# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

from webservice_rest.source.fornecedor.service.filmes_service import FilmesService

app = Flask(__name__, static_folder='templates')
print(app.root_path)
print(app.static_folder, app.static_url_path)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/busca_filmes', methods=['POST'])
def test():
    na = dict(request.form)
    print(na)
    no = FilmesService.busca_varios(**na)

    return render_template('resposta.html', filmes=no)


app.run(debug=True)
