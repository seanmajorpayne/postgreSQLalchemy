import pandas as pd
from upsert.importer import CSVImport
from project.models.nfl import NFL

class Upsert(CSVImport):
    """
    Performs a fast & efficient upsert on PostgreSQL using the sample NFL data.
    """
    def organize_chunk(self, chunk):
        """
        Chunks may contain null values which should be replaced with None.
        Pandas and SQLalchemy do not play nice with column ordering, so this
        has to be manually specified.
        """
        chunk = chunk.where(pd.notnull(chunk), None)
        chunk = chunk.dropna(axis=0, subset=["gameKey", "player", "time"])
        chunk = chunk[
            [
                "gameKey", "playID", "player", "time",
                "x", "y", "s", "a",
                "dis", "o", "dir", "event"
            ]
        ]
        return chunk.values.tolist()

    def upsert(self, chunk):
        """
        Performs a Postgresql Upsert.
        Will update all columns based on the provided primary keys.
        """
        table = self.metadata.tables.get(self.table)
        update_cols = [c.name for c in table.c if c not in self.unique_keys]
        stmt = postgresql.insert(table).values(chunk)

        on_conflict_stmt = stmt.on_conflict_do_update(
            index_elements=self.unique_keys,
            set_={k: getattr(stmt.excluded, k) for k in update_cols},
        )
        db.session.execute(on_conflict_stmt)
        db.session.commit()


def perform_upsert():
    """
    Table column names and unique keys (the values which shouldn't be updated)
    are pulled from the table and provided to the Upsert operation.
    """
    fields = NFL.__table__.columns.keys()
    #fields_to_remove = ["created_at", "updated_at"]
    #for field in fields_to_remove:
    #    fields.remove(field)
    fields = ",".join(fields)
    unique_keys = ["game_key", "player", "time"]
    upsert = Upsert(
        fields=fields,
        table="nfl",
        chunksize=10000,
        primary_keys=unique_keys,
    )
    upsert.import_data(filename="train_player_tracking.csv")
