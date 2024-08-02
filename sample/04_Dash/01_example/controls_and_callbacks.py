from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# CSVファイルを読み込む
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# アプリの初期化を行う
app = Dash(__name__)

# アプリのレイアウトを作成する
app.layout = html.Div([
    # アプリの概要を示すコンポーネントを作成する
    html.Div(children='My First App with Data, Graph, and Controls'),
    # 水平線を作成する
    html.Hr(),
    # ラジオボタンを作成する
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
    # 表を作成する
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    # グラフを作成する
    dcc.Graph(figure={}, id='controls-and-graph')
])

# コールバック関数に利用する出力と入力を設定する
@callback(
    # 出力をグラフへ行う
    Output('controls-and-graph', 'figure'),
    # 入力をラジオボタンから取得する
    Input('controls-and-radio-item', 'value')
)
# コールバック関数を定義する
def update_graph(col_chosen):
    # ラジオボタンで選択された大陸のデータを取得して、ヒストグラムとする
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    # ヒストグラムを返却する
    return fig

# アプリを実行する
if __name__ == '__main__':
    app.run(debug=True)