# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 08:58:04 2022

@author: dillo
"""

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
import os.path
import pandas as pd


buttons = [
    
         [sg.Listbox(values=[], size=(20,4), enable_events=True, key='-LIST1-'),
             ],
         [
         sg.In('get data folder',enable_events=True, key = '-output-'),
         sg.FolderBrowse()
         ]
         
         
         
     
    ]


    
    
def create_plot(p):
    import matplotlib.pyplot as plt
    import csv
    import pandas as pd
    path = p
    df = pd.read_csv(path)
    #df = df.iloc[500:1500]
    print(df)
    
    
    plt.plot(df['Hour'], df['Age wear'])
    plt.title('Bmw')
    plt.xlabel('Time(hours)')
    plt.ylabel('Level of wear')
    plt.grid(True)
    return plt.gcf()


fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

matplotlib.use("TkAgg")

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

# Define the window layout
layout = [[
    #[sg.Column(outputColumn, element_justification='left')],
     sg.Frame('inputs', [[
        sg.Column(buttons,vertical_alignment='center', expand_x=True),
        ]],border_width = 0),
    
    
    sg.VSeperator(),
    
    sg.Frame('plot',[[
        sg.Text("Plot test"),
        sg.Canvas(key="-CANVAS-"),
        sg.Button("Ok")
        ]])
             
    ]]

# Create the form and show it without the plot
window = sg.Window(
    "Matplotlib Single Graph",
    layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
)


while True:
    event, values = window.read()
    #if event == sg.WINDOW_CLOSED():
       #break
    if event == "-output-":
        output = values["-output-"]
        try:
            file_list = os.listdir(output)
        except:
            file_list = []
        
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(output,f))
            and f.lower().endswith(".csv")
            ]
        window["-LIST1-"].update(fnames)
    elif event == "-LIST1-":
        try:
            filename = os.path.join(
                values["-output-"], values["-LIST1-"][0])
            window["-CANVAS-"].TKCanvas.delete("all")
            draw_figure(window["-CANVAS-"].TKCanvas,create_plot(filename))
        except:
            pass
            
            
window.close()