# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
#  info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
# Для этого:
# a) Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
#  данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
#  «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
#  соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
#  os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и
#  поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
#  «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для
#  каждого файла);
# b) Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
#  данных  через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# c) Проверить работу программы через вызов функции write_to_csv().

import csv
import os
import re


INFO_PATH = os.getcwd() + '\info'
MAIN_DATA_PATH = os.getcwd() + '\main_data.txt'


def get_data(clues_path, path):
    os.chdir(path)
    files = os.listdir(path)

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    with open(clues_path) as file:
        strings = file.readlines()
        main_data = strings[0].split(sep=', ')

    for f in files:
        with open(f) as file:
            all_data = file.readlines()
            matches = []

            for code in main_data:
                pattern = f'^{code}:[0-9а-яёА-ЯЁa-zA-Z(\s)]+'

                for string in all_data:
                    matches_string = re.match(pattern, string)

                    if matches_string:
                        matches_string = matches_string.group().split(sep=':')
                        matches.append(matches_string)

            os_prod_list.append(matches[0][1])
            os_name_list.append(matches[1][1])
            os_code_list.append(matches[2][1])
            os_type_list.append(matches[3][1])

    os.chdir(os.getcwd() + '\..')
    return main_data, os_prod_list, os_name_list, os_code_list, os_type_list


def write_to_csv(name):
    # main_data, os_prod_list, os_name_list, os_code_list, os_type_list = get_data(MAIN_DATA_PATH, INFO_PATH)
    #
    # lists = [os_prod_list, os_name_list, os_code_list, os_type_list]
    # data = []
    # counter = 0
    # for i, item in enumerate(main_data):
    #
    #     dict_data = dict.fromkeys(main_data, lists[counter])
    #     print(dict_data)
    #     counter += 1

    # with open(name, 'w+') as csv_file:
        # writer = csv.DictWriter(csv_file, fieldnames=main_data)
        # writer.writeheader()
        # writer.writerows()


write_to_csv('test.csv')
