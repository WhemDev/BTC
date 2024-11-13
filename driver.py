from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import json

driver = webdriver.Chrome()

# 5818952657

token = "7920129716:AAHzPB_qD_-TQJhAonzk_1pz7qtsLEvXE_4"
url = f"https://api.telegram.org/bot{token}/sendMessage"
url2 = f"https://api.telegram.org/bot{token}/getUpdates"

messageP = "Growth in the number of enrolled participant count is SLOWED; Please pay attention to take manual action."
messageA = "TIMER ALERT\nThe counter has decreased significantly. Please check and prepare to take action.\nTIME LEFT: \n"
messageE = "An Error occurred. Please take action."
messageC = "AUTOMATICALLY CLICKED\nPLEASE TAKE IMMEDIATE ACTION"

url = "https://www.binance.com/en/game/button/btc-2024?ref=BUTTONGAME" 

time.sleep(2) 
print("Binance BTC Button Detector")
print("Welcome to the Binance BTC Button Alerter Bot!")
print("To get Alerts and Notifications and Informations, please to following steps : ")
print("1.   Open Telegram")
print("2.   Start a new chat with the our telegram bot @binanceBtcButtonBot")
print("3    Then use /start command to start a conversation. Then follow the introductions.")
print("4.   Once you started a new chat, please enter YOUR telegram username. So our bot can send you private messages.")

while not chat_id:
    username = input("Please enter your Telegram username: ")
    
    response = requests.get(url2)
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

print("\n")
print("Done, now a window of the Binance 1 BTC Buton game will opened and the further introductions will ne shown")
time.sleep(1)
driver.get(url)
print("\n")
print("PLEASE USE THE OPENED WINDOW AND LOGIN TO YOUR BINANCE ACCOUNT")
print("AFTER YOU LOGGED IN AND SAW THE GAME PAGE PLEASE PRESS ENTER TO START ")
print("\n")
ifready = (input("Type 'anything or simply press enter when you all set : ") == 'READY')


start = time.perf_counter()


def sendAlert(type, num):
    global chat_id
    if type == "p": message = messageP
    elif type == "a": message = messageA + str(num)
    elif type == "e": message = messageE
    params = {
    "chat_id": chat_id,
    "text": message
}
    response = requests.get(url, params=params)



try:
    participant_element = driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[5]/div[2]/div[2]')
    participant_text = participant_element.text
    lastP = participant_text
    button = driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[3]/div/div/img')
    
    while True:
        waitTime = 30
        timer_element1 = int(driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[2]/div[1]/div[1]/p').text)
        timer_element2 = int(driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[2]/div[1]/div[2]/p').text)
        timer_element3 = int(driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[2]/div[3]/div[1]/p').text)
        timer_element4 = int(driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[2]/div[3]/div[2]/p').text)

        secondsLeft = (timer_element1 * 1000) + (timer_element2 * 100) + (timer_element3 * 10) + (timer_element4)

        if secondsLeft < 40:
            button.click()
            sendAlert("c", secondsLeft)

        if 6000 > secondsLeft >= 4500:
            waitTime = 30
        elif secondsLeft < 4500:
            waitTime = 20
            sendAlert(4500)
        elif secondsLeft < 3000:
            waitTime = 5
            sendAlert(3000)
        elif secondsLeft < 5000:
            waitTime = 0
            sendAlert(5000)

        time.sleep(waitTime)


        now = time.perf_counter()
        passed = start - now
        start = now
        if passed > 60:
            participant_element = driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[5]/div[2]/div[2]')
            participant_text = participant_element.text
            newP = participant_text
            if lastP - newP < 5:
                sendAlert("p", participant_text)
            lastP = newP
            now = time.perf_counter()


except Exception as e:
    print("An error accuired please restart:", e)
    sendAlert("e", e)

driver.quit()