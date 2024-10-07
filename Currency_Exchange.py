import requests
link = requests.get("https://api.nbp.pl/api/exchangerates/tables/A/")
response = link.json()
print(response)

for rate in response[0]['rates']:
    print(f'Currency rate for {rate["code"]} is {rate["mid"]} PLN.')


quantity = int(input('How much you would like to convert?'))
currency = input('In what currency you have got money?')

for rate in response[0]['rates']:
    if currency == rate["code"]:
        result = quantity * float(rate["mid"])
        print(f'You wil get {result} PLN.')
