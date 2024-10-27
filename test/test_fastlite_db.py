import pytest
from sqlite_minutils.db import Database
from fastlite import Table

from data.fastlite_db import (
    create_sample_table,
    prepare_db,
    recreate_db,
    sample_structure,
    TABLES,
)


@pytest.fixture
def mock_db():
    return Database(":memory:")


def test_create_event_table(mock_db):
    sample_table = create_sample_table(mock_db)
    assert isinstance(sample_table, Table)
    assert sample_table.name == "sample"
    assert [col.name for col in sample_table.columns] == list(sample_structure.keys())
    assert sample_table.columns[0].name == "id"
    assert sample_table.columns[0].type == "INTEGER"
    assert sample_table.columns[0].is_pk == 1


def test_prepare_db(mock_db):
    prepare_db(mock_db)
    assert "sample" in [table.name for table in mock_db.tables]


def test_recreate_db(mock_db):
    # First, create some tables
    prepare_db(mock_db)
    assert len(mock_db.tables) > 0

    # Now recreate the database
    recreate_db(mock_db)

    # Check that all tables were dropped and recreated
    assert len(mock_db.tables) == len(TABLES)
    for table_name in TABLES:
        assert table_name in [table.name for table in mock_db.tables]


def test_tables_dict():
    assert "sample" in TABLES
    assert callable(TABLES["sample"])
