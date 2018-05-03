import csv


class FileWriter:

    def __init__(self, filename):
        self.file = open(filename, 'w')
        self.writer = csv.writer(self.file, lineterminator='\n')

    def write(self, row):
        self.writer.writerow(row)
        self.file.flush()
