import openpyxl

# column名
column_title = ['FirstName', 'LastName']

if __name__ == '__main__':
    '''
    CELL放入值
    '''
    wb = openpyxl.Workbook()
    ws = wb.active

    # 更改默认名称Sheet
    ws.title = 'worksheettitle'

    # column名和值顺序放入单元格中
    rows = [column_title,
            ['Tarou', 'Tanaka'],
            ['Tarou', 'Suzuki'],
            ['Tarou', 'Uchiayama']
            ]
    for row in rows:
        ws.append(row)

    # 保存
    wb.save('example1.xlsx')