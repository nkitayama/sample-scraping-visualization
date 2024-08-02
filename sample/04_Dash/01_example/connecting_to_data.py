from dash import Dash, html, dash_table
import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# アプリの初期化を行う
app = Dash(__name__)

# アプリのレイアウトを作成する
app.layout = html.Div([
    # 見出しを作成する
    html.H1(children='My First App with Data'),
    # 表を作成する
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
])

# アプリを実行する
if __name__ == '__main__':
    app.run(debug=True)