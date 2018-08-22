from flask import render_template, redirect, url_for, request
from app import app
from app.models import db, MyList

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