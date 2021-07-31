from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from tabulate import tabulate

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "tuto5"

mysql = MySQL(app)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/envia', methods=['GET', 'POST'])
def envia():
	if request.method == 'POST':
		hum = request.form['humedad']
		temp = request.form['temperatura']
		sql = mysql.connection.cursor()
		sql.execute("INSERT INTO tabla (humedad, temperatura) VALUES (%s, %s)", (hum, temp))
		mysql.connection.commit()
		sql.close()
		return "Enviado..."

@app.route('/mostrar', methods=['GET', 'POST'])
def mostrar():
	if request.method == 'POST':
		sql = mysql.connection.cursor()
		temp = sql.execute(''' SELECT * FROM tabla''')
		if temp > 0:
			rv = sql.fetchall()
			return render_template('ver.html', rv=rv)


if __name__ == '__main__':
	app.run(host='10.10.10.187')
