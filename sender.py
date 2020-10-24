from flask import Flask
from flask_mail import Mail, Message

# адреса почты, кому будет приходить уведомление
RECIPIENTS = [
    'td@21smart.ru',
    'tsvet005@yandex.ru']

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

text = 'Это просто текст пистьма.'

if __name__ == '__main__':
    send_mail(title='Everyday letter', body=text)
    app.run(debug=False)