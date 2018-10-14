import psycopg2


def connect():
	conn=psycopg2.connect("dbname='books' user='postgres' password='@Solve2016' host='localhost' port='5432'")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS table1 (id SERIAL,title text not null, author text not null,year integer not null, isbn integer not null)")
	conn.commit()
	conn.close()

def insert(title,author,year,isbn):
	conn=psycopg2.connect("dbname='books' user='postgres' password='@Solve2016' host='localhost' port='5432'")
	cur=conn.cursor()
	cur.execute("INSERT INTO table1 (title,author,year,isbn) VALUES ('%s','%s',%s,%s)" %(title,author,year,isbn))
	conn.commit()
	conn.close()

def view():
	conn=psycopg2.connect("dbname='books' user='postgres' password='@Solve2016' host='localhost' port='5432'")
	cur=conn.cursor()
	cur.execute("SELECT * FROM table1 ORDER BY id")
	rows=cur.fetchall()
	conn.close()
	return rows

def search(title="",author="",year=0,isbn=0):
	conn=psycopg2.connect("dbname='books' user='postgres' password='@Solve2016' host='localhost' port='5432'")
	cur=conn.cursor()
	cur.execute("SELECT * FROM table1 WHERE title like '%s' OR author like '%s' OR year = '%s' OR isbn = '%s'" %(title,author,year,isbn))
	rows=cur.fetchall()
	conn.close()
	return rows

def delete(id):
	conn=psycopg2.connect("dbname='books' user='postgres' password='@Solve2016' host='localhost' port='5432'")
	cur=conn.cursor()
	cur.execute("DELETE FROM table1 WHERE id='%s'" %(id,))
	conn.commit()
	conn.close()

def update(id,title,author,year,isbn):
	conn=psycopg2.connect("dbname='books' user='postgres' password='@Solve2016' host='localhost' port='5432'")
	cur=conn.cursor()
	cur.execute("UPDATE table1 SET title='%s', author='%s',year=%s,isbn=%s WHERE id='%s'" %(title,author,year,isbn,id))
	conn.commit()
	conn.close()



connect ()
#insert('The earth','John Smith',1918,913123231)
#insert('The water','John Doe',1919,913123231)
#insert('The fire','Jane Table',1920,913123231)
#insert('The wind','Jane Doe',1921,913123231)
#insert('The void','Jack Doe',1922,913123231)
#delete(2)
#update(6,'The moon','John Doe',1920,91319131)
#print (view())
#print(search(author='John Table'))
#print(search(isbn=9131))
