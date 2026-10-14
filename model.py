from datetime import datetime 

class Post:

    def __init__(self, user_id, title, text, timestamp=datetime.now().timestamp()):
        self.user_id = user_id
        self.title = title
        self.text = text 
        self.timestamp = timestamp

