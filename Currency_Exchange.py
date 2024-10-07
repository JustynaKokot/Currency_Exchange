import requests

req = requests.get("https://api.nbp.pl/api/exchangerates/tables/A/")
print(req.status_code)

print(req.headers)

print(req.text)

#lista, lista, słownik


rates = req.text[74:-3]
print(rates)

res = eval(rates)
print(res)

for res[1]['code'] in res:
    print(f"Currency rate for {res[1]['code']['code']} is {res[1]['code']['mid']} PLN.")

how_much = input('How much you would like to convert?')
from_currency = input('In what currency you have got money?')
to_currency = input('To what currency you would like to exchange?')

