from __future__ import annotations
import re

class SqlParser():
    """
    Parser for sql queries for when you need something very simple and sqlalchemy is one step beyond what you really
    need (aka, a way to store your sql queries somewhere).

    Given a path to a list of sql queries, will split the list in a dictionary of queries, keyed to the title you
    give it. Titles are denoted in the very first line with [example], similar to configparser. Comments are carried
    over within the sql statement. Multiline sql statements can be supported out of the box.

    Beyond being able to parse out a list of sql items, it has a variety of class methods to replace text. Meant to
    modify a query on the fly for WHERE clauses at the moment.

    Examples
    --------
    Parsing a sql file.
    >>> open('f.sql').read() = [example]\n SELECT * FROM some_database;
    >>> q = SqlParser('f.sql').sql
    >>> q['example'] = 'SELECT * FROM some_database'
    """
    def __init__(self, filepath: str=None):
        self._sql = self.parse(filepath)

    @property
    def filepath(self) -> str:
        return self._filepath

    @filepath.setter
    def filepath(self, fp):
        self._filepath = fp

    @property
    def sql(self) -> dict:
        return self._sql

    @sql.setter
    def sql(self, s):
        self._sql = s

    def __str__(self):
        return f'filepath: {self.filepath}, sql: {self.sql.keys()}'

    # parse a new file and return a dict
    def parse(self, filepath: str) -> dict:
        """

        Parameters
        ----------
        filepath

        Returns
        -------
        Dictionary form of parsed file in the filepath.

        """
        if filepath is None:
            self.filepath = 'None'
            self.sql = {}
            return self.sql

        try:
            self.filepath = filepath
            queries = [i.strip() for i in open(filepath).read().split(';') if len(i.strip())>0]

            # set up the compile dictionary
            parsed_file = {}
            NAME_RE = re.compile(r'(?<=\[).+(?=]\n)')
            QUERY_RE = re.compile(r'(?<=\]\n)[\w\W]+')

            for query in queries:
                query_name = NAME_RE.search(query)[0]
                query_sql = QUERY_RE.search(query)[0].strip()
                parsed_file[query_name] = query_sql

            print(parsed_file)
            return parsed_file
        except:
            raise ValueError('Bad config file.')

SqlParser('tests/sample.sql')