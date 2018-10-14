import os
import sys
import psycopg2
import psycopg2.extras

# Receber tipo e nome da tabela como argumento
tipo = sys.argv[1]
table_name = sys.argv[2]
path = os.path.dirname(os.path.realpath(__file__))

print "Baixando dados de " + tipo

# Montar query para extrair todas as colunas desde 2001-JAN
query = "SELECT * FROM %s WHERE yr >= 2001 ORDER BY yr,mon;" % (table_name)
#print(query)
#sys.exit("fim de teste")

# Executar query
conn = psycopg2.connect(host = "172.16.18.162", database = "arcserve", user="solve1",password="Solve123!")
cursor = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
cursor.execute(query)
tabela = cursor.fetchall()
#print(tabela)

# Gravar arquivo com dados
with open('%s/dados/hist_%s.csv' % (path, tipo), 'wb') as f:
	f.write('data,valor\n')
	for linha in tabela:
		# Escrever linha por linha no formato YYYY-MM-01,VALOR
		f.write("%s-%02d-01,%s\n" %(linha[0],int(linha[1]),linha[2]))
