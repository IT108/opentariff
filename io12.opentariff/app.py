from flask import Flask, render_template, request
from search import engine

app = Flask(__name__)
engine.init()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


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


if __name__ == '__main__':
    app.run()
