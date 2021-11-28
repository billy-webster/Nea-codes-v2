
import sqlite3

conn = sqlite3.connect('db.db')

cursor = conn.execute("SELECT * from ACCOUNTS")
print("ID\tUSERNAME\tPASSWORD\tEMAIL")
for row in cursor:
   print ("{}\t{}\t\t{}\t\t{}".format(row[0],row[1],row[2],row[3]))
conn.close()
