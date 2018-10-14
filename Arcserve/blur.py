import random
from random import randint
import psycopg2


def distinct_server():
	conn=psycopg2.connect("dbname='arcserve' user='solve1' password='Solve123!' host='172.16.18.162' port='5432'")
	cur=conn.cursor()
	cur.execute("drop table dist_srv;")
	cur.execute("create table dist_srv ( id serial primary key, server_ text,  number Integer,min_id Integer,max_id Integer,min_bkp_size Integer,min_raw_size Integer,min_actual_size Integer,max_actual_size Integer,min_start_time text,min_end_time text,min_bkp_time text,max_bkp_size Integer,max_raw_size Integer,max_start_time text,max_end_time text,max_bkp_time text )")
	cur.execute("INSERT INTO dist_srv (server_) SELECT distinct server_ FROM hchktbl;")
	cur.execute("UPDATE dist_srv SET (number) = (select count (server_) from hchktbl where dist_srv.server_=hchktbl.server_);")
	cur.execute("UPDATE dist_srv SET (min_id) = (select min(id) from hchktbl where dist_srv.server_=hchktbl.server_);")
	cur.execute("UPDATE dist_srv SET (max_id) = (select max(id) from hchktbl where dist_srv.server_=hchktbl.server_);")
	cur.execute("UPDATE dist_srv SET (min_bkp_size)=(select bkp_size from hchktbl where dist_srv.min_id=hchktbl.id);")
	cur.execute("UPDATE dist_srv SET (max_bkp_size)=(select bkp_size from hchktbl where dist_srv.max_id=hchktbl.id);")
	cur.execute("UPDATE dist_srv SET (min_actual_size)=(select written_size from hchktbl where dist_srv.min_id=hchktbl.id);")
	cur.execute("UPDATE dist_srv SET (min_start_time)=(select start_time from hchktbl where dist_srv.min_id=hchktbl.id);")
	cur.execute("UPDATE dist_srv SET (min_end_time)=(select end_time from hchktbl where dist_srv.min_id=hchktbl.id);")
	cur.execute("UPDATE dist_srv SET (min_bkp_time)=(select bkp_time from hchktbl where dist_srv.min_id=hchktbl.id);")
	cur.execute("UPDATE dist_srv SET (max_actual_size)=(select written_size from hchktbl where dist_srv.max_id=hchktbl.id);")
	cur.execute("UPDATE dist_srv SET (max_start_time)=(select start_time from hchktbl where dist_srv.max_id=hchktbl.id);")
	cur.execute("UPDATE dist_srv SET (max_end_time)=(select end_time from hchktbl where dist_srv.max_id=hchktbl.id);")
	cur.execute("UPDATE dist_srv SET (max_bkp_time)=(select bkp_time from hchktbl where dist_srv.max_id=hchktbl.id);")
	conn.commit()
	conn.close()

def insert_table():
    conn=psycopg2.connect("dbname='arcserve' user='solve1' password='Solve123!' host='172.16.18.162' port='5432'")
    cur=conn.cursor()
    cur.execute("COPY COMPANY FROM 'C:\csvdata\este2.csv' DELIMITER ',' CSV HEADER;")
#    cur.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) VALUES ( 'Paul', 32, 'California', 20000.00 );")
#    cur.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) VALUES ( 'Allen', 25, 'Texas', 15000.00 );")
    conn.commit()
    conn.close()

def view():
	conn=psycopg2.connect("dbname='arcserve' user='solve1' password='Solve123!' host='172.16.18.162' port='5432'")
	cur=conn.cursor()
#	cur.execute("SELECT * FROM company")
	cur.execute("select * from dist_srv order by server_ asc;")
	rows=cur.fetchall()
	conn.close()
	return rows
#create_table()
distinct_server()
print (view())
