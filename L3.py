def div(x, y):
    try:
        print(x/y)
    except BaseException:
        print('Bug')
    else:
        print(x/y)

div(10,5)
