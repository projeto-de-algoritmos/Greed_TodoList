from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy 
from datetime import date,datetime,timedelta
import pandas as pd

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

    late = lateness(todo_list)

    #todo_list = Todo.query.order_by(Todo.Deadline).all()
    print(todo_list)
    return render_template('base.html',todo_list = todo_list,now = date.today(),lateness = late)

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

@app.route('/deadline')
def sort_deadline():
    # pegar os dados do banco ordenados pela deadline
    # date
    # calcular lateness
    # redirecionar pra homepage
    # printar em ordem e printar lateness
    #todo_list = Todo.query.all()

    todo_list = Todo.query.order_by(Todo.Deadline).all()
    print(todo_list)

    #print(todo_list)

    late = lateness(todo_list)

    return render_template('base.html',todo_list = todo_list,now = date.today(),lateness = late)

def lateness(todo_list):

    late = {}

    Current = date.today()

    if(len(todo_list) == 0):
        return {}

    for todo in todo_list:
        end = (Current + timedelta(todo.ProcessTime))

        #print(f"Para {todo.Title} :\nDeadline {todo.Deadline}\nCurrent {Current}\nProcess {todo.ProcessTime}\n")
        if(todo.Deadline >= end):
            late[todo.Title] = (end - todo.Deadline)
        else:
            #print(f"Atraso {end - todo.Deadline}")
            late[todo.Title] = (end - todo.Deadline)

        
        Current = Current + timedelta(todo.ProcessTime)

    late_dict = pd.Series(late)

    #print("####################")
    #print(late_dict)
    lateness_list = late_dict.dt.days

    #print(lateness_list)
    
    late_dic = {}
    i = 0
    for todo in todo_list:
        late_dic[todo.Title] = lateness_list[i]
        i = i + 1

    return late_dic

@app.route('/process_time')
def sort_process_time():
    # pegar os dados do banco ordenados pela process
    # calcular lateness
    # redirecionar pra homepage
    # printar em ordem e printar lateness
    #todo_list = Todo.query.all()

    todo_list = Todo.query.order_by(Todo.ProcessTime).all()
    #print(todo_list)

    late = lateness(todo_list)
    return render_template('base.html',todo_list = todo_list,now = date.today(),lateness = late)

# here we go
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)