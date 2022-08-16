import sqlite3 as sq
import pandas as pd
con = sq.connect('finance.db')
cursor = con.cursor()
'''create_table_Fin_agg=""" CREATE TABLE IF NOT EXISTS FIN_AGG (
                        Month integer ,
                        Year integer,
                        Total decimal(18,2),
                        Transport decimal(18,2),
                        Food decimal(18,2),
                        Ex decimal(18,2)
); 
"""  '''
create_table_daily_record=""" CREATE TABLE IF NOT EXISTS DAILY_LOGS (
                          Day integer,
                          Month integer,
                          Year integer,
                           Transport decimal(18,2),
                        Food decimal(18,2),
                        Ex decimal(18,2),
                        Primary key (Day,month,year)
                          
);
"""
#cursor.execute(create_table_Fin_agg)
#cursor.execute(create_table_daily_record)
"""df_agg=pd.read_csv('Agg_records.csv',sep=',')
cln_df_agg= df_agg.fillna(value=0)
cln_df_agg.to_sql(name='FIN_AGG',con=con,if_exists='append',index=False)"""
df_dly=pd.read_csv('Daily_records.csv',sep=',')
cln_df_dly= df_dly.fillna(value=0)
cln_df_dly.to_sql(name='DAILY_LOGS',con=con,if_exists='append',index=False)
#cln_df_agg= df_agg.fillna(value=0)
#cln_df_agg.to_sql(name='FIN_AGG',con=con,if_exists='append',index=False)


con.close()