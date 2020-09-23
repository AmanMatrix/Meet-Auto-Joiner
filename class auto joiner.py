#Read readme file before executing(recommended)
import subprocess
import pyautogui
import time
from datetime import datetime
screenWidth,screenHeight = pyautogui.size()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
path=r'C:\Program Files\Google\Chrome\Application\\chrome.exe' #Enter path of your web browser here ending with \\chrome.exe
link='https://meet.google.com/gbh-nmjn-jzb' #Link for the class(make sure you are signed in)
classStart=input(f"Enter class start time in 24h format as hh:mm:ss (current time is {current_time})\n")
classEnd=input(f"Enter class end time in 24h format as hh:mm:ss (current time is {current_time})\n")
while(1):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time==classStart:
        proCess=subprocess.Popen(path)
        time.sleep(2)
        pyautogui.click(310*screenWidth/1366,51*screenHeight/768)
        pyautogui.write(f"{link}")
        pyautogui.press('enter')
        time.sleep(10)
        pyautogui.hotkey('ctrl','d') #Turns off Mic
        #pyautogui.click(408*screenWidth/1366,604*screenHeight/768)
        time.sleep(1)
        pyautogui.hotkey('ctrl','e') #Turns off Camera
        #pyautogui.click(486*screenWidth/1366,608*screenHeight/768)
        time.sleep(1)
        pyautogui.click(988*screenWidth/1366,440*screenHeight/768) #Join now
    elif current_time==classEnd:
        pyautogui.click(679*screenWidth/1366,715*screenHeight/768) #End Call
        break
    else:pass






