import os
import PySimpleGUI as sg
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

user_email = ""
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def open_login_window():
    layout = [
        [sg.Text("Enter your email "), sg.InputText(key='-User-')],
        [sg.Text("Enter your password "), sg.InputText(key='-Pass-',password_char='*')],
        [sg.Button("Login", key='-LOGIN-')]
    ]

    loginWindow = sg.Window("Rose Email Application", layout)

    while True:
        event, values = loginWindow.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '-LOGIN-':
            user_email = values['-User-']
            print("Login pressed")
            print('Gmail Entered ', user_email)
            print('Google Apps Password Entered ', values['-Pass-'])
            #Check for valid email and potentially restore last session

            if (re.fullmatch(pattern, user_email)):
                #close the login window and put user into the email window
                loginWindow.close()
                open_user_window()
            else:
                open_login_error_modal()

def open_login_error_modal():
    layout = [[sg.Text('Incorrect email format, ensure you have a valid gmail')],
                [sg.Text('If Apps password is incorrect, email will fail to send')]]
    window = sg.Window("Email Error", layout, modal=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    window.close()


def open_user_window():
    # All the stuff inside your window.
    layout = [  [sg.Text('Welcome to your E-mail User Application')],
                [sg.Text('Recipients'), sg.InputText(key='-Recipients-')],
                [sg.Text('If multiple recipients separated by a ","')],
                [sg.Text('Subject')],
                [sg.Input(key='-Subject-')],
                [sg.Text('Select file for attachment',font=('Arial Bold', 12), expand_x=True)],
                [sg.Input(enable_events=True, key='-Files-',font=('Arial Bold', 12),expand_x=True), sg.FileBrowse()],
                [sg.Text('If no file to attach leave blank')],
                [sg.Text('Enter Body Text',font=('Arial Bold', 12), expand_x=True)],
                [sg.Multiline(key='-Body-', expand_x=True, expand_y=True, justification='left')],
                [sg.Button('Send', key='-Send-'), sg.Button('Clear')] ]

    # Create the Window
    emailWindow = sg.Window('Rose Email Application', layout, location=(300,200))
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = emailWindow.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        if event == '-Send-':
            print('Recipients: ', values['-Recipients-'])
            print('Subject: ', values['-Subject-'])
            print('Files to attach: ', values['-Files-'])
            print('Body: ', values['-Body-'])
            send_email(values['-Subject-'], values['-Recipients-'], values['-Body-'], values['-Files-'])

    emailWindow.close()

def send_email(subject, recipients, body, Files):
    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['From'] = user_email
    msg['To'] = recipients
    msg.preamble = 'Message sent over SMTP from python gui application'

    msgAlt = MIMEMultipart('alternative')
    msg.attach(msgAlt)

    msgTxt = MIMEText(body)
    msgAlt.attach(msgTxt)

    for file in Files:
        print('File to open: ', file[1:])
        fp = open(file[1:], 'rb')
        msgImg = MIMEImage(fp.read)
        msgImg.add_header('Attachment', '<itsanattachedfile>')
        msg.attach(msgImg)
        fp.close()

    #Easy Rose-Hulman setup to send mail
    # s = smtplib.SMTP('rosehulman-edu01b.mail.protection.outlook.com', 25)
    # s.send_message(msg)

    #Gmail way to send mail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('ljbryant8888@gmail.com', "bflcwxjyffucwdwf")
    server.send_message(msg)
    server.quit()


def main():
    # set the DISPLAY environment variable to the IP address of your Windows machine
    os.environ["DISPLAY"] = "192.168.56.1:0"

    sg.theme('DarkAmber')   # Add a touch of color
    open_login_window()
    # open_user_window() 

if __name__ == "__main__":
    main()