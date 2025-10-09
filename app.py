from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/main')
def hello():
    return render_template('main.html')

@app.route('/kal', methods = ['POST', 'GET'])
def kalkulator():
    wynik = None
    if request.method == 'POST':
        with open('waluty.csv', 'r') as file:
            reader = csv.DictReader(file)
            waluta = request.form['waluta']
            kwota = float(request.form['kwota'])
            for i in reader:
                if i['code'] == waluta.upper():
                    kurs = float(i['ask'])
                    wynik = kwota * kurs
                    break
    return render_template('kalkulator.html', wynik = wynik)
