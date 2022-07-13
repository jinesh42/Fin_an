import sqlite3 as sq
con = sq.connect('finance.db')
cursor = con.cursor()
create_table_Fin_agg=""" CREATE TABLE IF NOT EXISTS FIN_AGG (
                        Month integer ,
                        Year integer,
                        Total decimal(18,2),
                        Transport decimal(18,2),
                        Food decimal(18,2),
                        Ex decimal(18,2)
); 
"""  
cursor.execute(create_table_Fin_agg)