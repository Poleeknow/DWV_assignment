import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import numpy as np


data = pd.read_csv('anime.csv', index_col=0)
data.sort_values(by=['itm_title', 'russian_title', 'year'], ignore_index=True, inplace=True)

lables = data['status'].value_counts().sort_index(ascending=True).to_frame()
print(lables)

# pie = px.pie(lables, values='status', names=lables.index, hole=.3, height=500)
# pie.update_traces(textposition='outside', textinfo='label+percent', textfont_size=20,
#                   marker=dict(colors=['mediumturquoise', 'darkorange'], line=dict(color='#000000', width=3)))
# pie.update_layout(annotations=[dict(text='Status of anime', x=0.5, y=0.5, font_size=22, showarrow=False)], legend=dict(x=0.8, y=0.5, title='Status:', font=dict(size=30),  bgcolor="LightGray", bordercolor="Black", borderwidth=3))

# ganres = dict(zip(data.columns[6:], [0]*len(data.columns[6:])))
# for d in data.columns[6:]:
#     ganres[d] = data[d].value_counts()[True]

# ganres = pd.DataFrame.from_dict(ganres, orient='index', columns=['amount'])

# fig = px.bar(ganres, x=ganres.index, y='amount', color='amount', text_auto=True, height=600, title='Anime genres', labels={'index':''})
# fig.update_traces(textfont_size=10, textangle=0, textposition="outside", cliponaxis=False)
# fig.update_layout(xaxis_tickangle=-45)

# data3 = []
# rat_col = sorted(data['rating'].unique(), reverse=True)
# y_col = sorted(data['year'].unique())
# print(data['rating'])
# print(len(rat_col), len(y_col))
# for rating in rat_col:
#     for year in y_col:
#         data3.append(data[data['rating'] == rating][data['year'] == year].count()[0])
# data3 = np.array(data3).reshape((len(rat_col), len(y_col)))

# years = sorted(data['year'].unique())
# years = list(map(str, years))
# ratings = sorted(data['rating'].unique(), reverse=True)
# ratings = list(map(str, ratings))

# hitmap = px.imshow(data3, text_auto=True, labels={'x' : 'year', 'y' : 'rating', 'color' : 'amount of animes'}, x=years, y=ratings, height=600)



# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div(children=[
#     html.H1(
#         children='Anime Statistics',
#         style={
#             'textAlign': 'center',
#             'color': 'black'
#         }
#         ),

#     html.Div([html.P(children='The data was collected from:'), html.A(children='Anime 365 Catalog', href='https://smotret-anime.com/anime')], style={'text-align':'center'}),

#     html.Div([
#         dcc.Graph(
#             id='first-graph',
#             figure=fig,
#             style={'text-align': 'center'}
#         )
#     ]),

#     html.Div([
#         dcc.Graph(
#             id= 'second-graph', 
#             figure=pie,
#             # style={'text-align': 'center', 'heigth' : '200'}
#         )
#     ],
#     style={'text-align': 'center', 'heigth' : '200'}
#     ),

#     html.Div([
#         dcc.Graph(
#             id= 'third-graph', 
#             figure=hitmap,
#             style={'text-align': 'center'}
#         )
#     ])
# ])
# app.run_server(debug=False, port=9999, host='localhost')