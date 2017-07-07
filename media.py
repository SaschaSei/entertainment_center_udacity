import webbrowser


class Movie():
    """This class is a way to store movie info."""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, titel, storyline, poster_image, trailer_youtube):
        self.title = titel
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
