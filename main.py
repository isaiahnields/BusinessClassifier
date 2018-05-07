from scripts import reader, writer, google, yelp, facebook


# load the data from the businesses that you would like to classify
data = reader.read('data/merchants.csv')

# create a csv file that the results will be written to
results = writer.FileWriter('data/results.csv')

# iterate through the data read from the merchants.csv file
for line in data:

    # if the account is a test account, skip classifying the account
    if line[13] == 'Test':
        break

    # get the business category from Google
    google_result = google.get_category(line[1], line[6])

    # get the business category from Yelp
    yelp_result = yelp.get_category(line[1], line[6])

    # get the business category from Facebook
    facebook_result = facebook.get_category(line[1], line[6])

    # write the data to results.csv
    results.write([line[0], line[1]] + google_result + yelp_result + facebook_result)

    # print the data
    print('Results for ' + line[1] + ': ' +
          "\n    Google: " + google_result[0] + " - " + google_result[1] +
          "\n    Yelp: " + yelp_result[0] + " - " + yelp_result[1] +
          "\n    Facebook: " + facebook_result[0] + " - " + facebook_result[1] + '\n')
