import os
import PySimpleGUI as sg
import re

smtp_host = ""
name = ""
user_email = ""

def open_login_window():
    layout = [
        [sg.Text("Enter your email "), sg.InputText()],
        [sg.Text("Enter your password "), sg.InputText()],
        [sg.Button("Login", key='-LOGIN-')]
    ]

    loginWindow = sg.Window("Rose Email Application", layout)

    while True:
        event, values = loginWindow.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '-LOGIN-':
            print("Login pressed")
            print('Rose Email Entered ', values[0])
            print('Password Entered ', values[1])
            #Check for valid Rose email and potentially restore last session

            #hide the login window and put user into the email window
            # loginWindow.hide() could potentially hide and then allow re login or exit from login screen
            loginWindow.close()
            open_user_window()
        


def open_user_window():
    # All the stuff inside your window.
    layout = [  [sg.Text('Welcome to your E-mail User Application')],
                [sg.Text('Enter Name to Show as Sender'), sg.InputText()],
                [sg.Text('Recipients'), sg.InputText()],
                [sg.Text('If multiple recipients separated by a ","')],
                [sg.Text('Select file for attachment',font=('Arial Bold', 12), expand_x=True)],
                [sg.Input(enable_events=True, key='-IN-',font=('Arial Bold', 12),expand_x=True), sg.FileBrowse()],
                [sg.Text('If no file to attach leave blank')],
                [sg.Text('Enter Body Text',font=('Arial Bold', 12), expand_x=True)],
                [sg.Button('Send'), sg.Button('Clear')] ]

    # Create the Window
    emailWindow = sg.Window('Rose Email Application', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = emailWindow.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        # if event == 
        print('You entered ', values[0])
        print('You entered ', values[1])

    emailWindow.close()


def main():
    # set the DISPLAY environment variable to the IP address of your Windows machine
    os.environ["DISPLAY"] = "192.168.56.1:0"

    sg.theme('DarkAmber')   # Add a touch of color
    open_login_window();
    # open_user_window();
    

if __name__ == "__main__":
    main()