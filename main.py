from scripts import reader, google, yelp
from scripts.writer import FileWriter

data = reader.read('data/merchants.csv') #load the data from the businesses that you would like to classify
results = FileWriter('data/results.csv') #create a csv file that the results will be written to

for row in data: #iterate through the data read from the merchants.csv file
    google_result = google.get_category(row[1], row[3] + ' ' + row[6]) #get the business category from Google
    yelp_result = yelp.get_category(row[1], row[3] + ' ' + row[6]) #get the business category from Yelp
    results.write([row[0], row[1], google_result, yelp_result]) #write the data to results.csv