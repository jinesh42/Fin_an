import xlsxwriter as xd
import pandas as pd
#workbook = xd.Workbook('Expense.xlsx')openpyxl,index_col=0,
dataw = pd.ExcelWriter('Expense.xlsx',engine='xlsxwriter')
data=pd.read_excel('Expense.xlsx',index_col=0,engine='openpyxl')

data.to_excel(dataw, sheet_name='Sheet1')
wbook = dataw.book #get a workbook
works = dataw.sheets['Sheet1']
chart = wbook.add_chart({'type':'column'}) #to make charts
chart.set_legend({'position': 'none'}) #do not want to set legend
chart.set_size({'width': 620, 'height': 476})
chart.add_series({'name': 'Total','categories': '=Sheet1!$A$2:$A$5','values':'=Sheet1!$B$2:$B$5'}) # name the x axis for which we specifing value
chart.set_x_axis({'name':'Months of 2019','name_font': {'size': 14, 'bold': True},'crossing':0,'num_font':  {'rotation': 25}})
chart.set_y_axis({'name':'Total Amount in (Rs)','name_font': {'size': 14, 'bold': True},'crossing':0,'min':0})  #,'major_unit':500
works.insert_chart('H3',chart)

dataw.save()
