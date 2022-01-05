# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 11:05:05 2022

@author: StannyGoffin
"""
# Module for list selection

import PySimpleGUI as sg

def list_selection(list_name):

    layout = [[sg.Text("Select List")],[sg.Button("Select")],[sg.Button("Add")],
          [sg.Button ('Delete')],[sg.Button("Close")]]

    # Create the window
    window = sg.Window("Minimalogue", layout, icon = "Images/Triangle.ico", finalize=True)
   
    window.bind("<Escape>", "Close")

    window.close()