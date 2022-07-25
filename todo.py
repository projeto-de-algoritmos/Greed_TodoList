from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    '''
    This is a tupleeeee
    '''
    id = db.Column(db.Integer,primary_key = True)
    Title = db.Column(db.String(64))
    Completed = db.Column(db.Boolean)

@app.route('/')
def homepage():
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html',todo_list = todo_list)

@app.route('/about')
def about():
    return "<h1>About us</h1>"

@app.route('/add',methods = ['POST'])
def add():
    '''
    
    '''
    title = request.form.get("title")
    new_todo = Todo(Title = title,Completed = False)
    db.session.add(new_todo)
    db.session.commit()
    
    return redirect(url_for("homepage"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    '''
    Query database
    '''
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.Completed = not todo.Completed
    db.session.commit()

    return redirect(url_for("homepage"))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    '''
    Query database
    '''
    
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("homepage"))


if __name__ == "__main__":
    db.create_all()

    app.run(debug=True)