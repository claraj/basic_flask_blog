from datetime import datetime 

class Post:

    def __init__(self, user_id, title, text, post_datetime=datetime.now()):

        if not user_id:
            raise ValueError('User ID must be provided')

        title = title.strip() 

        if not title:  # None and empty strings are False 
            raise ValueError('Title must be provided and not blank')

        text = text.strip()

        if not text: 
            raise ValueError('Text must be provided and not blank ')
        
        now = datetime.now()

        if post_datetime > now:  # is the date in the future? number of seconds greater than the current number of seconds 
            raise ValueError('Timestamp must be now or in the past')

        self.user_id = user_id
        self.title = title
        self.text = text 
        self.post_datetime = post_datetime