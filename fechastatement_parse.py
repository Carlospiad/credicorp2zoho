import xlrd
import csv

book = xlrd.open_workbook("data/data.xls")

sh = book.sheet_by_index(0)

empty_cell= False
with xlrd.open_workbook("data/data.xls") as wb:
    with open('data/output.csv', 'w+') as csvout:
        cs= wb.sheet_by_index(0)
        num_cols= cs.ncols
        num_rows= cs.nrows
        writer = csv.writer(csvout, lineterminator='\n')
        writer.writerow(['Date', 'Payee','Conepto','Referencia', 'Outflow', 'Inflow']) # write new header
        for row_index in range(12, num_rows):
            writer.writerow((
                sh.cell_value(row_index, colx=1),
                sh.cell_value(row_index, colx=6),
                sh.cell_value(row_index, colx=11),
                sh.cell_value(row_index, colx=16),
                sh.cell_value(row_index, colx=18),
                sh.cell_value(row_index, colx=23)
                ))
            # set count empty cells
            count_empty = 0
            print('Row: {}'.format(row_index))
            for col_index in range(0,num_cols):
                # get cell value
                cell_val= cs.cell(row_index, col_index).value
                # check if cell is empty
                if cell_val== '':
                    # set empty cell is True
                    empty_cell = True
                    # increment counter
                    count_empty+= 1
                else:
                    # set empty cell is false
                    empty_cell= False

                # check if cell is not empty
                if not empty_cell:
                    # print value of cell
                    print('Col #: {} | Value: {}'.format(col_index, cell_val))


            # check the counter if is = num_cols means the whole row is empty
            if count_empty == num_cols:
                print ('Row is empty')
                # stop looping to next rows
                break


# with open('data/output.csv', 'w+') as csvout:
#     writer = csv.writer(csvout, lineterminator='\n')
#     writer.writerow(['Date', 'Payee','Conepto','Referencia', 'Outflow', 'Inflow']) # write new header
#     for rx in range(12,23):
#         writer.writerow((
#             sh.cell_value(rx, colx=1),
#             sh.cell_value(rx, colx=6),
#             sh.cell_value(rx, colx=11),
#             sh.cell_value(rx, colx=16),
#             sh.cell_value(rx, colx=18),
#             sh.cell_value(rx, colx=23)
#             ))


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
