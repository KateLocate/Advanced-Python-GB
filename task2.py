# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

strings = ['class', 'function', 'method']

for s, string in enumerate(strings):
    binary_string_as_utf8 = bytes(string, encoding='utf-8')
    try:
        binary_string_as_ascii = bytes(string, encoding='ascii')
    except UnicodeEncodeError:
        binary_string_as_ascii = 'cannot be converted as ascii string'

    if binary_string_as_utf8 == binary_string_as_ascii:
        print('\n',string, '\n\nutf-8 byte string: ', '\ntype - ', type(binary_string_as_utf8), '\nlength - ',
              len(binary_string_as_utf8))
        print('ascii byte string: ', '\ntype - ', type(binary_string_as_ascii), '\nlength - ',
              len(binary_string_as_ascii), '\n', 'String converted from utf-8: ', binary_string_as_utf8,
              'is equivalent to string converted from ascii: ', binary_string_as_ascii)

    else:
        print('\n',string, '\n\nutf-8 byte string: ', '\ntype - ', type(binary_string_as_utf8), '\nlength - ',
              len(binary_string_as_utf8), '\n', 'String converted from utf-8: ', binary_string_as_utf8,
              binary_string_as_ascii)
