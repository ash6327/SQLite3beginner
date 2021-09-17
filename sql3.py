import sqlite3

conn = sqlite3.connect('Movies.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS movie
(movie_name TEXT, movie_actor REXT,movie_actress TEXT, movie_year INTEGER,movie_director TEXT)''' )

movies = [
('Mr robot','Rami Malek','Carly Chaikin','2015','Sam Ishmail'),
('Kuruti','Roshan Mathew','srindaa','2021','Anish Pallyall'),
('Nadodikkattu','Mohan Lal','Shobana','1987','Sathyan Anthikad'),
('Pattanapravesham','Sreenivasan','Shobana','1988','Sathyan Anthikad'),
('The social network','Jesse Eisenberg','Brenda Song','2010','David Fincher')
            ]

cur.executemany("INSERT INTO movie VALUES (?,?,?,?,?)",movies)
conn.commit()


for row in cur.execute('''SELECT * FROM movie'''):
    print(row)
a=input('Enter actor name:')
cur.execute(f"SELECT * FROM movie WHERE movie_actor LIKE '{a}'")
print(cur.fetchone())

conn.close()