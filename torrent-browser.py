import gtk, webkit, urllib, re

head = '''
<html>
<head>
<style>
p {
    font-size: 60%;
}
</style>
<title>Page title here</title>
</head>
<body>
    <div>
        <p>'''
foot = '</p></div></body></html>'
def omdb_call(name,year):
    url = 'http://www.omdbapi.com/?t={0}&y={1}&plot=full&r=json'.format(name,year)
    data = urllib.urlopen(url).read()
    data = data.replace(',', '<br>')
    data = data.replace('"','')
    data = data.replace('{','')
    data = data.replace('}','')
    return data
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
