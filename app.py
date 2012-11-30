from bottle import route, run, template, static_file, hook, request, redirect
from mpd import MPDClient
import os

BASE_DIR = os.path.dirname(__file__)


@hook("before_request")
def connect_mpd():
    request.mpd = MPDClient()
    request.mpd.connect("localhost", 6600)
    request.stats = request.mpd.stats

@hook("after_request")
def connect_mpd():
    request.mpd.disconnect()

@route('/')
@route('/<sort_by>')
def index(sort_by='album'):
    lists = request.mpd.list(sort_by)
    current = request.mpd.currentsong()

    return template('index', lists=lists, current=current)

@route('/do/<command>/')
def play(command):
    status = request.mpd.status().get( 'state', '')
    if command == 'play':
        request.mpd.pause() if status == 'play' else request.mpd.play()
    elif command == 'next':
        request.mpd.next()
    elif command == 'prev':
        request.mpd.prev()
    elif command == 'stop':
        request.mpd.stop()
    return redirect('/')
    
@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root=os.path.join(BASE_DIR, 'static'))

if __name__ == '__main__':
    
    run(host='localhost', port=8080, reloader=True, debug=True)
