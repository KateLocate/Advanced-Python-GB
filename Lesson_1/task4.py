# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
#  байтовое и выполнить обратное преобразование (используя методы encode и decode).

strings = ['разработка', 'администрирование', 'protocol', 'standard']

for s, string in enumerate(strings):
    binary_string = string.encode()
    decoded_string = binary_string.decode()
    print(binary_string, '==', decoded_string)
