#module to connect to MSSQL server
import csv
import random
from random import randint
import pyodbc

def create_table():
	server = 'aimbetter\sqlexpress'
	database = 'acmedb'
	username = 'sa'
	password = 'Solve123!'
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("CREATE TABLE acmedb.dbo.archchk_tbl ("
		"data varchar(10),"
		"server varchar(50),"
		"application varchar(50),"
		"backup_size int,"
		"written_size int,"
		"start_time varchar(50),"
		"end_time varchar(50),"
		"bkp_time varchar(50),"
		"clone_size varchar(50),"
		"company varchar(50) NULL,"
		"compression float,"
		"savings int)")
	cnxn=cnxn.commit()
#	cnxn=cnxn.close()
#date;server;application;backup_size;written_size;start;end;bkp_time;clone_size

def insert_table():
	#este modulo importa os dados do arquivo input_data8.csv para a tabela archchk_tbl
	server = 'aimbetter\sqlexpress'
	database = 'acmedb'
	username = 'sa'
	password = 'Solve123!'
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("""BULK INSERT archchk_tbl FROM 'c:\\csvdata\\input_data8.csv' WITH (FIRSTROW = 2,FIELDTERMINATOR = ',',ROWTERMINATOR = '\n', KEEPNULLS);""")
#	cursor.execute("ALTER TABLE archchk_tbl ADD company varchar(10) default 'Alpha'")
	print("Dados Inseridos")
	cnxn=cnxn.commit()
#	cnxn=cnxn.close()
#	list_table()

def update_table(name):
	server = 'aimbetter\sqlexpress'
	database = 'acmedb'
	username = 'sa'
	password = 'Solve123!'
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
#	cursor.execute("UPDATE acmedb.dbo.archchk_tbl SET application='oracle' WHERE application='oracle'",(email,name))
	cursor.execute("UPDATE acmedb.dbo.archchk_tbl SET company=? WHERE company IS NULL",(name))
#	cursor.execute("UPDATE acmedb.dbo.archchk_tbl SET compression=(acmedb.dbo.archchk_tbl.backup_size-acmedb.dbo.archchk_tbl.written_size)/acmedb.dbo.archchk_tbl.backup_size * 100 WHERE compression IS NULL",)
#	cursor.execute("UPDATE acmedb.dbo.archchk_tbl SET savings=acmedb.dbo.archchk_tbl.backup_size-acmedb.dbo.archchk_tbl.written_size WHERE savings IS NULL",)
	cnxn=cnxn.commit()
#	cnxn=cnxn.close()
#	list_table()

def delete_item(name):
	server = 'aimbetter\sqlexpress'
	database = 'acmedb'
	username = 'sa'
	password = 'Solve123!'
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("DELETE FROM acmedb.dbo.archchk_tbl WHERE name=?",(name))
	cnxn=cnxn.commit()
#	cnxn=cnxn.close()
	list_table()

def search_table(name):
	server = 'aimbetter\sqlexpress'
	database = 'acmedb'
	username = 'sa'
	password = 'Solve123!'
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("SELECT * FROM acmedb.dbo.archchk_tbl WHERE application=?",(name))
#	row=cursor.fetchone()
	row=cursor.fetchall()
	cnxn=cnxn.close()
	print(row)


def list_table():
	server = 'aimbetter\sqlexpress'
	database = 'acmedb'
	username = 'sa'
	password = 'Solve123!'
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("SELECT * FROM acmedb.dbo.archchk_tbl")
#	row=cursor.fetchone()
	row=cursor.fetchall()
	cnxn=cnxn.close()
	print(row)

def quantos_tem(name):
	server = 'aimbetter\sqlexpress'
	database = 'acmedb'
	username = 'sa'
	password = 'Solve123!'
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("select count (*) from dbo.archchk_tbl where company=?",(name))
#	row=cursor.fetchone()
	row=cursor.fetchall()
	cnxn=cnxn.close()
	print(row[0])



def out_data(name):
#    res = ['Alpha','Bravo','Charlie']
	server = 'aimbetter\sqlexpress'
	database = 'acmedb'
	username = 'sa'
	password = 'Solve123!'
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("select * from dbo.archchk_tbl where company=?",(name))
	res=cursor.fetchall()
	cnxn=cnxn.close()

    #Assuming res is a flat list
	with open(csvfile, "w") as output:
	    writer = csv.writer(output, lineterminator='\n')
	    for val in res:
	        writer.writerow([val])

	#Assuming res is a list of lists
	with open(csvfile, "w") as output:
	    writer = csv.writer(output, lineterminator='\n')
	    writer.writerows(res)

def lista_cliente():
	server = 'aimbetter\sqlexpress'
	database = 'acmedb'
	username = 'sa'
	password = 'Solve123!'
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("select distinct company from acmedb.dbo.archchk_tbl")
	#	row=cursor.fetchone()
	row=cursor.fetchall()
	cnxn=cnxn.close()
	return(row)

def lista_servers(name):
	server = 'aimbetter\sqlexpress'
	database = 'acmedb'
	username = 'sa'
	password = 'Solve123!'
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("select distinct server from acmedb.dbo.archchk_tbl where company=?",(name))
	#	row=cursor.fetchone()
	row=cursor.fetchall()
	cnxn=cnxn.close()
	return(row)
#	print(row)

def lista_apps(name):
	server = 'aimbetter\sqlexpress'
	database = 'acmedb'
	username = 'sa'
	password = 'Solve123!'
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("select distinct application from acmedb.dbo.archchk_tbl where server=?",(name))
	#	row=cursor.fetchone()
	row=cursor.fetchall()
	cnxn=cnxn.close()
	return(row)
	print(row)

def ajuste_csv(name):
    import pandas as pd
    df1 = pd.read_csv("Z:/Downloads/csvdata/book4_full.csv")
#    total_rows=df1.shape[0]
    #calculate compression
    bkp_size=df1.backup_size
    dsk_size=df1.written_size
    cp=(dsk_size/bkp_size)*100
    df1['customer']=name
    df1['compression']=cp
#    df1['savings']=total_rows*(df1['backup_size']-df1['written_size'])
    df1['savings']=(df1['backup_size']-df1['written_size'])
    df1.to_csv('Z:/Downloads/csvdata/input_data.csv', index=None)

#delete_item("Solve2")
#insert_table("Solve2","Python SQL","solve2.pythonsql@solve.com.br")
#ajuste_csv("49ers")
#create_table()
#insert_table()
#update_table("Bravos")
#search_table("oracle")
#list_table()
quantos_tem("Acme")
#out_data("Bravos")
#lista_cliente("application")
#lista_servers("Acme")
#lista_apps("acme_sqlsrv01")
