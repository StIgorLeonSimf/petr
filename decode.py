with open('code.txt', encoding='utf-8') as file:
    s = file.read()
    key = input('Введите ключ шифрования: ')
    secret = ''
    for i in s:
        code = ord(i) - int(key)
        symbol = chr(code)
        secret += symbol
    print('Текст расшифрован!!!')

with open('decode.txt', 'w', encoding='utf-8') as file:
    file.write(secret)
print('Файл для чтения "decode.txt" сформирован!!!')


