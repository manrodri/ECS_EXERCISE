from utils import create_connection, run_raw_sql, get_db_version, update_db_version

statements = [
    "CREATE TABLE table2 (row1 VARCHAR(10), row2 INTEGER)",
    "INSERT INTO table1 (row1, row2) VALUES('foo', 'bar')",
    "SELECT * FROM table1",
    "SELECT id, row1 FROM table1 WHERE row1='foo'"

]

DB_URL = 'mysql://root:password@localhost/test'


