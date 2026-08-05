import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("Тест")
msg['Subject'] = 'Тест'
msg['From'] = 'твой_логин@mail.ru'
msg['To'] = 'твой_логин@mail.ru'

try:
    server = smtplib.SMTP('smtp.mail.ru', 465)
    server.login('твой_логин@mail.ru', 'пароль_приложения')
    server.send_message(msg)
    server.quit()
    print("✅ Успешно!")
except Exception as e:
    print("❌ Ошибка:", e)