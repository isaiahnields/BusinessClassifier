import csv


def read(filename):
    """
    Given a the location of a csv file, this function returns an array of the data.

    :param filename: a string that points to the csv file containing business information
    :return result: an array containing the rows of the csv file
    """

    # opens the csv file and passes the information into the csv reader
    file = open(filename, 'r')
    reader = csv.reader(file)

    # creates an array from the csv file
    result = []
    for row in reader:

        # if there are more than two digits in the business name
        if sum(c.isdigit() for c in row[1]) > 2:

            # remove the digits from the business name
            row[1] = ''.join([i for i in row[1] if not i.isdigit()])

        # add the business information to the result array
        result.append(row)

    # close the file
    file.close()

    return result
