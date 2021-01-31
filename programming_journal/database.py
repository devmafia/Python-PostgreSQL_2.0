import sqlite3

connection  = sqlite3.connect("databases/firstone.db")
connection.row_factory = sqlite3.Row


def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (context TEXT, date TEXT);")

# process the data
def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(f"INSERT INTO entries VALUES ('{entry_content}', '{entry_date}');")
        # second option // connection.execute("INSERT INTO entries VALUES (?, ?);", (entry_content, entry_date) )
    #entries.append({"content": entry_content, "date": entry_date})

# display the data
def get_entries():
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor # get the first row and move the cursor to it
