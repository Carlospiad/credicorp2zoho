import xlrd
import csv
from datetime import datetime


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
            writer.writerow((
                sh.cell_value(row_index, colx=1), #fecha
                '',
                sh.cell_value(row_index, colx=6)+sh.cell_value(row_index, colx=11),
                sh.cell_value(row_index, colx=16),
                sh.cell_value(row_index, colx=18),
                sh.cell_value(row_index, colx=23)
                ))
