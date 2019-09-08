from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    name = request.args.get('name', 'Nobody')

    if request.method == 'POST':
        name = request.form['name']
        greet = request.form['greet']
        greeting = f'{greet}, {name}'
        return render_template('index.html', greeting=greeting)
    else:
        return render_template('hello_forms.html')


if __name__ == '__main__':
    app.run()
