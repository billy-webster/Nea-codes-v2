import  sqlite3
conn=sqlite3.connect("db.db")
conn.execute("""
CREATE TABLE ACCOUNTS(
ACCOUNTS_ID INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL ,
USERNAME TEXT NOT NULL, 
PASSWORD TEXT NOT NULL,
EMAIL TEXT NOT NULL)
""")
