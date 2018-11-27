from app import db

class MyList(db.Model):
    __tablename__ = 'todo_items'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.Text, nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'{self.item}'