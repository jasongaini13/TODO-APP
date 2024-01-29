from flask import Flask, render_template,session,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask import request



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/todo list'
db=SQLAlchemy(app)




class tasks(db.Model):
   
    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    done= db.Column(db.Boolean)
    

@app.route("/")
def index():
    tasks_list = tasks.query.all()

    return render_template('index.html',tasks_list=tasks_list)


@app.route("/add",methods=['POST'])
def add():
    name=request.form.get("name")
    new_task=tasks(name=name,done=False)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    task = tasks.query.get(todo_id)
    task.done=not task.done
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = tasks.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

       
app.run(debug=True)
