#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 13:27:39 2021

@author: ruthstam
"""

#--------------------------------IMPORT_FUNCTIONS--------------------------------

# import pandas for data preperation

import pandas as pd 

# import dash for dashboard

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# import plotly for graph

import plotly.express as px

#--------------------------------LOADING--------------------------------

# load bootstrap theme

BS = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/spacelab/bootstrap.min.css"

# image directory

image_emotion = "/assets/none.png"

image_compare = "/assets/0.png"

image_figure = "/assets/0_figure.png"


#--------------------------------IMPORTJSON+SORTDATA--------------------------------

# import json files

df = pd.read_json("simulation_data_prototype_3-a.json")  

#--------------------------------DATA_PREP--------------------------------

# select relevant data

df1 = df.iloc[:8]

df1['vergelijk_getal'] = df1['vergelijk_getal'].astype(int)

# assign variables 

gemeente = df1["gemeente"]

level = df1["level"]

verpakkingen_dag = df1["verpakkingen_dag"]

verpakkingen_maand = df1["verpakkingen_maand"] 

# select rows for interactive figure

nul = df1.loc[df1['verpakkingen_dag'] == 0]

nul = nul.replace({"level": {"none": "Jij", "good2": "Gemiddelde consument", "best1": "Duurzame consument"}})

een = df1.loc[df1['verpakkingen_dag'] == 1]

een = een.replace({"level": {"best1": "Jij", "good2": "Gemiddelde consument", "worst": "Minst duurzame consument"}})
    
twee = df1.loc[df1['verpakkingen_dag'] == 2]

twee = twee.replace({"level": {"best2": "Jij", "good2": "Gemiddelde consument", "best1": "Duurzame consument"}})
    
drie = df1.loc[df1['verpakkingen_dag'] == 3]

drie = drie.replace({"level": {"good1": "Jij", "good2": "Gemiddelde consument", "best1": "Duurzame consument"}})
    
vier = df1.loc[df1['verpakkingen_dag'] == 4]

vier = vier.replace({"level": {"good2": "Gemiddelde consument", "best1": "Duurzame consument"}})
    
vijf = df1.loc[df1['verpakkingen_dag'] == 5]

vijf = vijf.replace({"level": {"bad1": "Jij", "good2": "Gemiddelde consument", "best1": "Duurzame consument"}})
    
zes = df1.loc[df1['verpakkingen_dag'] == 6]

zes = zes.replace({"level": {"bad2": "Jij", "good2": "Gemiddelde consument", "best1": "Duurzame consument"}})
    
zeven = df1.loc[df1['verpakkingen_dag'] == 7]

zeven = zeven.replace({"level": {"worst": "Jij", "good2": "Gemiddelde consument", "best1": "Duurzame consument"}})


# create dataframes for interactive figure

figure_0 = [nul,vier,een]

figure_1 = [een,vier,zeven]

figure_2 = [twee,vier,een]

figure_3 = [drie,vier,een]

figure_4 = [vier,vier,een]

figure_5 = [vijf,vier,een]

figure_6 = [zes,vier,een]

figure_7 = [zeven,vier,een]

figure_0 = pd.concat(figure_0)

# consumption number figure

fig = px.bar(figure_0, x="level", y="verpakkingen_maand", template="simple_white",labels={
                     "verpakkingen_maand": "Aantal geconsumeerde verpakkingen per maand",
                     "level": "Consument"

                 }).update_layout(
    {"plot_bgcolor": "rgba(0, 0, 0, 0)", "paper_bgcolor": "rgba(0, 0, 0, 0)"}, )


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

# user input component 2x
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
                  type="number", min=0, max=20, step=1, 
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

# comparative figure component
    html.Div(
        children=[
            html.Br(),
            dcc.Graph(id="bar_plot",
                      figure=fig)
            ],
            style = {'width': '50%', "display": "inline-block"},
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
        image_filename = "/assets/+.png"
    if number == 4:
        image_filename = "/assets/+.png"
    if number == 5:
        image_filename = "/assets/-.png"
    if number == 6:
        image_filename = "/assets/-.png"
    if number == 7:
        image_filename = "/assets/--.png"
    image_emotion = image_filename
    return image_emotion


# callback packaging materials 

@app.callback(Output("bar_plot", "figure"),
              [Input("packaging_input", "value")])
def return_figure(packaging):
    if packaging == 0: 
            compare_figure = figure_0
    if packaging == 1: 
            compare_figure = figure_1
    if packaging == 2:
            compare_figure = figure_2
    if packaging == 3:
            compare_figure = figure_3
    if packaging == 4:
            compare_figure = figure_4
    if packaging == 5:
            compare_figure = figure_5
    if packaging == 6:
            compare_figure = figure_6
    if packaging == 7:
            compare_figure = figure_7
    compare_figure = pd.concat(compare_figure)
    
    fig = px.bar(compare_figure, x="level", y="verpakkingen_maand", template="simple_white",labels={
                     "verpakkingen_maand": "Aantal geconsumeerde verpakkingen per maand",
                     "level": "Consument"

                 }).update_layout(
    {"plot_bgcolor": "rgba(0, 0, 0, 0)", "paper_bgcolor": "rgba(0, 0, 0, 0)"}, )
    
                     
    return fig


# callback number out of 100

@app.callback(Output('compare_image', "src"),
    [Input('packaging_input', 'value')])
def output_compare_image(number):
    if number == 1:
        image_filename = "/assets/15.png" 
    if number == 2:
        image_filename = "/assets/30.png" 
    if number == 3:
        image_filename = "/assets/45.png"
    if number == 4:
        image_filename = "/assets/60.png"
    if number == 5:
        image_filename = "/assets/75.png"
    if number == 6:
        image_filename = "/assets/90.png"
    if number >= 7:
        image_filename = "/assets/100.png"
    image_compare = image_filename
    
    return image_compare

"""
# callback number out of 100

@app.callback(Output('compare_figure', "src"),
    [Input('packaging_input', 'value')])
def output_compare_figure(number):
    if number == 1:
        image_filename = "/assets/1_figure.png" 
    if number == 2:
        image_filename = "/assets/2_figure.png" 
    if number == 3:
        image_filename = "/assets/3_figure.png"
    if number == 4:
        image_filename = "/assets/4_figure.png"
    if number == 5:
        image_filename = "/assets/5_figure.png"
    if number == 6:
        image_filename = "/assets/6_figure.png"
    if number == 7:
        image_filename = "/assets/7_figure.png"
    image_compare = image_filename
    
    return image_compare
"""

#--------------------------------RUN_APP--------------------------------

if __name__ == '__main__':
    app.run_server(debug=False)
