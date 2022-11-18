from flask import Flask ,jsonify
import requests
from bs4 import BeautifulSoup

def get_currency(input_currency , output_currency):
    url = f"https://www.x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content , 'html.parser')
    rate = soup.find('span' , class_='ccOutputRslt').get_text()
    rate = float(rate[0:-4])
    return rate

app = Flask(__name__)
@app.route('/') # creating our home page
def home():
	return '<h1>Currency Rate API</h1><p>Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<input_currency>-<output_currency>')
def api(input_currency,output_currency):
	rate=get_currency(input_currency,output_currency)
	result_dictionary={"input_currency":input_currency,"output_currency":output_currency,"rate":rate}
	return jsonify(result_dictionary)
	
app.run(host='0.0.0.0')