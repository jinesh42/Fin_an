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
'''create_table_daily_record=""" CREATE TABLE IF NOT EXISTS DAILY_LOGS (
                          Day integer,
                          Month integer,
                          Year integer,
                           Transport decimal(18,2),
                        Food decimal(18,2),
                        Ex decimal(18,2),
                        Primary key (Day,month,year)
                          
);
"""'''
#cursor.execute("delete from daily_logs_temp")
#cursor.execute(create_table_Fin_agg)
#cursor.execute(create_table_daily_record)
"""df_agg=pd.read_csv('Agg_records.csv',sep=',')
cln_df_agg= df_agg.fillna(value=0)
cln_df_agg.to_sql(name='FIN_AGG',con=con,if_exists='append',index=False)"""

df_dly=pd.read_csv('Daily_records.csv',sep=',')
cln_df_dly= df_dly.fillna(value=0)
cln_df_dly.to_sql(name='DAILY_LOGS_TEMP',con=con,if_exists='replace',index=False)
#cln_df_agg= df_agg.fillna(value=0)
#cln_df_agg.to_sql(name='FIN_AGG',con=con,if_exists='append',index=False)

cursor.execute("insert into daily_logs (Day,Month,Year,Transport,Food,Ex) select * from daily_logs_temp where true on conflict(day,Month,Year) do update set Transport=excluded.Transport,Food=excluded.food,ex=excluded.ex")

cursor.execute("insert into FIN_AGG (Month,Year,Transport,Food,Ex)  select Month,year,sum(Transport) as transport,sum(Food) as food,sum(ex) as ex from daily_logs group by Year,Month on conflict(Month,year) do update set Transport=excluded.Transport,Food=excluded.food,ex=excluded.ex")
cursor.execute("insert into FIN_AGG (Month,Year,Total)  select Month,year, (Transport+Food+Ex) as Total from (select Month,year,sum(Transport) as transport,sum(Food) as food,sum(ex) as ex from daily_logs group by Year,Month) where true on conflict(Month,year) do update set Total=excluded.Total")
con.commit()

con.close()
