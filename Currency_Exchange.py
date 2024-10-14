import requests
link = requests.get("https://api.nbp.pl/api/exchangerates/tables/A/")
response = link.json()
print(response)


# 1. Wyświetlanie wszystkich dostepnych kursów walut

for rate in response[0]['rates']:
    print(f'Currency rate from {response[0]["effectiveDate"]} for {rate["code"]} is {rate["mid"]} PLN.')


# 2. Przeliczanie waluty na inną walutę

quantity = int(input('How much you would like to convert?'))
currency_from = input('In what currency you have got money?')
currency_to = input('In what currency would you like to get money? ')

for rate in response[0]['rates']:
    if currency_from in rate["code"]:
        result1 = quantity * rate["mid"]
        print(f'You wil get {round(result1, 2)} PLN.')

for rate in response[0]['rates']:
    if currency_to in rate["code"]:
        result2 = result1 / rate["mid"]
        print(f'You can exchange {quantity} {currency_from} to {round(result2, 2)} {currency_to}.')


# 3. Pokazywanie zmian kursu waluty w czasie

to_compare = input('What currency would you like to compare?')
print(to_compare)

url = 'https://api.nbp.pl/api/exchangerates/rates/A/EUR/last/30/'
url_list = list(url)
print(url_list)
url_list[-12:-9] = to_compare
result_url = "".join(url_list)
print(result_url)


link2 = requests.get(result_url)
response2 = link2.json()
print(response2)

list = []
sum = 0

for number in response2['rates']:
    x = number['mid']
    list.append(x)
    sum += x
    x += 1

print(list)
print(sum)

average = sum/30
print(round(average, 4))

if list[29] > average:
    print('Better do not exchange money today. Today exchange rate is higher than average from last 30 days.')
elif list[29] == average:
    print('Today exchange rate is the same like an average from last 30 days.')
else:
    print('It is good day to exchange money! Today exchange rate is lower than average from last 30 days.')


# 7. Tworzenie wykresu

from matplotlib import pyplot as plt
import pandas as pd

list_of_dates = []
for date in response2['rates']:
    y = date['effectiveDate']
    list_of_dates.append(y)
print(list_of_dates)
print(len(list_of_dates))

#adding_2_lists = dict(zip(list_of_dates, list))
#print(adding_2_lists)

# co to jest scalar value?
df = pd.DataFrame([list_of_dates, list], index=['Date', 'Currency rate']).T.explode('Currency rate')
print(df.head(30))

x = df['Date']
y = df['Currency rate']
plt.figure(figsize=(17,6))
plt.plot(x, y, 'dodgerblue', label = 'Currency rate change', linewidth = 1)
plt.xlabel('Date', fontsize = 16)
plt.ylabel('Currency rate', fontsize = 16)
plt.title('Currency rate change over last 30 days', fontsize = 16)
plt.grid(False)
plt.legend()
plt.show()













