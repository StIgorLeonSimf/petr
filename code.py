with open('text.txt', encoding='utf-8') as file:
    s = file.read()
    key = input('Введите ключ шифрования: ')
    secret = ''
    for i in s:
        code = ord(i) + int(key)
        symbol = chr(code)
        secret += symbol
    print('Текст зашифрован!!!')

with open('code.txt', 'w', encoding='utf-8') as file:
    file.write(secret)
print('Файл для отправки "code.txt" сформирован!!!')


