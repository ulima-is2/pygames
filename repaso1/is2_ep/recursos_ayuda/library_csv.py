import csv

class CSVWriter:
    _filename = ""
    _spamwriter = None
    def __init__(self, filename):
        self._filename = filename

    def open(self):
        csvfile = open(self._filename, 'w')
        fieldnames = ['nombre', 'descripcion']
        #self._spamwriter = csv.writer(csvfile, delimiter=' ',
        #                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
        self._spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    def write(self, text_dict):
        self._spamwriter.writerow(text_dict)
