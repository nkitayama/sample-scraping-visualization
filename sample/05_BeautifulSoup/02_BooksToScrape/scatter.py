from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('books_and_categories.csv')

# アプリの初期化を行う
app = Dash(__name__)

# アプリのレイアウトを作成する
app.layout = html.Div([
    html.Div([
        # ドロップタウンを作成する
        dcc.Dropdown(
            df['Category'].unique(),
            'Travel',
            id='category',
            multi=True
        ),
        # グラフを作成する
        dcc.Graph(id='book-scatter'),
    ]),
])

# コールバック関数に利用する出力と入力を設定する
@callback(
    Output('book-scatter', 'figure'),
    Input('category', 'value'),
)
# コールバック関数を定義する
def update_graph(selected_categories):
    # ドロップダウンで1つのみ選択された場合に文字列が渡されるため、リストに変換する
    if isinstance(selected_categories, str):
        selected_categories = [selected_categories]
    # ドロップダウンで選択されたカテゴリのデータを抽出する
    filtered_df = df[df['Category'].isin(selected_categories)]
    # グラフを作成する
    fig = px.scatter(filtered_df, x='Price', y='Star Rating', color='Category', hover_name='Name')
    # グラフを返却する
    return fig

# アプリを実行する
if __name__ == '__main__':
    app.run(debug=True)
