from dash import Dash, dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
import json

# 適用するCSSファイルを指定する
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# アプリの初期化を行い、CSSファイルを適用する
app = Dash(__name__, external_stylesheets=external_stylesheets)

# 整形済みテキスト要素のスタイル情報を作成する
styles = {
    'pre': {
        # 境界線を作成する
        'border': 'thin lightgrey solid',
        # 横方向のスクロールバーを作成する
        'overflowX': 'scroll'
    }
}

# グラフに表示するデータを作成する
df = pd.DataFrame({
    'x': [1,2,1,2],
    'y': [1,2,3,4],
    'customdata': [1,2,3,4],
    'fruit': ["apple", "apple", "orange", "orange"]
})

# グラフを作成する
fig = px.scatter(df, x='x', y='y', color='fruit', custom_data=['customdata'])
# グラフをマウスで操作した際の設定を適用する
fig.update_layout(clickmode='event+select')
# グラフのマーカーのサイズを設定する
fig.update_traces(marker_size=20)

# アプリのレイアウトを作成する
app.layout = html.Div([
    # グラフを作成する
    dcc.Graph(
        figure=fig,
        id='basic-interactions'
    ),
    # 取得したデータを示すコンポーネントを作成する
    html.Div(className='row', children=[
        # マウスをホバーした際に取得したデータを表示する
        html.Div([
            dcc.Markdown('''
                **Hover Data**
                         
                グラフ内の値にマウスをホバーして取得したデータを表示します。
                         '''),
            html.Pre(id='hover-data', style=styles['pre'])
        ], className='three columns'),
        # クリックした際に取得したデータを表示する
        html.Div([
            dcc.Markdown('''
                **Click Data**
                         
                グラフ内の値をクリックして取得したデータを表示します。
            '''),
            html.Pre(id='click-data', style=styles['pre']),
        ], className='three columns'),
        # 矩形ツールなどで選択したデータを表示する
        html.Div([
            dcc.Markdown("""
                **Selection Data**

                グラフのメニューバーから投げ縄ツールまたは矩形ツールを用いて選択したグラフ内の値のデータを表示します。
                また、グラフ内の値をクリックして取得したデータを表示します。
            """),
            html.Pre(id='selected-data', style=styles['pre']),
        ], className='three columns'),
        # 表示された範囲の座標などの情報を表示する
        html.Div([
            dcc.Markdown("""
                **Zoom and Relayout Data**

                グラフをクリック&ドラッグしてズームするか、メニューバーのズームボタンをクリックすることによって、表示された範囲の座標などの情報を表示します。
            """),
            html.Pre(id='relayout-data', style=styles['pre']),
        ], className='three columns')
    ])
])

# コールバック関数に利用する出力と入力を設定する
@callback(
    Output('hover-data', 'children'),
    Input('basic-interactions', 'hoverData')
)
# コールバック関数を定義する
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)

# コールバック関数に利用する出力と入力を設定する
@callback(
    Output('click-data', 'children'),
    Input('basic-interactions', 'clickData'))
# コールバック関数を定義する
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)

# コールバック関数に利用する出力と入力を設定する
@callback(
    Output('selected-data', 'children'),
    Input('basic-interactions', 'selectedData'))
# コールバック関数を定義する
def display_selected_data(selectedData):
    return json.dumps(selectedData, indent=2)

# コールバック関数に利用する出力と入力を設定する
@callback(
    Output('relayout-data', 'children'),
    Input('basic-interactions', 'relayoutData'))
# コールバック関数を定義する
def display_relayout_data(relayoutData):
    return json.dumps(relayoutData, indent=2)

# アプリを実行する
if __name__ == '__main__':
    app.run(debug=True)