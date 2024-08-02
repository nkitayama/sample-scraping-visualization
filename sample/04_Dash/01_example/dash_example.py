from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

# アプリの初期化を行う
app = Dash(__name__)

# アプリのレイアウトを作成する
app.layout = html.Div([
    # 見出しを作成する
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    # ドロップダウンを作成する
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    # グラフを作成する
    dcc.Graph(id='graph-content')
])

# コールバック関数に利用する出力と入力を設定する
@callback(
    # 出力をグラフへ行う
    Output('graph-content', 'figure'),
    # 入力をドロップダウンから取得する
    Input('dropdown-selection', 'value')
)
# コールバック関数を定義する
def update_graph(value):
    # ドロップダウンで選択された国のデータを取得する
    dff = df[df.country==value]
    # データを折れ線グラフで返却する
    return px.line(dff, x='year', y='pop')

# アプリを実行する
if __name__ == '__main__':
    app.run(debug=True)