print()
print('1.Задача: Удалить из текста все слова, содержащие ""абв""')
with open('text.txt', 'r', encoding = 'utf_8') as data:
    s = data.read().split()
print(f'В файле записано: {s}')
print('Удалили все слова с абв и получили: ')
print(' '.join([word for word in s if 'абв' not in word]))
print()
