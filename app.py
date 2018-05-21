from flask import Flask, request, redirect, url_for, render_template
from models import db, MyList
import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:yourpasswordhere@localhost/todoflask'
db.init_app(app)

@app.route('/')
def index():
    mylist = MyList.query.all()
    return render_template('index.html', mylist=mylist)

@app.route('/add', methods=['POST'])
def add():
    # the item arg is tied to the name value of the input
    todo = MyList(item=request.form['todoitem'])
    db.session.add(todo) # session adds the todo variable
    db.session.commit()
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True, port=3000)