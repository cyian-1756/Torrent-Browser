from flask import Flask
from flask import render_template

import urllib
import json
import re

app = Flask(__name__)

@app.route('/<name>/<int:year>')
def populate_movie(name,year):
    url = 'http://www.omdbapi.com/?t={0}&y={1}&plot=full&r=json'.format(name,year)
    data = urllib.urlopen(url).read()
    json_data = json.loads(data)
    tpb_url = 'https://thepiratebay.se/s/?q={0}+({1})&video=on&category=0&page=0&orderby=99'.format(name,year)
    tpb_data = urllib.urlopen(tpb_url).read()
    magnets = re.findall('(magnet:\S*)"', tpb_data)

    return render_template('index.html', data=json_data, magnet=magnets[0])

if __name__ == '__main__':
	app.debug = True # turn off in production
	app.run()
