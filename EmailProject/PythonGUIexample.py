import os
import PySimpleGUI as sg

# set the DISPLAY environment variable to the IP address of your Windows machine
os.environ["DISPLAY"] = "192.168.56.1:0"

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Welcome to the email')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Clear')] ]

# Create the Window
window = sg.Window('Email Application', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()