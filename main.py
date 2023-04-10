import requests
from bs4 import BeautifulSoup
import os.path
import json
from datetime import datetime



def first_task():
    n = int(input('Введите положительное 2-байтное целое число (от 0 до 65535): '))
    if n < 0 or n > 65534:
        raise ValueError(
            'Некорректный ввод. Введите положительное 2-байтное целое число (от 0 до 65535)')

    low_byte = n & 0xFF
    high_byte = n >> 8

    new_n = (low_byte << 8) | high_byte
    print(f'Новое число:', new_n)


def second_task():
    n = int(input('Введите количество корзин\n'))
    w = int(input('Введите вес монеты\n'))
    d = int(input('Введите разницу в весе фальшивой монеты\n'))
    p = int(input('Введите суммарный вес монет\n'))
    s = 0
    for i in range(1, n):
        s += i * w
    if s == p:
        print(n)
    else:
        print((s - p) // d)

def third_task():
    response = requests.get('https://www.python.org')
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    text = soup.get_text()
    text = text.replace('\xa0', '')

    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    with open('readme.md', 'w', encoding="utf-8") as f:
        f.write('| Symbol | Count |\n')
        f.write('| ------ | ----- |\n')
        for char, count in sorted(char_counts.items()):
            if char != '\n' and char != '\r':
                f.write(f'| {char} | {count} |\n')


def fourth_task():
    with open('example.json', 'r') as f:
        data = json.load(f)

    for person in data['people']:
        person['updated'] = datetime.now().isoformat()

    with open('example.json', 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    while(True):
        task_number = int(input('введите номер задачи или 0 для завершения \n'))
        if task_number == 1:
            first_task()
        elif task_number == 2:
            second_task()
        elif task_number == 3:
            third_task()
        elif task_number == 4:
            fourth_task()
            print('Поля "updated" успешно изменены')
        elif task_number == 0:
            break