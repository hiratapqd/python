#!/usr/bin/env python

import csv, re
from subprocess import call

infile = 'C:\csvdata\Book4_full.csv'
db = 'arcserve'
table = 'hchktbl'

fh = csv.reader(open(infile, 'r'), delimiter=';', quotechar='"')
headers = fh.next()

def variablize(text, prefix=''):
    if not prefix:
        # if no prefix, move any digits or non-word chars to the end
        parts = re.match('(^[\W\d]*)(.*$)', text).groups()
        text = "%s %s" % (parts[1], parts[0])
    text = ("%s %s" % (prefix, text)).strip().lower()
    text =  re.sub('[\W]', '_', text)
    return re.sub('_*$', '', text)

columns = map(variablize, file(infile).readline().split(','))
columns = map(lambda v: '%s varchar(128)' % v, columns)
queries = [
    "copy %s from '%s' with csv header;" % (table, infile),
]
for q in queries:
    call(['psql','-a','-d',db,'-c',q])
