import sqlite3
connection=sqlite3.connect("movie.db")
cursor=connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY AUTOINCREMENT,movie_name TEXT NOT NULL, rating REAL NOT NULL )''')
movie="Dhurandhar"
rating=5
cursor.execute('''INSERT INTO movies (movie_name,rating)VALUES(?,?)''',(movie,rating))
connection.commit()

cursor.execute('''UPDATE movies SET rating=10 WHERE id=1''')
connection.commit()


cursor.execute('''DELETE FROM movies Where id=3''')
connection.commit()
cursor.execute('''DELETE FROM movies Where id=4''')
connection.commit()
cursor.execute('''DELETE FROM movies Where id=5''')
connection.commit()
cursor.execute('''DELETE FROM movies Where id=6''')
connection.commit()

cursor.execute('''SELECT * FROM movies''')
movies=cursor.fetchall()
for i in movies:
    print(i)

connection.close()