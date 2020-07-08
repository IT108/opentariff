from flask import Flask, render_template, request
from search import engine

app = Flask(__name__)
engine.init()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/tariff_search', methods=['POST'])
def search():
    print(request.form)
    return engine.search(request.form['query'])


if __name__ == '__main__':
    app.run()
