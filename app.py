from flask import Flask
from flask import render_template

import urllib
import json
import re
app = Flask(__name__)

@app.route('/<name>/<int:year>')
def omdb_call(name,year):
    url = 'http://www.omdbapi.com/?t={0}&y={1}&plot=full&r=json'.format(name,year)
    data = urllib.urlopen(url).read()
    json_data = json.loads(data)
    poster = json_data["Poster"]
    tpb_url = 'https://thepiratebay.se/s/?q={0}+({1})&video=on&category=0&page=0&orderby=99'.format(name,year)
    tpb_data = urllib.urlopen(tpb_url).read()
    magnets = re.findall('magnet:\S*',tpb_data)
    # Removing the extra "" from the magnet
    magnets = [s.replace('"','') for s in magnets]
    info = '<img src="{0}"/>'.format(poster) + '<br>' + json_data["Title"] + '<br>' + json_data["Year"] + '<br>' + json_data["Rated"] + '<br>' + json_data["Released"] + '<br>' +  json_data["Runtime"] + '<a href="{0}">'.format(magnets[0]) + '<br>' + 'Download </a>'

    return render_template('index.html', body=info)

if __name__ == '__main__':
	app.run()
