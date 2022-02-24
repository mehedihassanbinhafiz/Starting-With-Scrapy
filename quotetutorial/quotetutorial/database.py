import  sqlite3

conn = sqlite3.connect('quote.sqlite3')
cur = conn.cursor()
cur.execute("""create table quotes( title text, author text, tag text """)

conn.commit()
conn.close()
