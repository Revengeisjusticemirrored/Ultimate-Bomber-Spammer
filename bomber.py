from about import *
from instagram_bomber import *
from sms_bomber import *
from callprocess import *
from checkconnection import *
from whatsapp_bomber import wbbomber
from email_bomber import *
from simple_chalk import chalk
import time
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
# ... your code ...
driver.quit()


if platform.system() == 'Linux':
    linux = True
    pass
elif platform.system() == 'Windows':
    linux = False
    pass
else:
    print('OS not supported !')
    exit()

s1 = ''

Bomber = """
            ▄████████  ▄█        ▄█             ▄█  ███▄▄▄▄         ▄██████▄  ███▄▄▄▄      ▄████████ 
           ███    ███ ███       ███            ███  ███▀▀▀██▄      ███    ███ ███▀▀▀██▄   ███    ███ 
           ███    ███ ███       ███            ███▌ ███   ███      ███    ███ ███   ███   ███    █▀  
           ███    ███ ███       ███            ███▌ ███   ███      ███    ███ ███   ███  ▄███▄▄▄     
         ▀███████████ ███       ███            ███▌ ███   ███      ███    ███ ███   ███ ▀▀███▀▀▀     
           ███    ███ ███       ███            ███  ███   ███      ███    ███ ███   ███   ███    █▄  
           ███    ███ ███▌    ▄ ███▌    ▄      ███  ███   ███      ███    ███ ███   ███   ███    ███ 
           ███    █▀  █████▄▄██ █████▄▄██      █▀    ▀█   █▀        ▀██████▀   ▀█   █▀    ██████████ 
                      ▀         ▀                                                                    
                ▀█████████▄   ▄██████▄    ▄▄▄▄███▄▄▄▄   ▀█████████▄     ▄████████    ▄████████    
                  ███    ███ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███   ███    ███    
                  ███    ███ ███    ███ ███   ███   ███   ███    ███   ███    █▀    ███    ███    
                 ▄███▄▄▄██▀  ███    ███ ███   ███   ███  ▄███▄▄▄██▀   ▄███▄▄▄      ▄███▄▄▄▄██▀    
                ▀▀███▀▀▀██▄  ███    ███ ███   ███   ███ ▀▀███▀▀▀██▄  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀       
                  ███    ██▄ ███    ███ ███   ███   ███   ███    ██▄   ███    █▄  ▀███████████    
                  ███    ███ ███    ███ ███   ███   ███   ███    ███   ███    ███   ███    ███    
                ▄█████████▀   ▀██████▀   ▀█   ███   █▀  ▄█████████▀    ██████████   ███    ███    
                                                                                    ███    ███    
"""

Creds = """
                                ************************************************  
                                *   All In One Bomber - By NocturnalCompiler   * 
                                *            Version 2.0.0 (Stable)            *       
                                *         Discord : fyodor_dostoyevsky.        *
                                *          Old Maintainer : b31ngd3v           *
                                ************************************************                                     

"""

Options = """
    |-TYPE---------------------|
    | [1] - Email Bomber       |
    | [2] - SMS Bomber         |
    | [3] - WhatsApp Bomber    |
    | [4] - Instagram Bomber   |
    | [5] - Exit               |
    |--------------------------|"""

print(chalk.yellow.bold(Bomber))
print(chalk.cyanBright(Creds))
print(chalk.red.bold("                              Please use this tool for educational purpose only.                            "))
print(chalk.red.bold("                      Github : https://github.com/Nocturnal-Compiler/Ultimate-Bomber-Spammer                  "))
print('\n')
print(chalk.green.bold(Options))
opt = int(input(chalk.blue.bold("    |-> Enter the option number : ")))

if opt == 1:
    ebombingwin()

elif opt == 2:
    if linux:
        smsbombinglinux()
    else:
        smsbombingwin()

elif opt == 3:
    wbbomber()

elif opt == 4:
    if linux:
        igbombinglinux()
    else:
        igbombingwin()
