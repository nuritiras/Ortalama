def ortalama(yazili1,yazili2,per1,per2):
    ort=(yazili1+yazili2+per1+per2)/4.0
    return ort

sonuc=ortalama(100,50,25,50)

if sonuc<50:
    print(sonuc,"notuyla kaldınız")
else:
    print(sonuc,"notuyla geçti")

