import mysql.connector

# see https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
def connect_db(host, user, password, database):
    cnx = mysql.connector.connect(user=user, password=password,
                                  host=host,
                                  database=database)
    cnx.close()

