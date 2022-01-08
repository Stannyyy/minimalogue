# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 22:39:31 2021

@author: StannyGoffin
"""


# Import packages
import PySimpleGUI as sg
import pandas as pd
from datetime import date
from Receive_email_module import receive_gmail_by_subject_lifenode1994

save_folder = r'C:\Users\StannyGoffin\OneDrive - Smartz\Desktop\Minimalog/'

# Make gui

# Define buttons
lists = ["grocery", 'clothing', "tools"]
layout = [[sg.Text("Select List")],
          [sg.Combo(lists, size = (10,10), key = 'ListSelection')],
          [sg.Text("Add item")],
          [sg.InputText(do_not_clear=False, key='Submit')],
          [sg.Button("Submit",key='Submit')],
          [sg.Button("Remove last item")],
          [sg.Button("Close")]]

# Create the window
window = sg.Window("Minimalogue", layout, icon = "Images/Triangle.ico", finalize=True)
window['Submit'].bind("<Return>", "_Enter")
window.bind("<Escape>", "Close")

# Create an event loop
item_list = {}
for list_ in lists:
    item_list.update({list_:[]}) 
    
while True:
    event, values = window.read()
    print('---')
    print('event: '+str(event))
    print('values: '+str(values))
    print('---')
    # End program if user closes window or
    # presses the OK button
    if "Close" in event or event == sg.WIN_CLOSED :
        break
    elif 'Submit' in event:
        item_list[values['ListSelection']] += [values['Submit']]
        print(item_list)
    elif 'Remove' in event:
        item_list[values['ListSelection']] = item_list[values['ListSelection']][:len(item_list[values['ListSelection']]) -1 ]
        
window.close()

date = date.today()

for list_ in lists:
    data = pd.DataFrame(data =  item_list[list_],columns=[list_])
    data.to_csv(save_folder + list_ + '.csv',sep=';',index=False)
    
