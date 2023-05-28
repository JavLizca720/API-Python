from flask import Flask, render_template

import requests
app = Flask (__name__)

@app.route('/')
def index():
    datas=requests.get('https://api.dailymotion.com/videos?channel=music&limit=10')

    dataJSON = datas.json()
    print (dataJSON)

    return render_template('index.html', datas=dataJSON['list'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)