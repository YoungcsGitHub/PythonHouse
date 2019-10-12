import openpyxl

if __name__ == '__main__':
    wb = openpyxl.Workbook()
    ws = wb.active

    ws.title = 'WorkSheetTitle'

    # 设置Font
    font = openpyxl.styles.Font(name = '宋体', size = 15)

    a1 = ws['A1']
    a1.font = font
    a1.value = 'Test'

    wb.save('example3.xlsx')
