class Post:
    title = None
    post = None


    def __init__(self, title, post):
        self.title = title
        self.post = post


    def get_post(self):
        return title + ' ' + post