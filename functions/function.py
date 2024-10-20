# def toplama():
#     print('toplama')

# toplama()
# print(toplama)

# -----------------------------


# def toplama():
#     print('toplama')
#     return 'gulcin'

# x = toplama()
# print(x)

# -------------------------------


def toplama(a, b=3):
    """
    verilen a ve b parametresi icin toplama islemi gercekleşir
    """
    return a + b

help(toplama)
x = toplama(2)
print(x)