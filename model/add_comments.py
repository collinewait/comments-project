import uuid
import json

class addComments:
    def __init__(self,  id , comment , timestamp ):
        self.id = id
        self.comment = comment
        self.timestamp = timestamp

    def json(self):
        """
        json representation of the Order model
        """
        return json.dumps({
            'id': self.id,
            'comment': self.comment,
            'timestamp': self.timestamp,
           
        })
        
