import xlsxwriter as xd
with open('bill_data.txt','r+') as f:
    a=[]
    for i in range(0,12):
        lines=f.readline() #read
        a.append(lines)

    print(a)
    b=[]
    for i in range(1,len(a)):
        b.append(a[i].split(':'))

print(b)

workb = xd.Workbook('Expense.xlsx')
works = workb.add_worksheet()
header = ['Year','Total','Transport','Food','Others']
c=0
for i in range(0,len(header)):
    works.write(0,c,header[i])
    c+=1
for i in range(0,4):
    b[i][1] = b[i][1].strip()
    print(b[i][1])
    works.write(i+1,0,b[i][0])
    works.write(i+1, 1, b[i][1])

#works.write(1, 1, b[0][1][])
workb.close()


