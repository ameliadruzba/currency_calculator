import requests
import csv

dane_api = requests.get('https://api.nbp.pl/api/exchangerates/tables/C?format=json')
data = dane_api.json()

with open('waluty.csv', 'w') as file:
    naglowki = ["currency", "code", "bid", "ask"]
    writer =  csv.DictWriter(file, fieldnames=naglowki)
    writer.writeheader() #odpowaida za nazwy kolumn aby latwiej bylo sie odnosic

    for i in data[0]['rates']:
        writer.writerow({
            "currency": i["currency"],
            "code": i["code"],
            "bid": i["bid"],
            "ask": i["ask"]
        })