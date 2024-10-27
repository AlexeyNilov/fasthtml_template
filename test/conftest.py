import os
import pytest

os.environ["TEMPLATE_DB_PATH"] = "db/test_empty.sqlite"

from sqlite_minutils.db import Database
from data.fastlite_db import recreate_db, DB


@pytest.fixture
def db_with_tables() -> Database:
    recreate_db(DB)
    return DB
