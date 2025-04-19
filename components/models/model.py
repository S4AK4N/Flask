from components.models.db import db

#タスク名
class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
# タスク内容
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    article = db.Column(db.Text, nullable=False)
    is_done = db.Column(db.Boolean, default = False)
    