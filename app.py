from flask import Flask
from flask import render_template

import urllib
import json

app = Flask(__name__)

@app.route('/<name>/<int:year>')
def omdb_call(name,year):
    url = 'http://www.omdbapi.com/?t={0}&y={1}&plot=full&r=json'.format(name,year)
    data = urllib.urlopen(url).read()
    json_data = json.loads(data)
    poster = json_data["Poster"]
    info = '<img src="{0}"/>'.format(poster) + json_data["Title"] + '<br>' + json_data["Year"] + '<br>' + json_data["Rated"] + '<br>' + json_data["Released"] + '<br>' + json_data["Runtime"]

    return render_template('index.html', body=info)

if __name__ == '__main__':
	app.run()