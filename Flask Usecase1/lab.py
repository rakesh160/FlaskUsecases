#from flask import render_template
from app import app, db
from app.models import User

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User,'Room':'hmmm'}


if __name__ == '__main__':
    app.debug=True
    app.run(host='127.0.0.1', port=5000)
    