# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его
# содержимое.

with open('test_file.txt', 'w+') as file:
    file.write('сетевое программирование, сокет, декоратор')
    # file.write('dtfhcfykuilydfui')
    # - test the exception
    print('File name:', file.name, '\nFile encoding: ', file.encoding)

try:
    with open('test_file.txt', encoding='utf-8') as file:
        print('File decoded with UTF-8:', file.readlines())

except UnicodeDecodeError:
    print('UTF-8 cannot decode this file.')
