import requests


def converter(amount, from_curr, to_curr):
    api_key = "4VtAkMG76ToTKIglU76mvxrK388xfHhG"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_curr}&from={from_curr}&amount={amount}"
    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers)
    data = response.json()

    if data.get('success'):
        result = f"{amount} {from_curr.upper()} = {data['result']} {to_curr.upper()}"
    else:
        result = "Error: Failed to get data."
    return result
