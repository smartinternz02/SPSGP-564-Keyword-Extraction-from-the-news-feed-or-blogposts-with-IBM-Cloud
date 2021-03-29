from flask import Flask, request, render_template
import re
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/extractor')
def extractor():
    return render_template('extractor.html')

@app.route('/keywords', methods=['POST'])
def keywords():
    sen = request.form['sentence'].replace(" ", "%20")
    num = request.form['num']
    print(sen)
    keyword = check(sen, num)
    return render_template('keywords.html', keyword=keyword)

def check(sentence, num):
    url = "https://textanalysis-keyword-extraction-v1.p.rapidapi.com/keyword-extractor-text"

    payload = "text=" + sentence + "&wordnum=" + num
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-key': "bdf00f69d0mshf71b715e665de84p187496jsn103deb88c72c",
        'x-rapidapi-host': "textanalysis-keyword-extraction-v1.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.json()['result']

if __name__ == "__main__":
    app.run(debug="")