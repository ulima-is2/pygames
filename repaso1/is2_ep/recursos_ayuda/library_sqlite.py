import dataset

class SQLiteWorker:
    _db = None
    def connect(self, db_name):
        self._db = dataset.connect('sqlite:///%s' % (db_name))

    def insert(self, table_name, data):
        table = self._db[table_name]
        table.insert(data)
