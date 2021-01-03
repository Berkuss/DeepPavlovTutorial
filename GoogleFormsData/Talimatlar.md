### Google Sheet API ve gspread API 

Google sheet api sayesinde google tablolardaki verilere erişim sağlayabiliyoruz. Gspred ise bir Python kütüphanesi bize Google Sheet API yi 
kolaylıkla kodumuzda kullanmamızı sağlıyor.

İlk olarak şuradaki adımları yapmamız gerekiyor : https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html 
Burada ise Gspread kütüphanesinin dokumanı :  https://gspread.readthedocs.io/en/latest/index.html

## Adım 1 : 

Google console dan yeni proje açılır ve Google Sheet API  aktive edilir.

## Adım 2 :

Google projesindeki bir account service oluşturulur ve google bize ilgili client_config dosyasını verir. Bu dosyayı daha sonra projemizde kullancaz.

## Adım 3 :

Ardından tablonun sahibine, size verilen email'i paylaşarak sizi ilgili ilgili tablo için erişim izni isteyin.
