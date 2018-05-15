# Business Classifier

Automate business classification!

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/)
[![Selenium 3.12.0](https://img.shields.io/badge/selenium-3.12.0-yellow.svg)](https://www.seleniumhq.org/)
![Build passing](https://img.shields.io/badge/build-passing-brightgreen.svg)
[![MIT license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/isaiahnields/SearchQueue/blob/master/LICENSE)

## Table of Contents

[Purpose](#purpose)<br />
[Compatibility](#compatibility)<br />
[Set Up](#set-up)<br />
[Functionality](#functionality)<br />
[Use Cases](#use-cases)<br />
[Future Goals](#future-goals)<br />
[iMobile3](#imobile3)

## Purpose

The Business Classifier program is designed to categorize businesses using data from Facebook, Google, and Yelp. It was originally built in order to automate the classification of merchants who use iMobile3's point-of-sale and marketplace software, however it can be used whenever a database of businesses needs to be classified.

## Compatibility

The following code is compatible with Python 3.6 on Windows, Mac OS, and Linux.

## Setup

1. Clone the repository.
2. Run 'pip install -r requirements.txt'.
3. Run main.py with Python 3.6.

## Functionality

After running the program according to the directions above, the window pictured below is displayed. In this section, the functionality of each widget in this window will be explored in depth.
<img src="https://github.com/isaiahnields/BusinessClassifier/blob/master/screenshots/filled-gui.png" align="middle" width="600">

### Input and Output

The following widgets are useful for specifying how input is read and how output is saved.

#### Data File

The Data File widget is for selecting the file that contains the business data.

#### Results File

The Results File widget is for selecting where the results should be saved.

#### Business Name Columns

The Business Name Columns widget is for specifying which columns in the data file contain the name of the business. If columns are to be combined, commas should be used to separate the column numbers. Note: column indexing begins at 0.

#### Business Location Columns

The Business Location Columns widget is for specifying which columns in the data file contain the location of the business. If columns are to be combined, commas should be used to separate the column numbers. Note: column indexing begins at 0.

### API Keys

The following widgets are useful for entering API keys that allow for access to Facebook and Yelp.

#### Facebook Access Token

The Facebook Access Token widget allows a user to enter a Facebok access token. This access token allows the scraper to access the Facebook Graph API. [Learn more](https://developers.facebook.com/docs/facebook-login/access-tokens).

#### GeoNames Username

The GeoNames Username widget allows a user to enter a GeoNames username. This username allows the scraper to access the functionality of GeoNames. [Learn more](http://www.geonames.org/login).

#### Yelp API Key

The Yelp API Key widget allows a user to enter a Yelp API key. This api key allows the scraper to access the functionality of GeoNames. [Learn more](http://www.geonames.org/login).

## iMobile3

For more information on iMobile3, see the link below:

![alt text](https://www.imobile3.com/wp-content/uploads/2015/05/nav-logo-imobile3-dark-2x.png.pagespeed.ce.xYqpQD5-kC.png)

https://www.imobile3.com/
