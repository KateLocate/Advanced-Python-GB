# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

strings = ['attribute', 'класс', 'функция', 'type']

for s, string in enumerate(strings):
    try:
        binary_string = bytes(string, encoding='ascii')
        print('"', string, '"', 'in ascii: ', binary_string)
    except UnicodeEncodeError:
        print('"', string, '"', 'cannot be encoded as ascii string')
