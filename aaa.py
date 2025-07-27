import smtplib

try:
    server = smtplib.SMTP_SSL("smtp.yandex.ru", 465, timeout=10)
    server.login("takao.nakamuro@yandex.ru", "qdeqwoninzkzdzim")
    print("✅ Подключение успешно")
    server.quit()
except Exception as e:
    print("❌ Ошибка:", e)