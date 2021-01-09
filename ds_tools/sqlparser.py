
class SqlParser():
    def __init__(self, filepath: str=None, **kwargs):
        self._sql = self.parse(filepath)

    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, fp):
        self._filepath = fp

    @property
    def sql(self):
        return self._sql

    @sql.setter
    def sql(self, s):
        self._sql = s

    def __str__(self):
        return f'filepath: {self.filepath}, sql: {self.sql.keys()}'

    # parse a new file and return a dict
    def parse(self, filepath: str) -> dict:
        if filepath is None:
            self.filepath = None
            self.sql = {}
            return self.sql

        try:
            self.filepath = filepath

            f = open(filepath).read()

            parsed_file = {'value': f}
            return parsed_file
        except:
            raise FileNotFoundError('File not found.')