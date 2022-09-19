import sqlite3


# データベースの接続
conn = sqlite3.connect('./ranking.db')
cur = conn.cursor()

cur.execute("INSERT INTO ranking(name, score) VALUES('cron', 9999)")
conn.commit()