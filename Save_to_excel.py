import mysql.connector
import datetime
# Writing to an excel
# sheet using Python
from xlwt import Workbook
# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

mysqldb = mysql.connector.connect(host="localhost",user="root",password="password",database="students")
cursor = mysqldb.cursor()

cursor.execute("SELECT * FROM employee WHERE salary>4000 AND address  LIKE '% % % %' ")

result = cursor.fetchall()
print(result)

sheet1.write(0, 0, 'emp_id')
sheet1.write(0, 1, 'name')
sheet1.write(0, 2, 'salary')
sheet1.write(0, 3, 'date_of_joining')
sheet1.write(0, 4, 'address')

for i in range(len(result)):
    for j in range(len(result[i])):
        if isinstance(result[i][j], datetime.date):
            sheet1.write(i + 1, j, str(result[i][j]))
        else:
            sheet1.write(i+1, j, result[i][j])

wb.save('xlwt example.xls')


