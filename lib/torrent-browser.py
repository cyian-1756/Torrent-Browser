import gtk
import webkit
import urllib
import json

head = '''
<html>
<head>
<style>
p {
    font-size: 60%;
}
#content {
  width: 700px ;
  margin-left: auto ;
  margin-right: auto ;
}
</style>
<title>Page title here</title>
</head>
<body>
    <div>'''
foot = '</p></div></body></html>'
def omdb_call(name,year):
    url = 'http://www.omdbapi.com/?t={0}&y={1}&plot=full&r=json'.format(name,year)
    data = urllib.urlopen(url).read()
    json_data = json.loads(data)
    poster = json_data["Poster"]
    urllib.urlretrieve(poster, json_data["Title"])
    info = '<img src="{0}"/>'.format(poster) + json_data["Title"] + '<br>' + json_data["Year"] + '<br>' + json_data["Rated"] + '<br>' + json_data["Released"] + '<br>' + json_data["Runtime"]
    return info
test_stuff = omdb_call('brick','2005')

# Create window
w = gtk.Window()
w.set_title("Example Editor")
w.connect("destroy", gtk.main_quit)

window = webkit.WebView()
# Load an HTML
window.load_html_string(head + test_stuff + foot, "file:///")

w.add(window)
w.show_all()

gtk.main()
