# Telegram Bot for Monitoring VPS Fornex

<h4>Телеграмм бот для мониторинга сервера CSGO, созданного через LGSM.</h4>
<hr>
Требуется версия python 3.7 и ниже!
Бот сделан на <b>aiogram</b>, что позволяет асинхронно использовать функции бота.
Используется библиотека <b>paramiko</b> для подключения к отдельному серверу через SSH.
Для взаимодействия с сервером CSGO используется библиотека <b>valve</b>.

Для использования достаточно изменить файл <b><i>.env.example</i></b> на <b><i>.env</i></b>, затем добавить в него необходимые ключи.

Бот запускается командой<code>python bot.py</code>
<hr>

Помимо этого присутствует Dockerfile для контейнирезации:
<p style='text-align: center;'><code>docker build -t ваш тег .</code></p>
<p style="text-align: center;"><code>docker run -d ваш тег</code></p>