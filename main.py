import iohandler
import scrapers

# load the keys from the businesses that you would like to classify
data = iohandler.reader.read('keys/merchants.csv')

# create a csv file that the results will be written to
results = iohandler.writer.FileWriter('keys/results.csv')

# iterate through the keys read from the merchants.csv file
for line in data:

    # if the account is a test account, skip classifying the account
    if line[13] == 'Test':
        break

    # get the business category from Google
    google_result = scrapers.google.get_category(line[1], line[6])

    # get the business category from Yelp
    yelp_result = scrapers.yelp.get_category(line[1], line[6])

    # get the business category from Facebook
    facebook_result = scrapers.facebook.get_category(line[1], line[6])

    # write the keys to results.csv
    results.write([line[0], line[1]] + google_result + yelp_result + facebook_result)

    # print the keys
    print('Results for ' + line[1] + ': ' +
          "\n    Google: " + google_result[0] + " - " + google_result[1] +
          "\n    Yelp: " + yelp_result[0] + " - " + yelp_result[1] +
          "\n    Facebook: " + facebook_result[0] + " - " + facebook_result[1] + '\n')
