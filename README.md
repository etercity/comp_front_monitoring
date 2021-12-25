# comp_front_monitoring
Comparium test E2E monitoring 2.0
Selenium | web-driver | Pytest | POM

1. Установить версию Python выше 3.0
2. Добавить путь к Python в глобальную переменную Path
3. Скачать драйвера соответствующие установленным браузерам (chrome & firefox)
4. Положить скаченные драйвера каждый в отдельную папку корневой директории диска С (папки назвать по названию драйверов - chromedriver и geckodriver соответственно)
5. Добавить пути к драйверам в глобальную переменную PATH
6. Клонировать проэкт с гитхаба: 
        git clone https://etercity@github.com/etercity/comp_monitor_2_0.git
7. Если нужно, установить пакеты из requirements.txt (лучше всего создать новое виртуальное окружение и активировать. После чего выполнить команду:
		pip install -r requirements.txt), все пакеты будут автоматом установлены.
8. Из командной строки перейти в директорию склонированного проэкта и установить модуль: 
        pip install requests
9. Из командной строки перейти в директорию склонированного проэкта, в папку tests

10. Параметры запуска тестов из командной строки:
--browser_name (по дефолту chrome):
	"chrome" либо "firefox"
--browser_mode (по дефолту gui:
	"gui" либо "headless"
--login (обязательно!): email зареганый во front.comparium.app с максимальным планом на 10 парал. сессий. (будет меньше, тесты упадут!)
--password (обязательно!): password
--telechat: передаем telechat_id телебота, если хотим получить репорт в телеграмм
--teletoken: передаем teletoken, если хотим получить репорт в телеграмм
--browser (по дефолту selected total): передаем браузер из капабилити скриншотилки
--os: (по дефолту selected total): передаем OS из капабилити скриншотилки
--width (по дефолту 1024): передаем width из капабилити скриншотилки
--vnc_os: передаем vnc_os из капабилити ливтестинга (либо Linux либо Windows), по дефолту тесты пройдут по обоим платформам.
--test_url_baa: передаем тестовый урл с БА
--login_baa: передаем логин для БА
--password_baa: передаем пароль для БА

Примеры запуска тестов:
    pytest -q -s --telechat="******" --teletoken="******" --login="example@gmail.com" --password="*******" test_front_screenshot.py
    pytest -q -s --telechat="******" --teletoken="******" --login="example@gmail.com" --password="*******" test_front_screenshot_login_profile.py
    pytest -q -s --telechat="******" --teletoken="******" --login="example@gmail.com" --password="*******" --test_url_baa="https://*****" --login_baa="*****" --password_baa="*****" test_front_screenshot_ba.py
    pytest -q -s --telechat="******" --teletoken="******" --browser_name="firefox" --browser_mode="headless" --login="example@gmail.com" --password="*******" test_front_live_testing.py
total:
    pytest -q -s --telechat="******" --teletoken="******" --browser_name="firefox" --browser_mode="headless" --login="example@gmail.com" --password="*******"
    


