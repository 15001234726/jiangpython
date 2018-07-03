import xlrd


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'/Users/katyjiang/Desktop/6.20mr.xls')
    # 获取所有sheet
    # print(workbook.sheet_names())

    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始
    # sheet1 = workbook.sheet_by_name('sheet1')

    # sheet的名称，行数，列数
    print((sheet1.name, sheet1.nrows, sheet1.ncols))

    # 获取整行和整列的值（数组）
    rows = sheet1.row_values(0) # 获取第_行内容
    # cols = sheet1.col_values(0) # 获取第_列内容
    print(rows)
    # print(cols)

    # 获取单元格内容
    # print(sheet1.cell(0, 4).value)
    print(sheet1.cell(1, 0).value.encode('utf-8'))
    # print(sheet1.cell_value(0,0).encode('utf-8'))
    # print(sheet1.row(0)[0].value.encode('utf-8'))

    # 获取单元格内容的数据类型
    # print(sheet1.cell(0,0).ctype)


if __name__ == '__main__':
    read_excel()


