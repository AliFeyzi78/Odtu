
x=4
x=x**2
print(x)

kenar_1 = int(input("Hesaplamak istediğiniz alanın 1. kenar değerini tamsayı olarak giriniz: "))
kenar_2 = int(input("Hesaplamak istediğiniz alanın 2. kenar değerini tamsayı olarak giriniz: "))
kenar_1 *= kenar_1
kenar_2 *= kenar_2
print(kenar_1, kenar_2)
dortgen_alan_hesapla_v2 = kenar_1*kenar_2
print("Dörtgenin Alanı:", dortgen_alan_hesapla_v2, "br2'dir")