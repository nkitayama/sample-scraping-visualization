from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# CSVファイルを読み込む
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# アプリの初期化を行う
app = Dash(__name__)

# アプリのレイアウトを作成する
app.layout = html.Div([
    # アプリの概要を示すコンポーネントを作成する
    html.Div(children='My First App with Data and a Graph'),
    # 表を作成する
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    # グラフを作成する
    dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))
])

# アプリを実行する
if __name__ == '__main__':
    app.run(debug=True)