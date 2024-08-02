from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
import csv

# Excelのワークブックに相当するインスタンスを作成する
workbook = Workbook()

# アクティブのシートを取得する
worksheet = workbook.active

# CSVファイルを読み込む
with open('books_and_categories.csv', 'r', newline='', encoding='utf-8') as csvfile:
    # CSVファイルのデータを読み込む
    csv_reader = csv.reader(csvfile)
    # データのヘッダーをシートに入力する
    worksheet.append(next(csv_reader))

    # データを行ごとにループする
    for row in csv_reader:
        # 価格と評価レートの値を文字列から数値へ変換する
        row[1] = float(row[1])
        row[2] = int(row[2])
        # データをシートに入力する
        worksheet.append(row)

# テーブルの名前と範囲を指定する
table = Table(displayName="Books", ref="A1:D1001")
# テーブルスタイルを設定する
style = TableStyleInfo(name="TableStyleMedium9")
# テーブルスタイルを適用する
table.tableStyleInfo = style
# シートにテーブルを追加する
worksheet.add_table(table)

# ワークブックを保存する
workbook.save('connecting_to_data.xlsx')