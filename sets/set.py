# alacaklar = set()

# # print(dir(alacaklar)) setle kullanilacak fonksiyonları görmek için

# alacaklar.add('araba')
# alacaklar.add('ev')
# alacaklar.add('kitap')
# alacaklar.add('kitap')

# print(alacaklar)
# print("\n")

# alacaklar.remove('kitap')
# print(alacaklar)
# print("\n")

# alacaklar.discard('agac') # varsa siler yoksa hata vermez
# print(alacaklar)

# # alacaklar.clear() # her seyi siler
# # print(alacaklar)


# # bu iki sekildede tanimlanabilir
# alacaklar = set(['elma', 'armut', 'kiraz'])
# alacaklar = {'elma', 'armut', 'kiraz'}

# print(alacaklar)

tek_sayilar = set([1, 3, 5, 7, 9])
cift_sayilar = {2, 4, 6, 8}

print(cift_sayilar.union(tek_sayilar)) # birlesim
print(cift_sayilar.intersection(tek_sayilar)) # kesisim

