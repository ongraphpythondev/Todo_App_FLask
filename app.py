from flask import render_template,request,redirect,url_for

from settings import *
from models import Todo,db


@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['description']
        todo = Todo(title,desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template("index.html", allTodo=allTodo)

@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method=="POST":
        title = request.form['title']
        desc = request.form['description']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.description = desc
        db.session.commit()
        return redirect(url_for('home'))
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template("update.html",todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/view/<int:sno>')
def view(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('view.html',todo=todo)



if __name__ == "__main__":
    app.run(debug=True)
