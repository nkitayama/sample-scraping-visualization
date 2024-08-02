from dash import Dash, html, dash_table
import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('books.csv')

# アプリの初期化を行う
app = Dash(__name__)

# アプリのレイアウトを作成する
app.layout = html.Div([
    # 見出しを作成する
    html.H1(children='Books with Data'),
    # 表を作成する
    dash_table.DataTable(
        # セルを複数行に折り返す
        style_data={
            'whiteSpace': 'normal',
            'height': 'auto',
        },
        # セルの余白を設定する
        style_cell={'padding': '10px'},
        # 'Name'カラムを左寄せにする
        style_cell_conditional=[
            {
                'if': {'column_id': 'Name'},
                'textAlign': 'left'
            }
        ],
        # データを指定する
        data=df.to_dict('records'),
        # 表の1ページに表示される行数を設定する
        page_size=10,
    )
])

# アプリを実行する
if __name__ == '__main__':
    app.run(debug=True)