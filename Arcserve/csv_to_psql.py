import psycopg2
import csv

def ajuste_csv(name):
    import pandas as pd
    df1 = pd.read_csv("c:/csvdata/book4_full.csv")
#    total_rows=df1.shape[0]
    #calculate compression
    bkp_size=df1.backup_size
    dsk_size=df1.written_size
    cp=(dsk_size/bkp_size)*100
    df1['customer']=name
    df1['compression']=cp
#    df1['savings']=total_rows*(df1['backup_size']-df1['written_size'])
    df1['savings']=(df1['backup_size']-df1['written_size'])
    df1.insert(0, 'id', range(1, len(df1)+1))
    #print(df1[index])
    df1.to_csv('c:/csvdata/input_data.csv', index=None)


def insert_table():
    ajuste_csv("Acme")
    #f = open(r'C:\csvdata\Book4_full.csv', 'r')
    conn=psycopg2.connect("dbname='arcserve' user='solve1' password='Solve123!' host='172.16.18.162' port='5432'")
    cur=conn.cursor()
    cur.execute("COPY hchktbl FROM 'C:/csvdata/input_data.csv' DELIMITER ',' CSV HEADER;")
    conn.commit()
    conn.close()

def view_table():
    conn=psycopg2.connect("dbname='arcserve' user='solve1' password='Solve123!' host='172.16.18.162' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM hchktbl")
    rows=cur.fetchall()
    conn.close()
    return rows

def last_row():
    conn=psycopg2.connect("dbname='arcserve' user='solve1' password='Solve123!' host='172.16.18.162' port='5432'")
    cur=conn.cursor()
    cur.execute("select count(id) from hchktbl;")
    blar=cur.fetchall()
    conn.commit()
    conn.close()
    print (blar[0])
    return blar

    #COPY sample_table FROM 'C:\tmp\sample_data.csv' DELIMITER ',' CSV HEADER;
    #cur.copy_from(f, hchktbl, sep=';')
    #f.close()
#ajuste_csv("Acme")
#insert_table()
#print(view_table())
last_row()
