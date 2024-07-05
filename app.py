from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find_all('h1')  # Por ejemplo, obteniendo todas las etiquetas <h1>
        return render_template('index.html', results=results)
    return render_template('index.html', results=[])

if __name__ == '__main__':
    app.run(debug=True)
