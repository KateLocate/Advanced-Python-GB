# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на
#  кириллице.

import subprocess


google_args = ['ping', 'google.com']
subproc_google_ping = subprocess.Popen(google_args, stdout=subprocess.PIPE)

yandex_args = ['ping', 'yandex.ru']
subproc_yandex_ping = subprocess.Popen(yandex_args, stdout=subprocess.PIPE)

pings = [subproc_google_ping, subproc_yandex_ping]

for p, ping in enumerate(pings):
    for line in ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))
