#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Prototype_3

This prototype provides a dashboard to test the comparative element feedback. 

"""
#--------------------------------IMPORT_FUNCTIONS--------------------------------

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

#--------------------------------LOADING--------------------------------

# load bootstrap theme

BS = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/spacelab/bootstrap.min.css"

# image directory

image_emotion = "/assets/none.png"

image_compare = "/assets/0.png"

image_figure = "/assets/0_f.png"

#--------------------------------APP_LAYOUT--------------------------------

# load stylesheet in app 
app = dash.Dash(external_stylesheets=[BS])

# open app
app.layout = html.Div(children= [
    
# header component
    html.Div(
        children=[
        html.H1("Verpakkingsmeter"),
        ],
        style = {'width': '50%', 'textAlign': 'center' ,'marginBottom': 50, 'marginTop': 50, 'backgroundColor':''}
        ),

# user input component 
    html.Div(
        children=[
        html.Br(),
        html.P("Waar woon je?"),
        dbc.Select(id="town_input", 
                   options=[{"label": "Amsterdam", "value": "amsterdam"}, 
                            {"label": "Enschede", "value": "enschede"},
                            {"label": "Stavoren", "value": "stavoren"},
                            {"label": "Utrecht", "value": "utrecht"},
                            {"label": "Harderwijk", "value": "harderwijk"},
                            {"label": "Flevoland", "value": "flevoland"},
                            {"label": "Woudenberg", "value": "woudenberg"},
                            {"label": "Brabant", "value": "brabant"},
                            {"label": "Rotterdam", "value": "rotterdam"},
                            {"label": "Tilburg", "value": "tilburg"},
                            {"label": "Deventer", "value": "deventer"},
                            {"label": "Driebergen", "value": "driebergen"},
                            {"label": "Rhenen", "value": "rhenen"},
                            {"label": "Veenendaal", "value": "veenendaal"},
                            {"label": "Zeewolde", "value": "zeewolde"}],
                   placeholder="Selecteer waar je woont"),
            html.Br(),
            html.Br(),
            html.P("Hoeveel verpakkingen heb je vandaag gebruikt of gebruik je gemiddeld in een dag?"),
            dbc.Input(id="packaging_input", 
                  type="number", min=0, max=15, step=1, 
                  placeholder="Voer een nummer in",),
            ],
            style = {'width': '50%', 'textAlign': 'center', "display": "inline-block"},
            className = ""
            ),

# emoticon image component
     html.Div(
         children=[
         html.Img(id="emotion_image",
                     src= image_emotion)
         ],
         style = {'width': '50%', 'textAlign': 'center' ,'marginBottom': 50, 'marginTop': 60},
         className = ""
         ),

# comparative information component
     html.Div(
         children=[
         html.Img(id="compare_image",
                     src= image_compare)
         ],
         style = {'width': '50%', 'textAlign': 'center' ,'marginBottom': 50, 'marginTop': 60},
         className = ""
         ),

# comparative information component
     html.Div(
         children=[
         html.Img(id="compare_figure",
                     src= image_figure)
         ],
         style = {'width': '50%', 'textAlign': 'center' ,'marginBottom': 50, 'marginTop': 60},
         className = ""
         ),

], 
    
)# close general Div user input
                    
                
#--------------------------------CALLBACKS_APP--------------------------------

# callback user input town

@app.callback(Output("bar_plot", "children"), 
              [Input("town_input", "value")])
def output_text(town):
    return town

# callback user input packaging number

@app.callback(Output("packaging_numb", "children"), 
              [Input("packaging_input", "value")])
def output_number(number):
    return number

# callback emotion icon

@app.callback(Output('emotion_image', "src"),
    [Input('packaging_input', 'value')])
def output_emotion_image(number):
    if number == 1:
        image_filename = "/assets/++.png"
    if number == 2:
        image_filename = "/assets/++.png"
    if number == 3:
        image_filename = "/assets/++.png"
    if number == 4:
        image_filename = "/assets/+.png"
    if number == 5:
        image_filename = "/assets/+.png"
    if number == 6:
        image_filename = "/assets/+.png"
    if number == 7:
        image_filename = "/assets/+-.png"
    if number == 8:
        image_filename = "/assets/+-.png"
    if number == 9:
        image_filename = "/assets/+-.png"
    if number == 10:
        image_filename = "/assets/-.png"
    if number == 11:
        image_filename = "/assets/-.png"
    if number == 12:
        image_filename = "/assets/-.png"
    if number == 13:
        image_filename = "/assets/--.png"
    if number == 14:
        image_filename = "/assets/--.png"
    if number == 15:
        image_filename = "/assets/--.png"
    image_emotion = image_filename
    return image_emotion

# callback score element

@app.callback(Output('compare_image', "src"),
    [Input('packaging_input', 'value')])
def output_compare_image(number):
    if number == 1:
        image_filename = "/assets/20.png"
    if number == 2:
        image_filename = "/assets/20.png"
    if number == 3:
        image_filename = "/assets/20.png"
    if number == 4:
        image_filename = "/assets/40.png"
    if number == 5:
        image_filename = "/assets/40.png"
    if number == 6:
        image_filename = "/assets/40.png"
    if number == 7:
        image_filename = "/assets/60.png"
    if number == 8:
        image_filename = "/assets/60.png"
    if number == 9:
        image_filename = "/assets/60.png"
    if number == 10:
        image_filename = "/assets/80.png"
    if number == 11:
        image_filename = "/assets/80.png"
    if number == 12:
        image_filename = "/assets/80.png"
    if number == 13:
        image_filename = "/assets/100.png"
    if number == 14:
        image_filename = "/assets/100.png"
    if number == 15:
        image_filename = "/assets/100.png"
    image_compare = image_filename
    
    return image_compare

# callback compare figure

@app.callback(Output('compare_figure', "src"),
    [Input('packaging_input', 'value')])
def output_compare_figure(number):
    if number == 1:
        image_filename = "/assets/1_f.png"
    if number == 2:
        image_filename = "/assets/2_f.png"
    if number == 3:
        image_filename = "/assets/3_f.png"
    if number == 4:
        image_filename = "/assets/4_f.png"
    if number == 5:
        image_filename = "/assets/5_f.png"
    if number == 6:
        image_filename = "/assets/6_f.png"
    if number == 7:
        image_filename = "/assets/7_f.png"
    if number == 8:
        image_filename = "/assets/8_f.png"
    if number == 9:
        image_filename = "/assets/9_f.png"
    if number == 10:
        image_filename = "/assets/10_f.png"
    if number == 11:
        image_filename = "/assets/11_f.png"
    if number == 12:
        image_filename = "/assets/12_f.png"
    if number == 13:
        image_filename = "/assets/13_f.png"
    if number == 14:
        image_filename = "/assets/14_f.png"
    if number == 15:
        image_filename = "/assets/15_f.png"
    image_compare = image_filename
    
    return image_compare


#--------------------------------RUN_APP--------------------------------

if __name__ == '__main__':
    app.run_server(debug=False)
