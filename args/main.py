# def toplama(x, y):
#     return x + y

# toplam = toplama(y=2,x=4)

# print(toplam)

def toplama(*args, **kwargs):
    print(args)
    print(kwargs)

toplama(1, 2, 3, 4, y=2, x=4)