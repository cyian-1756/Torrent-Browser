import gtk, webkit, urllib

def omdb_call(name,year):
    url = 'http://www.omdbapi.com/?t={0}&y={1}&plot=full&r=json'.format(name,year)
    return urllib.urlopen(url).read()
test_stuff = omdb_call('brick','2006')

# Create window
w = gtk.Window()
w.set_title("Example Editor")
w.connect("destroy", gtk.main_quit)

window = webkit.WebView()
# Load an HTML
window.load_html_string(str(test_stuff), "file:///")

w.add(window)
w.show_all()

gtk.main()
