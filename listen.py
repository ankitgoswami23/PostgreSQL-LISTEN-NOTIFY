import asyncio
import psycopg2

# dbname should be the same for the notifying process
conn = psycopg2.connect(host="localhost", dbname="example", user="example", password="example")
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cursor = conn.cursor()
cursor.execute(f"LISTEN match_updates;")

def handle_notify():
    conn.poll()
    for notify in conn.notifies:
        print(notify.payload)
    conn.notifies.clear()

loop = asyncio.get_event_loop()
loop.add_reader(conn, handle_notify)
loop.run_forever()
