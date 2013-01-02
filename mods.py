from goatfish import models
import sqlite3

class Song(models.Model):
    """title = models.Attribute()
                album = models.Attribute() 
                albumartist = models.Attribute()
                artist = models.Attribute()
                date = models.Attribute()
                file = models.Attribute()
                genre = models.Attribute()
                time = models.Attribute()"""

    class Meta:
        connection = sqlite3.connect(':memory:')
        indexes = (
            ('album',),
            ('artist',),
            ('genre',),
            ('date',),
        )
