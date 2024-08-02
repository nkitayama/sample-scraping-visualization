from openpyxl import Workbook

# Excelのワークブックに相当するインスタンスを作成する
workbook = Workbook()

# アクティブのシートを取得する
worksheet = workbook.active

# A1セルからC2セルの範囲に値を入力する
for i, row in enumerate(worksheet['A1':'C2']):
    for j, cell in enumerate(row):
        cell.value = f'{i}_{j}'

# 末尾の行(3行目)に値を入力する
worksheet.append(['2_0', '2_1', '2_2'])

# 行と列を指定したセルの範囲に値を入力する
for i, row in enumerate(worksheet.iter_rows(min_row=4, max_row=5, max_col=4)):
    for j, cell in enumerate(row):
        cell.value = f'{i+3}_{j}'

# 入力した値を取得する
for row in worksheet.values:
    # 改行を出力する
    print()
    for value in row:
        # セルの値を出力する
        print(value, end=' ')

# ワークブックを保存する
workbook.save('accessing_many_cells.xlsx')