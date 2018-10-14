import pyodbc

# Configure the module according to your needs
from datadog import initialize

options = {
    'api_key':'f0288441c48e7cb1b1557e8665f20e1b',
    'app_key':'634a3df6b1cee29a30c31a0a193fae4931a95e76'
}

initialize(**options)

# Use Datadog REST API client
from datadog import api

title = "Arcserve Brazil application is running"
text = 'Another happy customer!'
tags = ['version:1', 'application:web']

api.Event.create(title=title, text=text, tags=tags)


# Use Statsd, a Python client for DogStatsd
from datadog import statsd

# Increment a counter.
statsd.increment('page.views')

# Or ThreadStats, an alternative tool to collect and flush metrics,using Datadog REST API
from datadog import ThreadStats
stats = ThreadStats()
stats.start()
stats.increment('page.views')

def load_initial():
    server = 'localhost'
    database = 'acmedb'
    username = 'sa'
    password = 'Solve123!'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("SELECT DISTINCT company from archchk_tbl")
	#	row=cursor.fetchone()
    row=cursor.fetchall()
    cnxn=cnxn.close()
#    print (row)
    return row

def create_table():
	server = 'localhost'
	database = 'acmedb'
	username = 'sa'
	password = 'Solve123!'
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("CREATE TABLE acmedb.dbo.archchk_tbl ("
		"date date,"
		"server varchar(50),"
		"application varchar(50),"
		"backup_size int,"
		"written_size int,"
		"start_time varchar(50),"
		"end_time varchar(50),"
		"bkp_time varchar(50),"
        "clone_size varchar(50),"
		"company varchar(50))")
	cnxn=cnxn.commit()

def how_many_bkp(name,company):
    server = 'localhost'
    database = 'acmedb'
    username = 'sa'
    password = 'Solve123!'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("select count(server) from acmedb.dbo.archchk_tbl where server=? and company=?", (name,company))
    #	row=cursor.fetchone()
    data=cursor.fetchall()
    cnxn=cnxn.close()
#    for row in data :
#        print (row[0])
#    print(row[0])
    return (data)

def what_servers(company):
    server = 'localhost'
    database = 'acmedb'
    username = 'sa'
    password = 'Solve123!'
#    print('backend',str(company))
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("select distinct server from acmedb.dbo.archchk_tbl where company=?",(company))
    data=cursor.fetchall()
    cnxn=cnxn.close()
    for row in data :
#        print (row[0])
#    print(row)
#    return (row)
        return (data)

def find_first(name,company):
    server = 'localhost'
    database = 'acmedb'
    username = 'sa'
    password = 'Solve123!'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("select min(date) from acmedb.dbo.archchk_tbl where server=? and company=?",(name,company))
    plunkt=cursor.fetchone()
    row=plunkt
#    print(plunkt[0])
    return row

def find_last(name,company):
    server = 'localhost'
    database = 'acmedb'
    username = 'sa'
    password = 'Solve123!'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("select max(date) from acmedb.dbo.archchk_tbl where server=? and company=?",(name,company))
    plakt=cursor.fetchone()
    cnxn=cnxn.close()
    row=plakt
#    print(plakt[0])
    return row




#load_initial()
#create_table()
#how_many_bkp('sqlsrv01','49ers')
#what_servers('49ers')
#find_first('sqlsrv03','49ers')
