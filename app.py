import os
import itertools
import operator
from bottle import route, run, template, static_file, hook, request, redirect
from mpd import MPDClient
from mods import Song


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
    songs = Song.find()
    current = request.mpd.currentsong()
    import ipdb; ipdb.set_trace()
    ordered = itertools.groupby(songs, key=operator.attrgetter(sort_by))
    return template('index', songs=ordered, current=current)

@route('/do/<command>/')
def play(command):
    status = request.mpd.status().get( 'state', '')
    if command == 'play':
        request.mpd.pause() if status == 'play' else request.mpd.play()
    elif command == 'next':
        request.mpd.next()
    elif command == 'prev':
        request.mpd.previous()
    elif command == 'stop':
        request.mpd.stop()
    return redirect('/')
    
@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root=os.path.join(BASE_DIR, 'static'))

if __name__ == '__main__':
    Song.initialize()
    c = MPDClient()
    c.connect("localhost", 6600)
    for s in c.listallinfo():
        try:
            song = Song(**s)
        except Exception as e:
            print(e, s)
        else:
            song.save() 
    
    run(host='localhost', port=8080, reloader=True, debug=True)
