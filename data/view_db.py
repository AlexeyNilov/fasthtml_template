from data.fastlite_db import DB, prepare_db
from fastcore.utils import hl_md


prepare_db()

t = DB.t.sample
print(hl_md(t.schema, "sql"))

for s in DB.t.sample():
    print(s)
