from flask import Flask, render_template, request
from search import engine

app = Flask(__name__)
engine.init()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/tariff_search', methods=['POST'])
def search():
    # print(request.form)
    search_result = engine.search(request.form['query'])
    return render_template('list_template.html', items=search_result['results'])


if __name__ == '__main__':
    app.run()
