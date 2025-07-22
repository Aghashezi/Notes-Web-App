from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

DB_NAME = 'notes.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    query = request.args.get('q', '')
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    if query:
        c.execute("SELECT * FROM notes WHERE title LIKE ? OR content LIKE ? ORDER BY timestamp DESC", 
                  ('%' + query + '%', '%' + query + '%'))
    else:
        c.execute("SELECT * FROM notes ORDER BY timestamp DESC")
    notes = c.fetchall()
    conn.close()
    return render_template('index.html', notes=notes, query=query)

@app.route('/add', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        c.execute("UPDATE notes SET title = ?, content = ?, timestamp = CURRENT_TIMESTAMP WHERE id = ?", 
                  (title, content, note_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        c.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
        note = c.fetchone()
        conn.close()
        return render_template('edit_note.html', note=note)

@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
