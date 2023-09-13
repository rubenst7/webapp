import datetime
from app import db


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    date_task = db.Column(db.DateTime, nullable=False)

    def __init__(self, text):
        self.text = text
        self.date_task = datetime.datetime.now()