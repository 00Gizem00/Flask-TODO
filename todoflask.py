import sqlite3
from flask import Flask, redirect, render_template, jsonify, g, request

app = Flask(__name__)

DATABASE = 'todoslist.db'

# Connect to database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE) # Create database if not exist
    return db

# Close database connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def hello_world():
    TODOS = get_db()
    cur = TODOS.cursor()
    cur.execute("SELECT * FROM todos")
    todos = cur.fetchall()
    return render_template('index.html', todos=todos)


# api jsonified
@app.route('/api/todos', methods=['post'])
def api_todos():
    TODOS = get_db()
    return jsonify(TODOS)



@app.route('/add', methods=['POST'])
def add_todo():
    todo_title = request.form.get('todo')
    if todo_title:
        TODOS = get_db()
        cur = TODOS.cursor()
        cur.execute("INSERT INTO todos (title, completed) VALUES (?, ?)", (todo_title, 0))
        TODOS.commit()
    return redirect('/')

@app.route('/todos/<id>/update', methods=['POST'])
def update_todo(id):
    todo_title = request.form.get('title')
    if todo_title:
        TODOS = get_db()
        cur = TODOS.cursor()
        cur.execute("UPDATE todos SET title = ? WHERE id = ?", (todo_title, id))
        TODOS.commit()
    return redirect('/')

@app.route('/todos/<int:id>/delete', methods=['POST'])
def delete_todo(id):
    TODOS = get_db()
    cur = TODOS.cursor()
    cur.execute("DELETE FROM todos WHERE id = ?", (id,))
    TODOS.commit()
    return redirect('/')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)