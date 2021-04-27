# Ejercicio 4.17: Fijando ideas
# 4.17Ideas.py

import csv

f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row  = next(rows)

print(row)

types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))

print(record)

