# PythonEmailApplication

This is a Python email application built upon SMTP protocol. It features the ability to send emails to multiiple users and 
add an attachment to the email. To connect to your local email provider use dig -NS with your website (if a school will be your www.school.edu for example) to find mail servers available to you and then use that as the mail host.

For all users ensure you download tkinter and pysimplegui using commands
    python/python3 -m pip install pysimplegui
    sudo apt-get install python3-tk

If running on windows using Ubuntu or some Linux shell follow these instructions to get started:

1. Download Xming on your windows machine and start the X server using instructions here: https://vlaams-supercomputing-centrum-vscdocumentation.readthedocs-hosted.com/en/latest/access/using_the_xming_x_server_to_display_graphical_programs.html 

2. uncomment the os.environ["DISPLAY"] and enter your machines ip like so "Your_ip:0", use ipconfig in commmand prompt to get your machines ip.

If NOT RUNNING ON WINDOWS
comment out the os.environ line