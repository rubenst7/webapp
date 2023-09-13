# Import necessary modules 
from flask import Flask
from flask import request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig

# Create a Flask app instance
app = Flask(__name__)

# Configure the Flask app using settings from BaseConfig
app.config.from_object(BaseConfig)

# Initialize the SQLAlchemy database with the Flask app
db = SQLAlchemy(app)

from models import *

# Route for rendering index and retrieves all tasks
@app.route('/', methods=['GET'])
def index():
    tasks = Task.query.order_by(Task.date_task.desc()).all()
    return render_template('index.html', tasks=tasks)

# Route for adding tasks
@app.route('/addtask', methods=['POST'])
def submit():
    text = request.form['text']
    new_task = Task(text)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

# Route for deleting tasks
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    # Retrieve the task to delete
    task = Task.query.get_or_404(task_id)

    # Delete the task from the database
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for('index'))

# Start the Flask application if this script is run directly
if __name__ == '__main__':
    app.run()
