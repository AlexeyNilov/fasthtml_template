import os

os.environ["PUSHUP_DB_PATH"] = "db/test_empty.sqlite"

from sqlite_minutils.db import Database
from data.fastlite_db import recreate_db, DB


@pytest.fixture
def empty_db() -> Database:  # TODO use in mem db?
    recreate_db(DB)
    return DB
