# coding: UTF-8

# PyAutoGUIをインポート
import pyautogui 
import time
import webbrowser
import pyperclip
import requests
import json
import os
from dotenv import load_dotenv

# .envファイルの内容を読み込み
load_dotenv()

# os.environを用いて環境変数を表示させます
# print (os.environ['EMAIL'])

def main():

    #表②開く
    webbrowser.open("https://docs.google.com/spreadsheets/d/1GPpVKAA1okFjpifE494Ax4laHYQ5XaMvIZ6CQByPD_Y/edit#gid=0") 
    time.sleep(15)
    pyautogui.hotkey('ctrl','down')
    time.sleep(2)
    pyautogui.hotkey('right')
    time.sleep(2)
    pyautogui.hotkey('ctrl','up')
    time.sleep(2)
    pyautogui.hotkey('down')
    time.sleep(2)
    pyautogui.hotkey('right')
    time.sleep(2)
    pyautogui.hotkey('ctrl','c')
    time.sleep(2)
    copy = pyperclip.paste()
    print(copy)
    time.sleep(2)

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
        print(mailtop)
        if mailtop is None: #ムームーメールログイン成功
            time.sleep(0.6)
            pyautogui.click(x=1874, y=95) #右上box位置クリック
            time.sleep(1)
            pyautogui.hotkey('tab')
            time.sleep(0.6)
            pyautogui.hotkey('enter')
            time.sleep(3)
            pyautogui.click(x=45, y=324) #転送設定クリック
            time.sleep(1)
            pyautogui.click(x=283, y=338) #メアド入力boxクリック
            time.sleep(0.6)
            pyperclip.copy("y.mail.forward@mileshare.jp")
            time.sleep(0.6)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.6)
            pyautogui.hotkey('tab')
            time.sleep(0.6)
            pyautogui.hotkey('enter')
            time.sleep(3)
            pyautogui.click(x=297, y=594) #保存するクリック
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
            pyautogui.hotkey('enter') 
            time.sleep(0.6)
            pyautogui.click(x=1899, y=13) #右上×クリック
            time.sleep(0.6)
        else:
            pyautogui.click(x=130, y=16) #表②位置クリック
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
        time.sleep(1)
        pyautogui.hotkey('right')
        time.sleep(1)
        pyautogui.hotkey('ctrl','shift','alt',':')
        time.sleep(0.5)
        pyautogui.hotkey('right')
        time.sleep(1)
        pyautogui.hotkey('right')
        time.sleep(1)
        pyautogui.hotkey('ctrl','c')
        time.sleep(2)
        domain_number = pyperclip.paste()
        # print(copy)
        webbrowser.open("https://muumuu-domain.com/?mode=conpane&state=mail_edit_address")
        time.sleep(3)
        for i in range(3):
            pyautogui.hotkey('tab')
            time.sleep(0.2) 
        pyautogui.hotkey('backspace') 

        if 3<= int(domain_number) <=20 : #ドメイン番号でアカウント切り替え（3～20）真之アカ
            time.sleep(0.6)
            pyperclip.copy("saneyuki.akiyama2018@gmail.com")
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.6)
            pyautogui.hotkey('tab')
            time.sleep(0.6)
            pyautogui.hotkey('backspace') 
            time.sleep(0.6)
            pyperclip.copy(os.environ['pass1'])
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.6)
            pyautogui.hotkey('tab')
            time.sleep(0.6)
            pyautogui.hotkey('enter') 
            time.sleep(6)
            for i in range(14):
                pyautogui.hotkey('down')
                time.sleep(0.2)   
            pyautogui.click(x=1034, y=972) #メールアドレス作成ボタンクリック
            time.sleep(0.5)
        elif 21<= int(domain_number) <=25:
            time.sleep(0.6)
            pyperclip.copy("ty_para@hotmail.com")
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.6)
            pyautogui.hotkey('tab')
            time.sleep(0.6)
            pyautogui.hotkey('backspace') 
            time.sleep(0.6)
            pyperclip.copy(os.environ['pass2'])
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.6)
            pyautogui.hotkey('tab')
            time.sleep(0.6)
            pyautogui.hotkey('enter') 
            time.sleep(6)
            for i in range(14):
                pyautogui.hotkey('down')
                time.sleep(0.2)   
            pyautogui.click(x=1034, y=972) #メールアドレス作成ボタンクリック
            time.sleep(0.5)
        elif 26<= int(domain_number) <= 32:
            time.sleep(0.6)
            pyperclip.copy("kita.minami.ue@gmail.com")
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.6)
            pyautogui.hotkey('tab')
            time.sleep(0.6)
            pyautogui.hotkey('backspace') 
            time.sleep(0.6)
            pyperclip.copy(os.environ['pass3'])
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.6)
            pyautogui.hotkey('tab')
            time.sleep(0.6)
            pyautogui.hotkey('enter') 
            time.sleep(6)
            for i in range(20):
                pyautogui.hotkey('down')
                time.sleep(0.2)   
            create = pyautogui.locateOnScreen('create.png' , confidence=0.7)
            print(create)
            pyautogui.click(create) #メールアドレス作成ボタンクリック
            # pyautogui.click(x=1034, y=972) #メールアドレス作成ボタンクリック
            time.sleep(0.5)
        pyautogui.click(x=130, y=16) #表②位置クリック
        time.sleep(4)
        pyautogui.hotkey('left')
        time.sleep(1)
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
        # pyautogui.click(x=130, y=16) #表②位置クリック
        # time.sleep(2)
        # pyautogui.hotkey('right')
        # time.sleep(0.5)
        # pyautogui.hotkey('ctrl','c') #ドメイン番号コピー
        # time.sleep(0.6)
        # domain_number = pyperclip.paste()
        # pyautogui.click(x=345, y=16) #ムームドメインクリック
        # time.sleep(2)
        
        #ドメイン選択
        if domain_number == "20" or domain_number == "27":
            pyautogui.hotkey('down')
            time.sleep(0.3)   
        elif domain_number == "13" or domain_number == "29":
            for i in range(3):
                pyautogui.hotkey('down')
                time.sleep(0.3)   
        elif domain_number == "10" or domain_number == "21" or domain_number == "26":
            for i in range(4):
                pyautogui.hotkey('down')
                time.sleep(0.3)   
        elif domain_number == "19":
            for i in range(7):
                pyautogui.hotkey('down')
                time.sleep(0.3)   
        elif domain_number == "4":
            for i in range(9):
                pyautogui.hotkey('down')
                time.sleep(0.3)   
        elif domain_number == "15":
            for i in range(10):
                pyautogui.hotkey('down')
                time.sleep(0.3)   
        elif domain_number == "7":
            for i in range(11):
                pyautogui.hotkey('down')
                time.sleep(0.3)   
        elif domain_number == "16":
            for i in range(12):
                pyautogui.hotkey('down')
                time.sleep(0.3)   
        elif domain_number == "14":
            for i in range(16):
                pyautogui.hotkey('down')
                time.sleep(0.3)   
        elif domain_number == "12":
            for i in range(17):
                pyautogui.hotkey('down')
                time.sleep(0.3)   
        elif domain_number == "18":
            for i in range(18):
                pyautogui.hotkey('down')
                time.sleep(0.3)   
        elif domain_number == "11":
            for i in range(20):
                pyautogui.hotkey('down')
                time.sleep(0.3)   
        elif domain_number == "5":
            for i in range(21):
                pyautogui.hotkey('down')
                time.sleep(0.3)   
        elif domain_number == "17":
            for i in range(22):
                pyautogui.hotkey('down')
                time.sleep(0.3)   
        elif domain_number == "6":
            for i in range(23):
                pyautogui.hotkey('down')
                time.sleep(0.3)   
        elif domain_number == "3":
            for i in range(24):
                pyautogui.hotkey('down')   
                time.sleep(0.3)  
        elif domain_number == "22" or domain_number == "28":
            time.sleep(0.3)  
        elif domain_number == "23" or domain_number == "30":
            for i in range(2):
                pyautogui.hotkey('down')   
                time.sleep(0.3)  
        elif domain_number == "24" or domain_number =="32":
            for i in range(5):
                pyautogui.hotkey('down')   
                time.sleep(0.3)  
        elif domain_number == "25" or domain_number == "31":
            for i in range(6):
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

        for i in range(3):
            pyautogui.hotkey('tab')
            time.sleep(0.6)

        pyautogui.hotkey('ctrl','shift','i')
        time.sleep(5)
        pyautogui.hotkey('ctrl','f')
        time.sleep(0.6)
        pyperclip.copy("g-recaptcha-response")
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        g_recaptcha = pyautogui.locateOnScreen('g.png' , confidence=0.7)
        pyautogui.doubleClick(g_recaptcha)
        time.sleep(0.6)
        text = pyautogui.locateOnScreen('f.png' , confidence=0.7)
        pyautogui.doubleClick(text)
        time.sleep(0.6)
        pyautogui.hotkey('right')
        time.sleep(0.5)
        for i in range(14):
            pyautogui.hotkey('backspace')
            time.sleep(0.6)
        pyautogui.hotkey('enter') 
        time.sleep(3)
        pyautogui.click(x=882, y=631)   


        #recaptcha開始
        service_key = os.environ['API_KEY'] # 2captcha service key 
        google_site_key = os.environ['data-sitekey'] # reCAPTCHAのdata-sitekey
        pageurl = 'https://muumuu-domain.com/?mode=conpane&state=mail_edit_address' 
        url = "http://2captcha.com/in.php?key=" + service_key + "&method=userrecaptcha&googlekey=" + google_site_key + "&pageurl=" + pageurl 
        resp = requests.get(url) 
        print(resp)
        if resp.text[0:2] != 'OK': 
            quit('Service error. Error code:' + resp.text) 
        captcha_id = resp.text[3:]


        fetch_url = "http://2captcha.com/res.php?key="+ service_key + "&action=get&id=" + captcha_id
        
        for i in range(1, 10):
            time.sleep(20) # wait 10 sec.
            resp = requests.get(fetch_url)
            print(resp)
            if resp.text[0:2] == 'OK':
                break
        print('Google response token: ', resp.text[3:])
        pyperclip.copy(resp.text[3:])
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(3)
        pyautogui.hotkey('tab')
        time.sleep(0.6)
        pyautogui.hotkey('enter') 
        time.sleep(7)

        emailexist = pyautogui.locateOnScreen('existmail.png' , confidence=0.8)
        home = pyautogui.locateOnScreen('home.png' , confidence=0.7)
        if home is not None:
           #logout
            pyautogui.moveTo(1095, 173)
            time.sleep(2)
            logout_button = pyautogui.locateOnScreen('logout.jpg' , confidence=0.7)
            pyautogui.click(logout_button)
            time.sleep(3)
            pyautogui.click(x=130, y=16) #表②位置クリック
            time.sleep(2)
            pyautogui.hotkey('right')
            time.sleep(0.5)
            pyautogui.hotkey('ctrl','shift','alt',':')
            time.sleep(0.5)

        elif emailexist is not None:
            print("作成済みメアド")
            pyautogui.click(x=1170, y=383) #表示×クリック
            for i in range(21):
                pyautogui.hotkey('up')
                time.sleep(0.6)
            pyautogui.moveTo(1095, 173)
            time.sleep(2)
            logout_button = pyautogui.locateOnScreen('logout.jpg' , confidence=0.7)
            pyautogui.click(logout_button)
            time.sleep(3)
            pyautogui.click(x=130, y=16) #表②位置クリック
            time.sleep(2)
            pyautogui.hotkey('right')
            time.sleep(0.5)
            pyautogui.hotkey('ctrl','shift','alt',':')
            time.sleep(0.5)
        else:
            print("メアド作成失敗")
            pyautogui.click(x=1170, y=383) #×クリック
            for i in range(21):
                pyautogui.hotkey('up')
                time.sleep(0.6)
            pyautogui.moveTo(1095, 173)
            time.sleep(2)
            logout_button = pyautogui.locateOnScreen('logout.jpg' , confidence=0.7)
            pyautogui.click(logout_button)
            time.sleep(3)

        time.sleep(3)
        pyautogui.click(x=1899, y=13) #右上×クリック
        time.sleep(3)

if __name__ == "__main__":
    while True:
        main()



