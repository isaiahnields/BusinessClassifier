from scripts import reader, writer, google, yelp


# load the data from the businesses that you would like to classify
data = reader.read('data/merchants1.csv')

# create a csv file that the results will be written to
results = writer.FileWriter('data/results.csv')

# iterate through the data read from the merchants.csv file
for line in data:
    # get the business category from Google
    google_result = google.get_category(line[1], line[7])

    # get the business category from Yelp
    yelp_result = yelp.get_category(line[1], line[7])

    # write the data to results.csv
    results.write([line[0], line[1], google_result, yelp_result])
