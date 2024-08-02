from dash import Dash, dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px

# 適用するCSSファイルを指定する
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# アプリの初期化を行い、CSSファイルを適用する
app = Dash(__name__, external_stylesheets=external_stylesheets)

# CSVファイルを読み込む
df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

# アプリのレイアウトを作成する
app.layout = html.Div([
    html.Div([
        html.Div([
            # ドロップダウンを作成する
            dcc.Dropdown(
                df['Indicator Name'].unique(),
                'Fertility rate, total (births per woman)',
                id='crossfilter-xaxis-column',
            ),
            # ラジオボタンを作成する
            dcc.RadioItems(
                ['Linear', 'Log'],
                'Linear',
                id='crossfilter-xaxis-type',
                labelStyle={'display': 'inline-block', 'marginTop': '5px'}
            )
        ], style={'width': '49%', 'display': 'inline-block'}),

        html.Div([
            # ドロップダウンを作成する
            dcc.Dropdown(
                df['Indicator Name'].unique(),
                'Life expectancy at birth, total (years)',
                id='crossfilter-yaxis-column'
            ),
            # ラジオボタンを作成する
            dcc.RadioItems(
                ['Linear', 'Log'],
                'Linear',
                id='crossfilter-yaxis-type',
                labelStyle={'display': 'inline-block', 'marginTop': '5px'}
            )
        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
    ], style={
        'padding': '10px 5px'
    }),

    html.Div([
        # さまざまな国の環境に関するデータを表示するグラフを作成する
        dcc.Graph(
            id='crossfilter-indicator-scatter',
            hoverData={'points': [{'customdata': 'Japan'}]}
        )
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        # マウスをホバーした国の環境に関する時系列グラフを作成する
        dcc.Graph(id='x-time-series'),
        dcc.Graph(id='y-time-series'),
    ], style={'display': 'inline-block', 'width': '49%'}),

    html.Div(
        # スライダーを作成する
        dcc.Slider(
            df['Year'].min(),
            df['Year'].max(),
            step=None,
            id='crossfilter-year-slider',
            value=df['Year'].max(),
            marks={str(year): str(year) for year in df['Year'].unique()}
        ), 
    style={'width': '49%', 'padding': '0px 20px 20px 20px'})
])

# コールバック関数に利用する出力と入力を設定する
@callback(
    Output('crossfilter-indicator-scatter', 'figure'),
    Input('crossfilter-xaxis-column', 'value'),
    Input('crossfilter-yaxis-column', 'value'),
    Input('crossfilter-xaxis-type', 'value'),
    Input('crossfilter-yaxis-type', 'value'),
    Input('crossfilter-year-slider', 'value')
)
# さまざまな国の環境に関するデータのグラフを作成するコールバック関数を定義する
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    # スライダーで選択した年のデータを抽出する
    dff = df[df['Year'] == year_value]
    # 散布図を作成する
    fig = px.scatter(x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
            y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
            hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])
    # マウスをホバーした際に国名を表示する
    fig.update_traces(customdata=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])
    # x軸のタイトルとグラフの形式を設定する
    fig.update_xaxes(title=xaxis_column_name, type='linear' if xaxis_type == 'Linear' else 'log')
    # y軸のタイトルとグラフの形式を設定する
    fig.update_yaxes(title=yaxis_column_name, type='linear' if yaxis_type == 'Linear' else 'log')
    # レイアウトを設定する
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    # グラフを返却する
    return fig

# マウスをホバーした国の環境に関する時系列グラフを作成する関数を定義する
def create_time_series(dff, axis_type, title):
    # 時系列グラフを作成する
    fig = px.scatter(dff, x='Year', y='Value')
    # 各値を線で結ぶように設定する
    fig.update_traces(mode='lines+markers')
    # x軸のグリッドを非表示にする
    fig.update_xaxes(showgrid=False)
    # y軸のグラフの形式を設定する
    fig.update_yaxes(type='linear' if axis_type == 'Linear' else 'log')
    # タイトルを追加する
    fig.add_annotation(x=0, y=0.85, xanchor='left', yanchor='bottom',
                       xref='paper', yref='paper', showarrow=False, align='left',
                       text=title)
    # レイアウトを設定する
    fig.update_layout(height=225, margin={'l': 20, 'b': 30, 'r': 10, 't': 10})
    # グラフを返却する
    return fig

# コールバック関数に利用する出力と入力を設定する
@app.callback(
    Output('x-time-series', 'figure'),
    Input('crossfilter-indicator-scatter', 'hoverData'),
    Input('crossfilter-xaxis-column', 'value'),
    Input('crossfilter-xaxis-type', 'value'))
# x軸の指標の時系列グラフを作成するコールバック関数を定義する
def update_x_timeseries(hoverData, xaxis_column_name, axis_type):
    # マウスをホバーした国名を取得する
    country_name = hoverData['points'][0]['customdata']
    # マウスをホバーした国のデータを抽出する
    dff = df[df['Country Name'] == country_name]
    dff = dff[dff['Indicator Name'] == xaxis_column_name]
    # グラフのタイトルを作成する
    title = f'<b>{country_name}</b><br>{xaxis_column_name}'
    # 時系列グラフを作成する関数を呼び出し、グラフを返却する
    return create_time_series(dff, axis_type, title)

# コールバック関数に利用する出力と入力を設定する
@app.callback(
    Output('y-time-series', 'figure'),
    Input('crossfilter-indicator-scatter', 'hoverData'),
    Input('crossfilter-yaxis-column', 'value'),
    Input('crossfilter-yaxis-type', 'value'))
# y軸の指標の時系列グラフを作成するコールバック関数を定義する
def update_y_timeseries(hoverData, yaxis_column_name, axis_type):
    # マウスをホバーした国名を取得する
    country_name = hoverData['points'][0]['customdata']
    # マウスをホバーした国のデータを抽出する
    dff = df[df['Country Name'] == country_name]
    dff = dff[dff['Indicator Name'] == yaxis_column_name]
    # 時系列グラフを作成する関数を呼び出し、グラフを返却する
    return create_time_series(dff, axis_type, yaxis_column_name)

# アプリケーションを起動
if __name__ == '__main__':
    app.run(debug=True)
