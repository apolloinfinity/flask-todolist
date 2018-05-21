from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MyList(db.Model):
    # __tablename__ = 'todo_items'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'{self.id} {self.item}'