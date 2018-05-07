import csv


class FileReader:

    def __init__(self, file_location):
        """
        Opens the file at file location and creates a csv reader for that file.

        :param file_location: the location of the file that is to be read
        """

        # open the csv file located at file_location in read mode
        file = open(file_location, 'r')

        # create a reader that reads from the file
        self.reader = csv.reader(file)

    def __iter__(self):
        """
        A necessary method for creating an iterable. Returns the iterable itself.

        :return self: the iterable object itself
        """

        # return the iterator
        return self

    def next(self):
        """
        Returns the next object in the iterator.

        :return next: the next object in the iterator
        """

        # return the next object in the iterator
        return next(self.reader)
