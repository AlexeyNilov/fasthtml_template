import os
from typing import Callable
from typing import Dict

import fastlite as fl
from sqlite_minutils.db import Database


db_path = os.environ.get("TEMPLATE_DB_PATH", "db/template.sqlite")
DB: Database = fl.database(db_path)


sample_structure = dict(
    id=int,
    time=str,
    user_id=int,
    text=str,
)


def create_sample_table(db=DB) -> fl.Table:
    event = db.t.event
    if event not in db.t:
        event.create(sample_structure, pk="id")
    return event


TABLES: Dict[str, Callable] = {
    "sample": create_sample_table,
}


def prepare_db(db: Database = DB):
    for create_func in TABLES.values():
        create_func(db)


def recreate_db(db: Database = DB):
    for t in db.tables:
        t.drop()

    prepare_db(db=db)