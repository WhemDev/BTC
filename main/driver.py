from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import requests
#


class BinanceBot():
    load_dotenv()

    def __init__(self):
        print("""
.------..------..------..------..------..------..------.     .------..------.     .------..------..------.     .------..------..------.       
|W.--. ||E.--. ||L.--. ||C.--. ||O.--. ||M.--. ||E.--. |.-.  |T.--. ||O.--. |.-.  |B.--. ||B.--. ||B.--. |.-.  |B.--. ||O.--. ||T.--. |.-.    
| :/\: || (\/) || :/\: || :/\: || :/\: || (\/) || (\/) ((5)) | :/\: || :/\: ((5)) | :(): || :(): || :(): ((5)) | :(): || :/\: || :/\: ((5))   
| :\/: || :\/: || (__) || :\/: || :\/: || :\/: || :\/: |'-.-.| (__) || :\/: |'-.-.| ()() || ()() || ()() |'-.-.| ()() || :\/: || (__) |'-.-.  
| '--'W|| '--'E|| '--'L|| '--'C|| '--'O|| '--'M|| '--'E| ((1)) '--'T|| '--'O| ((1)) '--'B|| '--'B|| '--'B| ((1)) '--'B|| '--'O|| '--'T| ((1)) 
`------'`------'`------'`------'`------'`------'`------'  '-'`------'`------'  '-'`------'`------'`------'  '-'`------'`------'`------'  '-'  
  """)
        self.username = input("Please enter your Telegram username: ")
        self.driver = webdriver.Chrome()
        self.token = os.getenv('TOKEN')
        self.url = f"https://api.telegram.org/bot{self.token}/getUpdates"
        self.url2 = f"https://api.telegram.org/bot{self.token}/getUpdates"


    def main(self):
        clear = lambda: os.system('cls')
        clear()
        print("Growth in the number of enrolled participant count is SLOWED; Please pay attention to take maual action.")
        print("To get Alerts and Notifications and Informations, please to following steps : \n1.   Open Telegram\n2.   Start a chat with our bot @binanceBtcButtonBot\n3.   Once you started a new chat, please copy your chat ID and paste it here")
        self.driver.get("https://www.binance.com/en/game/button/btc-2024?ref=BUTTONGAME") #Websiteyi aciyor
        WebDriverWait(self.driver,30).until(
            lambda driver : self.driver.execute_script("return document.readyState") == "complete" #sayfanin tamamen yuklenmesi js ile kontrol ediyor
        )
        clear()
        print("PLEASE USE THE OPENED WINDOW AND LOGIN TO YOUR BINANCE ACCOUNT\nAFTER YOU LOGGED IN AND SAW THE GAME PAGE PLEASE PRESS ENTER TO START")
        ifready = (input("Simply press enter when you all set : ") == 'READY')

        start = time.perf_counter()
        try:
            participant_element = self.driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[5]/div[2]/div[2]')
            participant_text = participant_element.text
            lastP = participant_text
            button = self.driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[3]/div/div/img')
            
            while True:
                waitTime = 30
                timer_element1 = int(self.driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[2]/div[1]/div[1]/p').text)
                timer_element2 = int(self.driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[2]/div[1]/div[2]/p').text)
                timer_element3 = int(self.driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[2]/div[3]/div[1]/p').text)
                timer_element4 = int(self.driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[2]/div[3]/div[2]/p').text)

                secondsLeft = (timer_element1 * 1000) + (timer_element2 * 100) + (timer_element3 * 10) + (timer_element4)

                if secondsLeft < 40:
                    button.click()
                    self.sendAlert("c", secondsLeft)

                if 6000 > secondsLeft >= 4500:
                    waitTime = 30
                elif secondsLeft < 4500:
                    waitTime = 20
                    self.sendAlert("c",4500)
                elif secondsLeft < 3000:
                    waitTime = 5
                    self.sendAlert("c",3000)
                elif secondsLeft < 5000:
                    waitTime = 0
                    self.sendAlert("c",5000)

                time.sleep(waitTime)


                now = time.perf_counter()
                passed = start - now
                
                if passed > 60:
                    participant_element = self.driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[5]/div[2]/div[2]')
                    participant_text = participant_element.text
                    newP = participant_text
                    if lastP - newP < 5:
                        self.sendAlert("p", participant_text)
                    lastP = newP
                    now = time.perf_counter()
        except Exception as e:
            print("An error accuired please restart:", e)
            self.sendAlert("e", e)

    def sendAlert(self,type, num):
        messageP = "Growth in the number of enrolled participant count is SLOWED; Please pay attention to take manual action."
        messageA = "TIMER ALERT\nThe counter has decreased significantly. Please check and prepare to take action.\nTIME LEFT: \n"
        messageE = "An Error occurred. Please take action."
        messageC = "AUTOMATICALLY CLICKED\nPLEASE TAKE IMMEDIATE ACTION"
        chat_id = None
        while not chat_id:
            username = input("Please enter your Telegram username: ")
            
            response = requests.get(self.url2)
            data = response.json()
            
            for result in data["result"]:
                if result["message"]["chat"].get("username") == username:
                    chat_id = result["message"]["chat"]["id"]
                    break

            if chat_id:
                print(f"Chat ID for username '{username}': {chat_id}")
            else:
                print(f"User with username '{username}' not found.")
                print("Please try again. Make sure you have started a conversation with the bot using /start.")
                time.sleep(1)
        message = "Ready"
        url = f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url).json()
        if type == "p": message = messageP
        elif type == "a": message = messageA + str(num)
        elif type == "e": message = messageE
        elif type == "c": message = messageC
        params = {
        "chat_id": chat_id,
        "text": message
    }
        response = requests.get(url, params=params)

if __name__ == "__main__":
    btcStart = BinanceBot()
    btcStart.main()
