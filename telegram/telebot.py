"""
bot was blocked by the user — пользователь удалил чат с ботом на стороне телеграм, таким образом отписавшись от получения сообщений.
user is deactivated — пользователь удалил свой номер телефона на стороне телеграм или его номер телефона находится в процессе деактивации.
phone number invalid — пользователь неверно указал свой номер телефона на стороне телеграм.
bad request chat not found — пользователь не написал ничего в ваш телеграм бот. Пользователю нужно написать сообщение в бот, прежде чем бот сможет написать сообщение пользователю.
[400]Bad Request: wrong HTTP URL — возникает при неверном указании ссылки в рассылке telegram. Чаще всего это связано с опечаткой в ссылке.
[400]Bad Request: can’t parse entities: Unexpected end tag at byte offset — может возникать в случае, если в теле письма были не закрыты какие-либо HTML-теги.
[400]Bad Request: MEDIA_CAPTION_TOO_LONG — Эта ошибка связана с ограничением в количестве символов в подписи к медиафайлам (1024 символа, включая пробелы).
[400]Bad Request: message is too long — говорит о том, что количество используемых символов в тексте письма превысило 4096 символов. Данное значение установлено самим Телеграмом.
[400]Bad Request: wrong file identifier/HTTP URL specified — ссылается на неверный идентификатор файла. Обратите внимание, что при использовании «image url» изображение должно быть в формате «.jpeg».
[400]Bad Request: failed to get HTTP URL content или Bad Request: wrong file identifier/HTTP URL specified — могут возникать в случае, ели превышен максимальный размер вложения (5 мб для картинок и 20 мб для других типов файлов).
[400]Bad Request: unsupported URL protocol — возникает из-за неправильного указания ссылки в синтаксисе кнопки. Например, при наличии лишнего пробела.
"""
import requests
from ..settings import main_settings


class Telebot():

    def __init__(self, telechat, teletoken):
            self.token = teletoken
            self.chat_id = telechat

    def send_report_to_telegram(self, screenshot, report):
        len_report = len(report)
        if len_report <= main_settings.COUNT_SYMBOLS: Telebot.send_screen_and_title(self, report, screenshot)
        else:
            Telebot.sendImage(self, screenshot)
            Telebot.sendMessage(self, report)

    def send_screen_and_title(self, report, screenshot):
        print('Sending report to Telegram...')
        url = (f"https://api.telegram.org/bot{self.token}/sendPhoto")
        files = {'photo': open(f"{screenshot}", 'rb')}
        title = report
        data = {'chat_id': f"{self.chat_id}", 'caption': title}
        r = requests.post(url, files=files, data=data)
        print(r.status_code, r.reason, r.content)

    def sendImage(self, screenshot):
        url = (f"https://api.telegram.org/bot{self.token}/sendPhoto")
        files = {'photo': open(f"{screenshot}", 'rb')}
        data = {'chat_id': f"{self.chat_id}"}
        r = requests.post(url, files=files, data=data)
        print(r.status_code, r.reason, r.content)

    def sendFile(self, report):
        pass

    def sendMessage(self, report):
        requests.get((f"https://api.telegram.org/bot{self.token}/sendMessage"), params=dict(
            chat_id=self.chat_id,
            text=report
        ))


