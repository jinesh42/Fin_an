import pandas as pd
import sqlite3 as sq
con = sq.connect('finance.db')

df=pd.read_csv('Daily_records.csv','r')
print(df.head)


