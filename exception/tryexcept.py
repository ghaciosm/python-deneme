sayi1 = input("SAYI1:")
sayi2 = input("SAYI2:")

try:
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    if sayi2 == 0:
        raise ZeroDivisionError
    print(sayi1 / sayi2)
# except ValueError:
#     print("lütfen 10 luk tabanda sayi girin")

# except ZeroDivisionError:
#     print("Bir sayi 0'a bölünemez")

except (ValueError, ZeroDivisionError):
    print("Bir hata oluştu")
else:
    print("kod calisiyor")
finally: # her türlü calisicak
    print("finally calisiyor")