from flask import Flask
from flask_mail import Mail, Message
import datetime

# адреса почты, кому будет приходить уведомление
RECIPIENTS = ['tsvet005@yandex.ru']

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.yandex.ru'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'informersmart@yandex.ru'
app.config['MAIL_DEFAULT_SENDER'] = 'informersmart@yandex.ru'
app.config['MAIL_PASSWORD'] = 'Smart620514'

def send_mail(title, body, html=''):
    with app.app_context():
        mail = Mail(app)
        msg = Message(title, recipients=RECIPIENTS)
        msg.body = body
        print('Отправка писем')
        mail.send(msg)
    print(f'Письма отправлены: {RECIPIENTS}')
    return

current_date = datetime.datetime.now()
print('Текущий день недели: ',current_date.isoweekday())
if current_date.isoweekday() == 4 :
    text = 'Это просто текст письма. Отправлено: {} в {}'.format(
        current_date.date(), current_date.time())
    send_mail(title='Test letter', body=text)

print('Завершение работы')
