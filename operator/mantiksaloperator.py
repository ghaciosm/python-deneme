ehliyet = False
araba = True

if ehliyet and araba:
    print("araba kullanbilirsin")
# elif ehliyet or araba:
#     print("araba kullanmana çok az kaldi")
elif araba and not ehliyet:
    print("ehliyet al")
else:
    print("araba kullanman icin çok zaman var")