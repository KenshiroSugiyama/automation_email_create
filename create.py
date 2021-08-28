# coding: UTF-8

# PyAutoGUIをインポート
import pyautogui 
import time
import webbrowser
import pyperclip

#表②開く
webbrowser.open("https://docs.google.com/spreadsheets/d/1GPpVKAA1okFjpifE494Ax4laHYQ5XaMvIZ6CQByPD_Y/edit#gid=0") 
time.sleep(10)
pyautogui.hotkey('right')
time.sleep(0.5)
pyautogui.hotkey('ctrl','down')
time.sleep(0.5)
pyautogui.hotkey('down')
time.sleep(0.5)
pyautogui.hotkey('right')
time.sleep(0.5)
pyautogui.hotkey('ctrl','c')
copy = pyperclip.paste()

if copy == "forward setting":
    print("転送設定スタート") 
    for i in range(6):
        pyautogui.hotkey('right')
        time.sleep(0.6)
    webbrowser.open("https://muumuu-mail.com/")
    time.sleep(0.6)
    pyautogui.click(x=130, y=16) #表②位置クリック
    time.sleep(2)
    pyautogui.hotkey('ctrl','c') #メアドコピー
    time.sleep(0.6)
    pyautogui.hotkey('right')
    time.sleep(0.6)
    pyautogui.click(x=345, y=16) #ムームーメール位置クリック
    time.sleep(2)
    pyautogui.hotkey('ctrl','v') #メアド貼り付け
    time.sleep(0.6)
    pyautogui.hotkey('tab')
    time.sleep(0.6)
    pyautogui.click(x=130, y=16) #表②位置クリック
    time.sleep(2)
    pyautogui.hotkey('ctrl','c') #パスワードコピー
    time.sleep(0.6)
    pyautogui.click(x=345, y=16) #ムームーメール位置
    time.sleep(2)
    pyautogui.hotkey('ctrl','v') #パスワード貼り付け
    time.sleep(0.6)
    pyautogui.hotkey('tab')
    time.sleep(0.6)
    pyautogui.hotkey('enter')
    time.sleep(10)
    mailtop = pyautogui.locateOnScreen('mail.png' , confidence=0.7)
    if mailtop is "none": #ムームーメールログイン成功
        time.sleep(0.6)
        pyautogui.click(x=1874, y=95) #右上box位置クリック
        time.sleep(1)
        pyautogui.hotkey('tab')
        time.sleep(0.6)
        pyautogui.hotkey('enter')
        time.sleep(3)
        pyautogui.click(x=45, y=324) #転送設定クリック
        time.sleep(1)
        pyautogui.click(x=277, y=406) #メアド入力boxクリック
        time.sleep(0.6)
        pyautogui.typewrite("y.mail.forward@mileshare.jp")
        time.sleep(0.6)
        pyautogui.hotkey('tab')
        time.sleep(0.6)
        pyautogui.hotkey('enter')
        time.sleep(3)
        pyautogui.click(x=1874, y=95) #右上box位置クリック
        time.sleep(1)
        pyautogui.hotkey('tab')
        time.sleep(0.6)
        pyautogui.hotkey('tab')
        time.sleep(0.6)
        pyautogui.hotkey('enter') #ログアウト
        time.sleep(10)
        pyautogui.click(x=130, y=16) #表②位置クリック
        time.sleep(2)
        pyautogui.hotkey('ctrl','left')
        time.sleep(0.6)
        pyautogui.hotkey('ctrl','shift','alt',':')
        time.sleep(0.6)
        pyautogui.hotkey('left')
        time.sleep(0.6)
        pyperclip.copy("転送済み")
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.6)
        pyautogui.hotkey('enter') 
        time.sleep(0.6)
        pyautogui.click(x=1899, y=13) #右上×クリック
        time.sleep(0.6)
    else:
        time.sleep(2)
        pyautogui.hotkey('left')
        time.sleep(0.6)
        pyautogui.hotkey('left')
        time.sleep(0.6)
        pyautogui.hotkey('backspace') 
        time.sleep(0.6)
        pyautogui.click(x=1899, y=13) #右上×クリック
        time.sleep(0.6)
else:
    print("メアド作成スタート")
    


        








