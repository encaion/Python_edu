import xlrd
xls = xlrd.open_workbook("file_name.xlsx")
print(xls.sheet_names())
