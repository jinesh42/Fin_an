import sqlite3 as sq
from matplotlib import pyplot as py

def addLabel(header,values):
    for i in range(len(header)):
        py.text(i,values[i],values[i])

con=sq.connect('finance.db')
cursor=con.cursor()

cursor.execute("select * from tot_exp_by_year;")
out=cursor.fetchall()
values=[]
header=[]
for i in range(0,len(out)):
    values.append(round(out[i][0],2))
    header.append(out[i][1])
    #py.text(i,round(out[i][0],2),round(out[i][0],2),ha='center')
py.figure(figsize=(6,5))
print(header,values)
py.bar(header,values,width=0.3,align='center')
#addLabel(header,values)

py.xticks(header,fontsize=8)
py.yticks(fontsize=8)
py.title('Total Expenses by year')
py.xlabel('Year',fontweight='bold',fontsize=10)
py.ylabel('Total Expenses', fontweight='bold', fontsize=10)
#addLabel(header,values)
py.savefig("Expenses_by_year.pdf", format="pdf", bbox_inches="tight")
#py.show()



