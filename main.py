from flask import Flask, render_template, request
import converter

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        amount = request.form['amount']
        from_curr = request.form['from']
        to_curr = request.form['to']
        return render_template('index.html', result=converter.converter(amount, from_curr, to_curr))
    else:
        return render_template('index.html', result='')


if __name__ == '__main__':
    app.run(debug=True)
