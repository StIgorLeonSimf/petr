
while True:
    try:
        n = int(input('> '))
    except Exception as er:
        print('Sorry', er)
    else:
        print(n)
    # finally:
    #     print('also')
