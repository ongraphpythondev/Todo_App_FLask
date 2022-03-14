from datetime import datetime
from settings import *

#Init db
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500),nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"

    def __init__(self,title, description):
        self.title = title
        self.description = description        
