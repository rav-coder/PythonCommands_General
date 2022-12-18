
# Database connection

import sqlite3

conn = sqlite3.connect("example1.db")
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXIST EMP(ID INT PRIMARY KEY, NAME TEXT, SALARY REAL)""")
c.execute("INSERT INTO EMP(ID,NAME,SALARY) VALUES(101,'ABC', 1000")

conn.execute("COMMIT")

c.execute(""" SELECT * FROM EMP """)
print(next(c))

for row in c:
	print(row)

c.execute("UPDATE EMP SET SALARY= 2000 WHERE ID=101")

c.execute(""" DELETE FROM EMP WHERE ID= 101""")

conn.execute("COMMIT")
