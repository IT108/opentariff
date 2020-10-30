from flask import render_template, request
from app.search import engine
from app import app
import app.config as cfg


@app.route('/')
def index():
    return render_template('index.html', **cfg.params)


@app.route('/about')
def about():
    return render_template('about.html', **cfg.params)


@app.route('/find-tariff')
def find_tariff():
    return render_template('find-tariff.html', **cfg.params)


@app.route('/api/tariff_search', methods=['POST'])
def search():
    # print(request.form)
    search_result = engine.search(request.form['query'])
    return render_template('list_template.html', items=search_result['results'])


@app.route('/api/get_tariff', methods=['POST'])
def get_tariff():
    search_result = engine.get_by_id(request.form['tariff_id'])
    res = {'result': search_result}
    print(res)
    return res
