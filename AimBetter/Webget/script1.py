import psycopg2
import csv


def view():
#	conn=psycopg2.connect("dbname='roiaimbetter' user='solve1' password='Solve123!' host='localhost' port='5432'")
	conn=psycopg2.connect('postgres://szktdjccnybwae:d11900f5c5772e2c4a2cbc0145cb5ac8ef0ce61e6f5723e57851729a262de39e@ec2-23-23-226-190.compute-1.amazonaws.com:5432/d5r1reiru2d3ff?sslmode=require')
	cur=conn.cursor()
	cur.execute("select * from data")
#	cur.execute("COPY data TO 'c:/csvdata/roi_output_data.csv' DELIMITER ',' CSV HEADER;")
	rows=cur.fetchall()
	conn.close()
	csvfile="c:/csvdata/roi_output_data.csv"
	with open(csvfile, 'w') as f:
	    writer = csv.writer(f, delimiter=';')
	    for row in rows:
	        writer.writerow(row)
	return rows

print (view())
