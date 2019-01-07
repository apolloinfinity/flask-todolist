from app import app, db  # First app is the folder module, then the second app variable
from app.models import MyList


@app.shell_context_processor
def make_shel_context():
    return {'db': db, 'MyList': MyList}


if __name__ == '__main__':
    app.run(debug=True)
