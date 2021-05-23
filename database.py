import main
import sqlite3 as sq
con = sq.connect('finance.db')
cursor = con.cursor()
#cursor.execute("Insert into fin_agg  values('March 2019',500.34,259.12,34.45,12.10)")
#con.commit()
row=cursor.execute("select * from fin_agg").fetchall()
print(row)
print(main.b)

