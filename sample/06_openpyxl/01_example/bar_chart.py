from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

# Excelのワークブックに相当するインスタンスを作成する
workbook = Workbook()

# アクティブのシートを取得する
worksheet = workbook.active
# データを作成する
popData = [["country", "continent", "pop"], ["Afghanistan", "Asia", 31889923.0], ["Albania", "Europe", 3600523.0], ["Algeria", "Africa", 33333216.0]]
# セルに値を入力する
for row in popData:
    worksheet.append(row)

# グラフ形式を棒グラフに設定する
chart = BarChart()
# 縦棒グラフとする
chart.type = "col"
# グラフのタイトルを設定する
chart.title = "gapminder"
# y軸のタイトルを設定する
chart.y_axis.title = 'pop'
# x軸のタイトルを設定する
chart.x_axis.title = 'country'
# 凡例をなしとする
chart.legend = None

# グラフに描画するデータの参照範囲を指定する
data = Reference(worksheet, min_col=3, min_row=2, max_row=4, max_col=3)
# グラフにデータを設定する
chart.add_data(data)
# グラフに描画するカテゴリの参照範囲を指定する
categories = Reference(worksheet, min_col=1, min_row=2, max_row=4, max_col=1)
# グラフにカテゴリを設定する
chart.set_categories(categories)

# シートにグラフを追加する
worksheet.add_chart(chart, 'E1')

# ワークブックを保存する
workbook.save('bar_chart.xlsx')