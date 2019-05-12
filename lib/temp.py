from utils import create_connection, run_raw_sql, get_db_version, update_db_version, set_up_logger
statements = [
    "CREATE TABLE table2 (row1 VARCHAR(10), row2 INTEGER)",
    "INSERT INTO table1 (row1, row2) VALUES('foo', 'bar')",
    "SELECT * FROM table1",
    "SELECT id, row1 FROM table1 WHERE row1='foo'"

]

DB_URL = 'mysql://root:password@localhost/test'

logger = set_up_logger()

session = create_connection(DB_URL)
result = run_raw_sql(session, statements[1])
for line in result:
    logger.info(line)
