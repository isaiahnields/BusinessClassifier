import csv


def read(filename):
    """Given a the location of a csv file, this function returns an array of the data.
    Args:
        filename (str): The location of the file on the computers storage device.
    Returns:
        array: The data in the csv file in the form of an array."""
    file = open(filename, 'r')
    reader = csv.reader(file)
    result = [row for row in reader]
    return result
