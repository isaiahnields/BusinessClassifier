# BusinessClassifier


## Purpose

The BusinessClassifier program is designed to categorize businesses using Google and Yelp data. It was origionally built in order to facilitate and automate the classification of merchants who use iMobile3's point-of-sale and marketplace software. The data produced by this algorithm was manually translated to SIC codes for iMobile3's internal classification purposes.

## Compatibility

The following code is compatible with Python 3.6. The Google maps classification algorithm is only compatible with Windows, Linux, and Mac OS as it requires Selenium in order to control Chrome. The Yelp algorithm directly interfaces with the Yelp API and thus can be run from essentially any Python 3.6 interpreter.

## Setup

1. Clone the repository to your computer and open it with PyCharm.
2. Run 'pip install -r requirements.txt' in terminal to install dependencies.
3. Obtain an API key from Yelp by creating an app (https://www.yelp.com/developers/documentation/v3/authentication).
4. Paste the API key from Yelp into '/data/api_key.txt'.
5. Add the data containing the businesses that you would like to classify to '/data/merchants.csv'.
6. Edit 'main.py' such that the business data is correctly passed into get_category functions.
7. You're done! You can now run 'main.py' and your businesses should begin to be classified.

## iMobile3

For more information on iMobile3, see the link below:

![alt text](https://www.imobile3.com/wp-content/uploads/2015/05/nav-logo-imobile3-dark-2x.png.pagespeed.ce.xYqpQD5-kC.png)

https://www.imobile3.com/
