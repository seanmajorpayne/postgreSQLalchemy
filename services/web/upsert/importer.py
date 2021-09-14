from project import db
import pandas as pd
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base


class CSVImport:

    def __init__(self, fields, table, chunksize=10000, unique_keys=None):
        self.fields = fields
        self.table = table
        self.unique_keys = unique_keys
        self.chunksize = chunksize
        self.base = declarative_base()
        self.metadata = MetaData()
        self.metadata.reflect(bind=db.engine)

    def import_data(self, filename):
        """
        Reads data from a CSV.
        To keep memory low for large files, chunking is used.
        Calls upsert on each chunk for fast database entry.
        """
        chunks = pd.read_csv(
            filename,
            sep=",",
            quotechar='"',
            error_bad_lines=False,
            chunksize=self.chunksize,
        )
        for chunk in chunks:
            chunk = self.organize_chunk(chunk)
            self.upsert(chunk)

    def organize_chunk(self):
        """
        Override with Children Classes
        """
        return []

    def upsert(self):
        """
        Override with Children Classes
        """
        pass