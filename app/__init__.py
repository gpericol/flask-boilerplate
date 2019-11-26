from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.mod_dummy.controllers import mod_dummy as dummy_module

app.register_blueprint(dummy_module)
# app.register_blueprint(..._module)
# ..

db.create_all()