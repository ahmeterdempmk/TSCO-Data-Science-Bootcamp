sayi = int(input("Bir sayı giriniz: "))
asalMi = True

if sayi < 2:
    asalMi = False
else:
    for i in range(2, sayi):
        if sayi % i == 0:
            asalMi = False
            break

if asalMi:
    print("Sayı asaldır.")
else:
    print("Sayı asal değildir.")