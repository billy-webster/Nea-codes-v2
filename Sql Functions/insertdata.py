import  sqlite3
conn=sqlite3.connect("db.db")


conn.execute("INSERT INTO ACCOUNTS(USERNAME,PASSWORD,EMAIL) VALUES ('billy', '123', 'billywebster2019@outlook.com')");

conn.execute("INSERT INTO ACCOUNTS(USERNAME,PASSWORD,EMAIL) VALUES ('dan', '456','s201027@greenhead.ac.uk')");


conn.commit()

conn.close()


