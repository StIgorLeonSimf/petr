import json


# d = {'black': 'черный',
#      'red': 'красный'
#      }
with open('dict.json', 'r', encoding='utf-8') as fl:
    d = json.load(fl)

while True:
    print()
    word = input('Введите слово для перевода: ')
    if word in d:
        print(f'{word} - {d[word]}')
    elif word == '123':
        break
    else:
        transl = input(f'Введите перевод для слова {word} ')
        d[word] = transl
        with open('dict.json', 'w', encoding='utf-8') as fl:
            json.dump(d, fl)

