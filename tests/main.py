import cv2
import numpy as np
import mss
from datetime import datetime
import os
import time
from tests.config import * 

# Şablon görüntüleri yükleme
templates = {str(i): cv2.imread(f'templates/templates/{i}.png', 0) for i in range(10)}
templates[":"] = cv2.imread('templates/templates/colon.png', 0)

# Ekran görüntülerinin kaydedileceği klasör
output_dir = "screenshots"
os.makedirs(output_dir, exist_ok=True)  # Klasörü oluşturur (varsa atlar)

# İkinci monitörü seçelim (Monitor 2 örneği)

# mss kullanarak ekran görüntüsü alma
with mss.mss() as sct:
    # Seçilen monitörün tam koordinatlarını al
    monitor = sct.monitors[monitor_number]
    
    # Seçilen monitörde belirtilen alanı güncelle
    monitor_region["top"] += monitor["top"]
    monitor_region["left"] += monitor["left"]

    while True:
        # Ekranın belirtilen bölgesinin fotoğrafını çek
        screenshot = np.array(sct.grab(monitor_region))
        gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        detected_digits = []

        # Her bir şablonla eşleştirme
        for digit, template in templates.items():
            # Şablon eşleştirme
            res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8  # Eşleşme eşiği
            loc = np.where(res >= threshold)

            # Eşleşen konumları listeye ekle
            for pt in zip(*loc[::-1]):
                detected_digits.append((pt[0], digit))  # X konumuna göre kaydediyoruz

        # Tespit edilen rakamları X koordinatına göre sırala
        detected_digits.sort()

        # Tespit edilen saat formatını oluştur
        time_str = "".join([d[1] for d in detected_digits])
        print(detected_digits)
        
        # Eğer tespit edilen formatta ":" işareti yoksa, düzgün saat tespiti yapılmamış olabilir.
        if ":" in time_str:
            print("Süre:", time_str)
        else:
            print("Geçersiz tespit:", time_str)

        # Belirli bir süre bekleyerek döngüyü düzenle (örneğin her 5 saniyede bir kontrol)
        time.sleep(5)