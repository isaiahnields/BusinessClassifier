import csv


class FileWriter:

    def __init__(self, file_location):
        """
        Opens the file at file_location and creates a csv writer for that file.

        :param file_location: the location of the file that is to be written to
        """

        # opens the file at file_location in write mode
        self.file = open(file_location, 'w')

        # creates a writer to write to the file
        self.writer = csv.writer(self.file, lineterminator='\n')

    def write(self, row):
        """
        Writes a row of data to the csv file at file_location.

        :param row: an array containing the data that will be written to the csv file
        """

        # write the data to the file
        self.writer.writerow(row)

    def close(self):
        """
        Closes the file reader.
        """

        self.file.close()
