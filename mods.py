from goatfish import models

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
        database = ':memory:'
        indexes = (
            ('album',),
            ('artist',),
        )
