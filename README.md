## BusinessClassifier


### Purpose

The BusinessClassifier program is designed to categorize businesses using Google and Yelp data. It was origionally built in order to facilitate and automate the classification of merchants who use iMobile3's point-of-sale and marketplace software. The data produced by this algorithm was then manually translated to SIC codes for iMobile3's internal classification purposes.

### Setup

1. Obtain an API key from Yelp by creating an app (https://www.yelp.com/developers/documentation/v3/authentication).
2. Paste the API key from Yelp into '/data/api_key.txt'.
3. Add the data containing the businesses that you would like to classify to '/data/merchants.csv'.
4. Edit 'main.py' such that the business data is correctly passed into get_category functions.
5. You're done! You can now run 'main.py' and your businesses should begin to be classified.
