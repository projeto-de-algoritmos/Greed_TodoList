from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date,datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    '''
    I think this is like the tupple, got that ? 
    '''
    id = db.Column(db.Integer,primary_key = True)
    Title = db.Column(db.String(64))
    Completed = db.Column(db.Boolean)
    ProcessTime = db.Column(db.Integer,default = 1)
    Deadline = db.Column(db.Date)


@app.route('/')
def homepage():
    '''
        homepage of the todo app
    '''
    todo_list = Todo.query.all()

    return render_template('base.html',todo_list = todo_list,now = date.today())

@app.route('/add',methods = ['POST'])
def add():
    '''
        when you click the add botão, insere no db
    '''
    title = request.form.get("title")
    process_time = request.form.get("process")
    deadline = request.form.get("deadline")

    #print(f"HERE GO THE DEEEEEEEADLIIIINEEEEEEE  {deadline} OI OI OI OI OI OI ")
    #print(type(deadline))

    deadline_p = datetime.strptime(deadline, '%Y-%m-%d').date()

    new_todo = Todo(Title = title,Completed = False, ProcessTime = process_time, Deadline = deadline_p)
    db.session.add(new_todo)
    db.session.commit()
    
    return redirect(url_for("homepage"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    '''
        Query database, here you just change the status from not completed to completed
    '''
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.Completed = not todo.Completed
    db.session.commit()

    return redirect(url_for("homepage"))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    '''
    Query database to delete the numbeeer, with the todo_id paramm
    '''
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("homepage"))

# here we go
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)