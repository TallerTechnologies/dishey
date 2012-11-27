from bottle import route, run, template, static_file
from mpd import MPDClient
import os

BASE_DIR = os.path.dirname(__file__)
mpd = MPDClient()
mpd.connect("localhost", 6600)


@route('/')
def index():
    lists = mpd.list("album")
    import ipdb; ipdb.set_trace()
    return template('index', lists=lists)

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root=os.path.join(BASE_DIR, 'static'))

if __name__ == '__main__':
    
    run(host='localhost', port=8080, reloader=True, debug=True)
