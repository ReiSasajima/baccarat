from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

# データベースの接続
conn = sqlite3.connect('./ranking.db', check_same_thread=False)
cur = conn.cursor()

@app.route('/')
def ranking():
  scores = cur.execute("SELECT name, score FROM ranking ORDER BY score DESC;")
  return render_template('ranking.html', scores=scores)

@app.route('/register', methods=['POST', 'GET'])
def register():
  if request.method == 'GET':
    return render_template('register.html')

  elif request.method == 'POST':
    name = request.form['name']
    score = request.form['score']
    if not name:
      return redirect('/')
    if not score:
      return redirect('/')
    #スコアの追加
    try:
      cur = conn.cursor()
      cur.execute("INSERT INTO ranking(name, score) VALUES(?, ?);", (name, score,))
      conn.commit()
      return redirect('/')
    except:
      return redirect('/')

  else:
    return redirect('/')

if __name__ == '__main__':
    app.run()



