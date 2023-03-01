"""
2. Styling Dash Apps.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s0L3QA__0jmqlD9QD_uF36IQZywIbZIZ
"""

"""
## Adding logos and notes

While a picture (or a graph!) is worth a thousand words; sometimes there is a need to add more explanatory notes to a dashboard. Luckily you have been working on your skills to add and format text as well as add images and further structure to your Dash apps.

Let's create a dashboard that includes the company logo, a single graph then some brief explanatory notes.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/2bac9433b0e904735feefa26ca913fba187c0d55/e_com_logo.png'
ecom_bar = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)').sort_values(by='Total Sales ($)', ascending=False)
top_country = ecom_bar.loc[0]['Country']            
bar_fig_country = px.bar(ecom_bar, x='Total Sales ($)', y='Country', color='Country', color_discrete_map={'United Kingdom':'lightblue', 'Germany':'orange', 'France':'darkblue', 'Australia':'green', 'Hong Kong':'red'})         
    
app = dash.Dash(__name__)

app.layout = html.Div([
  # Add the company logo
  html.Img(src=logo_link),
  html.H1('Sales by Country'),
  html.Div(dcc.Graph(figure=bar_fig_country), 
           style={'width':'750px', 'margin':'auto'}),
  # Add an overall text-containing component
  html.Span(children=[
    # Add the top country text
    'This year, the most sales came from: ', 
    html.B(top_country),
    # Italicize copyright notice
    html.I(' Copyright E-Com INC')])
    ], 
  style={'text-align':'center', 'font-size':22})

if __name__ == '__main__':
    app.run_server(debug=True)

"""
## Adding an HTML list to Dash

While working at your desk, someone from the Marketing department saw the last little dashboard you produced and have asked you to create one for them. They would like a bar chart of the top categories by total sales amount but with a list below that notes the top few categories for a quick glance.

They also have a few stylistic notes - but they all seem within your knowledge base given your recent work in HTML and Dash.

Your task is to extend the dashboard you created to include a list of the top categories and their sales volume.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/2bac9433b0e904735feefa26ca913fba187c0d55/e_com_logo.png'
ecom_category = ecom_sales.groupby(['Major Category','Minor Category']).size().reset_index(name='Total Orders').sort_values(by='Total Orders', ascending=False).reset_index(drop=True)
num1_cat, num1_salesvol = ecom_category.loc[0].tolist()[1:3]
num2_cat, num2_salesvol = ecom_category.loc[1].tolist()[1:3]
ecom_bar = px.bar(ecom_category, x='Total Orders', y='Minor Category', color='Major Category')
ecom_bar.update_layout({'yaxis':{'dtick':1, 'categoryorder':'total ascending'}})             

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Img(src=logo_link),
    html.H1('Top Sales Categories'),
    html.Div(dcc.Graph(figure=ecom_bar)),
    html.Span(children=[
    'The top 2 sales categories were:',
    # Set up an ordered list
    html.Ol(children=[
      	# Add two list elements with the top category variables
        html.Li(children=[num1_cat, ' with ', num1_salesvol, ' sales volume']),
        html.Li(children=[num2_cat, ' with ', num2_salesvol, ' sales volume'])
    ], style={'width':'350px', 'margin':'auto'}),
    # Add a line break before the copyright notice
    html.Br(),
    html.I('Copyright E-Com INC')])
    ], style={'text-align':'center', 'font-size':22})

if __name__ == '__main__':
    app.run_server(debug=True)

"""
## Styling a Dash app with CSS

It's time to take your dashboards to the next level by unleashing the power of CSS. You have been thinking about ways to spruce up the marketing dashboard you created and have a few ideas to demonstrate to the business stakeholder.

It would be good to adjust the size of the graph and logo, as well as add some nice background colors to various elements. That ought to jazz it up!
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/2bac9433b0e904735feefa26ca913fba187c0d55/e_com_logo.png'
ecom_category = ecom_sales.groupby(['Major Category','Minor Category']).size().reset_index(name='Total Orders').sort_values(by='Total Orders', ascending=False).reset_index(drop=True)
top_cat = ecom_category.loc[0]['Minor Category']
ecom_bar = px.bar(ecom_category, x='Total Orders', y='Minor Category', color='Major Category')
ecom_bar.update_layout({'yaxis':{'dtick':1, 'categoryorder':'total ascending'}, 'paper_bgcolor':'rgb(224, 255, 252)'})         

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Img(src=logo_link,
    # Set the size of the logo
    style={'width':'215px', 'height':'240px'} 
    ),
    html.H1('Top Sales Categories'),
    # Set the size of the bar graph
    html.Div(dcc.Graph(figure=ecom_bar, 
                       style={'width':'500px', 'height':'350px', 'margin':'auto'}),
    ),
    html.Br(),
    html.Span(children=[
    'The top category was: ',
    html.B(top_cat),
    html.Br(),
    html.I('Copyright E-Com INC',
    # Add a background color to the copyright notice
    style={'background-color': 'lightgrey'})])
    # Add a background color to the entire app
    ], style={'text-align':'center', 'font-size':22, 'background-color':'rgb(224,255,252)'})

if __name__ == '__main__':
    app.run_server(debug=True)

"""
## Switching to Darkmode

A common trend in software products and web pages is having a 'Dark Mode', which is easier on the eyes and preferred by some people. Dark Mode is where the background of elements are black, and the text color for everything is white.

Your task is take the dashboard you created in the last exercise and switch it over to the 'dark side'. This will involve changing the background and text color on your graph and HTML elements.

Most of the last dashboard has been provided, including the creation of necessary graphs. However, there is key work to be done to switch over the dashboard to Dark Mode. You can use words for the colors in this exercise rather than RGB codes.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/1c95273e21a54b5ca48e0b03cc0c1faeafb3d7cd/e-comlogo_white.png'
ecom_category = ecom_sales.groupby(['Major Category','Minor Category']).size().reset_index(name='Total Orders').sort_values(by='Total Orders', ascending=False).reset_index(drop=True)
top_cat = ecom_category.loc[0]['Minor Category']
ecom_bar = px.bar(ecom_category, x='Total Orders', y='Minor Category', color='Major Category')

# Set the font color of the bar chart
ecom_bar.update_layout({'yaxis':{'dtick':1, 'categoryorder':'total ascending'}, 'paper_bgcolor':'black', 'font': {'color':'white'}})

app = dash.Dash(__name__)

app.layout = html.Div([
    # Set the new white-text image
    html.Img(src=logo_link,
    style={'width':'165px', 'height':'50px'}),
    html.H1('Top Sales Categories'),
    html.Div(dcc.Graph(figure=ecom_bar,style={'width':'500px', 'height':'350px', 'margin':'auto'})),
    html.Br(),
    html.Span(children=[
    'The top category was: ',
    html.B(top_cat),
    html.Br(),
    html.I('Copyright E-Com INC')])
    ], style={'text-align':'center', 'font-size':22,
              # Update the background color to the entire app
              'background-color':'black',
              # Change the text color for the whole app
              'color':'white'
               })

if __name__ == '__main__':
    app.run_server(debug=True)

"""
## A refined sales dashboard

The e-commerce company from Chapter 1 has called you up and has a budget for you to extend the previous work you did, building a basic proof-of-concept sales dashboard.

Now that you have built your skills in styling and positioning, you can really make this dashboard presentation-worthy.

As a reminder, the company would like a line chart of their total sales each month, a bar chart of their total sales in each country, and a high-level summary statistic around the highest order quantity for the period. However, they would prefer these side-by-side, and their corporate style guide asks for light blue backgrounds. They have requested for there to be two logos, one on either side of the main title, so their brand is nice and prominent.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/fdbe0accd2581a0c505dab4b29ebb66cf72a1803/e-comlogo.png'
ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
ecom_line = ecom_sales.groupby('Year-Month')['OrderValue'].agg('sum').reset_index(name='TotalSales')
line_fig = px.line(data_frame=ecom_line, x='Year-Month', y='TotalSales',title='Total Sales by Month')
line_fig.update_layout({'paper_bgcolor':'rgb(224, 255, 252)' }) 
ecom_bar = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='TotalSales')
bar_fig = px.bar(data_frame=ecom_bar, x='TotalSales', y='Country', orientation='h',title='Total Sales by Country')
bar_fig.update_layout({'yaxis':{'dtick':1, 'categoryorder':'total ascending'}, 'paper_bgcolor':'rgb(224, 255, 252)'}) 

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.Div(children=[
      html.Img(src=logo_link, 
               # Place the logo side-by-side the H1 with required margin
               style={'display':'inline-block', 'margin':'25px'}),
      html.H1(children=['Sales Figures'],
              # Make the H1 side-by-side with the logos
              style={'display':'inline-block'}), 
      html.Img(src=logo_link,
               # Place the logo side-by-side the H1 with required margin
               style={'display':'inline-block', 'margin':'25px'})]),
    html.Div(
        dcc.Graph(figure=line_fig), 
        # Ensure graphs are correct size, side-by-side with required margin
        style={'width':'500px', 'display':'inline-block', 'margin':'5px'}), 
    html.Div(
      	dcc.Graph(figure=bar_fig),
        # Ensure graphs are correct size, side-by-side with required margin
    	style={'width':'350px', 'display':'inline-block', 'margin':'5px'}), 
    html.H3(f'The largest order quantity was {ecom_sales.Quantity.max()}')
    ],style={'text-align':'center', 'font-size':22, 'background-color':'rgb(224, 255, 252)'})

if __name__ == '__main__':
    app.run_server(debug=True)

"""
## Controlling object layout

Your work with Dash is really having an impact in your organization. However, a colleague has contacted you about an issue they are having with one of their dashboards. Their envisioned dashboard has the company logo up the top, followed by two bar charts next to each other.

But the logo is too close to the top, and the graphs are stacked on top of each other. What a mess!

You think you can use your knowledge of CSS to help wrangle these objects into place.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/fdbe0accd2581a0c505dab4b29ebb66cf72a1803/e-comlogo.png'
ecom_bar_major_cat = ecom_sales.groupby('Major Category')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
ecom_bar_minor_cat = ecom_sales.groupby('Minor Category')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
bar_fig_major_cat = px.bar(ecom_bar_major_cat, x='Total Sales ($)', y='Major Category', color='Major Category', color_discrete_map={'Clothes':'blue','Kitchen':'red','Garden':'green','Household':'yellow'})
bar_fig_minor_cat = px.bar(ecom_bar_minor_cat, x='Total Sales ($)', y='Minor Category')                    

app = dash.Dash(__name__)

app.layout = html.Div([
  html.Img(src=logo_link,
        # Add margin to the logo
        style={'margin':'30px 0px 0px 0px'}),
  html.H1('Sales breakdowns'),
  html.Div(children=[
      dcc.Graph(
        # Style the graphs to appear side-by-side
        figure=bar_fig_major_cat,
        style={'display':'inline-block'}),
      dcc.Graph(
        figure=bar_fig_minor_cat,
        style={'display':'inline-block'}),
  ]),
  html.H2('Major Category',
        # Style the titles to appear side-by-side with a 2 pixel border
        style={'display':'inline-block', 'border':'2px solid black',
        # Style the titles to have the correct spacings       
               'padding':'10px', 'margin':'10px 220px'}),
  html.H2('Minor Category',
        # Style the titles to appear side-by-side with a 2 pixel border
        style={'display':'inline-block', 'border':'2px solid black',
        # Style the titles to have the correct spacings 
               'padding':'10px', 'margin':'10px 220px'}),
  
  ], style={'text-align':'center', 'font-size':22})

if __name__ == '__main__':
    app.run_server(debug=True)

