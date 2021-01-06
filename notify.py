import time
from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# dbname should be the same for the listening process
conn = connect(host="localhost", dbname="example", user="example", password="example")

cursor = conn.cursor()
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

while True:
    val = time.time()
    cursor.execute(f"NOTIFY match_updates, '{val}';")
    time.sleep(1)
