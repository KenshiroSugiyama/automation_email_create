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
        #ここに保存するボタンクリック必要
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
    pyautogui.hotkey('right')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','shift','alt',':')
    time.sleep(0.5)
    webbrowser.open("https://muumuu-domain.com/?mode=conpane&state=mail_edit_address")
    time.sleep(3)
    for i in range(14):
        pyautogui.hotkey('down')
        time.sleep(0.2)   
    pyautogui.click(x=1034, y=972) #メールアドレス作成ボタンクリック
    time.sleep(0.5)
    pyautogui.click(x=130, y=16) #表②位置クリック
    time.sleep(2)
    pyautogui.hotkey('right')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','c') #文字列コピー
    time.sleep(0.6)
    pyautogui.click(x=345, y=16) #ムームドメインクリック
    time.sleep(2)
    pyautogui.hotkey('ctrl','a') 
    time.sleep(0.6)
    pyautogui.hotkey('backspace') 
    time.sleep(0.6)
    pyautogui.hotkey('ctrl','v') #文字列貼り付け
    time.sleep(0.6)
    pyautogui.hotkey('tab') 
    time.sleep(0.6)
    pyautogui.click(x=130, y=16) #表②位置クリック
    time.sleep(2)
    pyautogui.hotkey('right')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','c') #ドメイン番号コピー
    time.sleep(0.6)
    domain_number = pyperclip.paste()
    
    #ドメイン選択
    if domain_number == "20":
        time.sleep(0.3)   
    elif domain_number == "13":
        for i in range(2):
            pyautogui.hotkey('down')
            time.sleep(0.3)   
    elif domain_number == "10":
        for i in range(3):
            pyautogui.hotkey('down')
            time.sleep(0.3)   
    elif domain_number == "19":
        for i in range(5):
            pyautogui.hotkey('down')
            time.sleep(0.3)   
    elif domain_number == "4":
        for i in range(6):
            pyautogui.hotkey('down')
            time.sleep(0.3)   
    elif domain_number == "15":
        for i in range(7):
            pyautogui.hotkey('down')
            time.sleep(0.3)   
    elif domain_number == "7":
        for i in range(8):
            pyautogui.hotkey('down')
            time.sleep(0.3)   
    elif domain_number == "16":
        for i in range(9):
            pyautogui.hotkey('down')
            time.sleep(0.3)   
    elif domain_number == "14":
        for i in range(12):
            pyautogui.hotkey('down')
            time.sleep(0.3)   
    elif domain_number == "12":
        for i in range(13):
            pyautogui.hotkey('down')
            time.sleep(0.3)   
    elif domain_number == "18":
        for i in range(14):
            pyautogui.hotkey('down')
            time.sleep(0.3)   
    elif domain_number == "11":
        for i in range(15):
            pyautogui.hotkey('down')
            time.sleep(0.3)   
    elif domain_number == "5":
        for i in range(16):
            pyautogui.hotkey('down')
            time.sleep(0.3)   
    elif domain_number == "17":
        for i in range(17):
            pyautogui.hotkey('down')
            time.sleep(0.3)   
    elif domain_number == "6":
        for i in range(18):
            pyautogui.hotkey('down')
            time.sleep(0.3)   
    elif domain_number == "3":
        for i in range(19):
            pyautogui.hotkey('down')   
            time.sleep(0.3)   

    time.sleep(0.6)
    pyautogui.hotkey('enter') 
    time.sleep(0.6)
    pyautogui.hotkey('enter') 
    time.sleep(0.6)
    pyautogui.hotkey('tab') 
    time.sleep(0.5)
    pyautogui.click(x=130, y=16) #表②位置クリック
    time.sleep(2)
    pyautogui.hotkey('right')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','c') #passwordコピー
    time.sleep(0.6)
    pyautogui.click(x=345, y=16) #ムームドメインクリック
    time.sleep(2)
    pyautogui.hotkey('ctrl','v') #password貼り付け
    time.sleep(0.6)
    pyautogui.hotkey('tab')
    time.sleep(0.6)
    pyautogui.hotkey('ctrl','v') #password貼り付け
    time.sleep(0.6)




