import xlrd
import csv

book = xlrd.open_workbook("data/data.xls")

sh = book.sheet_by_index(0)


with open('data/output.csv', 'w+') as csvout:
    writer = csv.writer(csvout, lineterminator='\n')
#     next(cs, None)  # skip the first row from the reader, the old header
    writer.writerow(['Date', 'Payee','Conepto','Referencia', 'Outflow', 'Inflow']) # write new header
    for rx in range(12,23):
        writer.writerow((
            sh.cell_value(rx, colx=1),
            sh.cell_value(rx, colx=6),
            sh.cell_value(rx, colx=11),
            sh.cell_value(rx, colx=16),
            sh.cell_value(rx, colx=18),
            sh.cell_value(rx, colx=23)
            ))


# print("The number of worksheets is {0}".format(book.nsheets))
# print("Worksheet name(s): {0}".format(book.sheet_names()))
# print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
# print("Cell D30 is {0}".format(sh.cell_value(rowx=20, colx=3)))
# for rx in range(sh.nrows):
#     print(sh.row(rx))

# for rx in range(12,23):
#     print(sh.row(rx))
# with open('data/MovimientosFecha.txt', newline='',encoding='latin-1') as csvfile:
#   with open('data/bgynab.csv', 'w+') as csvout:
#     writer = csv.writer(csvout, lineterminator='\n')
#     cs = csv.reader(csvfile, delimiter=';', quotechar='"')
#     next(cs, None)  # skip the first row from the reader, the old header
#     writer.writerow(['Date', 'Payee','Category','Memo', 'Outflow', 'Inflow']) # write new header
#     for line in cs:
#         writer.writerow((line[0],'','',line[3].replace(",", ""),line[4].replace(",", ""),line[5].replace(",", "")))


# ['Date','Payee','Category','Memo','Outflow','Inflow']
