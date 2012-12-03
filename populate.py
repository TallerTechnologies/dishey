from mpd import MPDClient
from mods import Song

c = MPDClient()
c.connect("localhost", 6600)

for s in c.listallinfo():
    song = Song(**s)
    song.save()
