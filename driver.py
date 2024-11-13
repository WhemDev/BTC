from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Tarayıcı sürücüsünü başlatın (Chrome kullanıyorsanız chromedriver yolunu belirleyin)
driver = webdriver.Chrome()

# Web sayfasını açın
url = "https://www.binance.com/en/game/button/btc-2024?ref=BUTTONGAME"  # Saat ve katılımcı sayısının bulunduğu sayfa
driver.get(url)

# Elementlerin yüklenmesi için bir süre bekleyin
time.sleep(3)  # Gerekirse sayfanın tamamen yüklenmesi için artırılabilir

try:
    # Saat elementini bulun
    timer_element1 = driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[2]/div[1]/div[1]/p').text
    timer_element2 = driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[2]/div[1]/div[2]/p').text
    timer_element3 = driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[2]/div[3]/div[1]/p').text
    timer_element4 = driver.find_element(By.XPATH, '//*[@id="__APP"]/div/div[2]/div[2]/div[3]/div[2]/p').text
    secondsLeft = (timer_element1 * 1000) + (timer_element2 * 100) + (timer_element3 * 10) + (timer_element4)
    print("Süre:", secondsLeft)

    # Katılımcı sayısı elementini bulun
    participant_element = driver.find_element(By.XPATH, '//*[@id="participants"]')  # XPath'i sayfa yapısına göre güncelleyin
    participant_text = participant_element.text
    print("Katılımcı Sayısı:", participant_text)

except Exception as e:
    print("Veri çekilirken bir hata oluştu:", e)

# Tarayıcıyı kapatın
driver.quit()