from scripts import reader, google, yelp
from scripts.writer import FileWriter

data = reader.read('data/merchants.csv')
results = FileWriter('data/results.csv')

for row in data:
    result = [google.get_category(row[1], row[3] + ' ' + row[6]), yelp.get_category(row[1], row[3] + ' ' + row[6])]
    results.write([row[0], row[1]] + result)