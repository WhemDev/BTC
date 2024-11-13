from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 
driver = webdriver.Chrome()


token = "7920129716:AAHzPB_qD_-TQJhAonzk_1pz7qtsLEvXE_4"
url = f"https://api.telegram.org/bot{token}/getUpdates"

message = "Growth in the number of enrolled participant count is SLOWED; Please pay attention to take maual action."

# Web sayfasını açın
url = "https://www.binance.com/en/game/button/btc-2024?ref=BUTTONGAME"  # Saat ve katılımcı sayısının bulunduğu sayfa

# Elementlerin yüklenmesi için bir süre bekleyin
time.sleep(3)  # Gerekirse sayfanın tamamen yüklenmesi için artırılabilir
print("Binance BTC Button Detector")
print("Welcome to the Binance BTC Button Alerter Bot!")
print("To get Alerts and Notifications and Informations, please to following steps : ")
print("1.   Open Telegram")
print("2.   Start a chat with our bot @binanceBtcButtonBot")
print("3.   Once you started a new chat, please copy your chat ID and paste it here")
chatID = input("Please enter your chat ID : ")
print("Done, now a window of the Binance 1 BTC Buton game will opened and the further introductions will ne shown")
time.sleep(2)
driver.get(url)
print("\n")
print("PLEASE USE THE OPENED WINDOW AND LOGIN TO YOUR BINANCE ACCOUNT")
print("AFTER YOU LOGGED IN AND SAW THE GAME PAGE PLEASE PRESS ENTER TO START ")
print("\n")
ifready = (input("Type 'anything or simply press enter when you all set : ") == 'READY')
print(ifready)

passed = time.perf_counter()

try:
    # Saat elementini bulun
    while True:
        timer_element1 = int(driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[2]/div[1]/div[1]/p').text)
        timer_element2 = int(driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[2]/div[1]/div[2]/p').text)
        timer_element3 = int(driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[2]/div[3]/div[1]/p').text)
        timer_element4 = int(driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[2]/div[3]/div[2]/p').text)

        print("Value: ")
        print(timer_element1)
        print(timer_element2)
        print(timer_element3)
        print(timer_element4)

        secondsLeft = (timer_element1 * 1000) + (timer_element2 * 100) + (timer_element3 * 10) + (timer_element4)
        print("Süre:", secondsLeft)
        # Katılımcı sayısı elementini bulun
        print(passed)
        time.sleep(10)
        if passed > 60:
            participant_element = driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[5]/div[2]/div[2]')  # XPath'i sayfa yapısına göre güncelleyin
            participant_text = participant_element.text
            print("Katılımcı Sayısı:", participant_text)
            passed = time.perf_counter()

        

except Exception as e:
    print("An error accuired please restart:", e)

# Tarayıcıyı kapatın
driver.quit()