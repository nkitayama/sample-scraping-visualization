from openpyxl.styles import Font
from openpyxl import Workbook

# Excelのワークブックに相当するインスタンスを作成する
workbook = Workbook()
# アクティブのシートを取得する
worksheet = workbook.active

# セルを取得する
a1 = worksheet['A1']
d4 = worksheet['D4']
# セルに値を入力する
a1.value = 'A1'
d4.value = 'D4'
# フォントの色とサイズを設定する
a1.font = Font(color="0000FF", size=20)
# フォントの色とイタリック体を設定する
d4.font = Font(color="FF0000", italic=True)

# ワークブックを保存する
workbook.save('cell_style.xlsx')