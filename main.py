from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def currency_converter():
    if request.method == 'POST':
        amount = request.form['amount']
        from_curr = request.form['from']
        to_curr = request.form['to']

        api_key = "4VtAkMG76ToTKIglU76mvxrK388xfHhG"
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_curr}&from={from_curr}&amount={amount}"
        headers = {"apikey": api_key}

        response = requests.get(url, headers=headers)
        data = response.json()

        if data.get('success'):
            result = f"{amount} {from_curr.upper()} = {data['result']} {to_curr.upper()}"
        else:
            result = "Error: Failed to get data."
        return render_template('index.html', result=result)
    else:
        return render_template('index.html', result='')


if __name__ == '__main__':
    app.run(debug=True)
