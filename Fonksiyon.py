# Fonksiyon 1: Dikdörtgenin alanının hesaplanması işlemini gerçekleştirecek fonksiyon hazırlanacaktır. 
# Fonksiyon ismi dortgen_alan_hesapla_v1 olacak ve kullanıcıdan iki adet tamsayı değerini girdi alarak 
# girilen değerlere göre alan hesabını yaparak sonucu kullanıcıya gösterecektir.

kenar_1 = int(input("Hesaplamak istediğiniz alanın 1. kenar değerini tamsayı olarak giriniz: "))
kenar_2 = int(input("Hesaplamak istediğiniz alanın 2. kenar değerini tamsayı olarak giriniz: "))
dortgen_alan_hesapla_v1 = kenar_1*kenar_2
print("Dörtgenin Alanı:", dortgen_alan_hesapla_v1, "br2'dir")

# Fonksiyon 2: Daire alanı hesaplayan bir fonksiyon geliştirilecektir. Fonksiyon ismi daire_alan_hesapla_v1 
# olacak ve kullanıcıdan sadece yarıçap değerini girdi olarak alacak ve girilen değere göre daire alanını 
# hesaplayarak sonucu kullanıcıya döndürecektir.

pi = 3.14
yarıcap = float(input("Hesaplamak istediğiniz alanın yarıçap değerini olarak giriniz: "))
daire_alan_hesapla_v1 = pi * yarıcap**2 
print("Darirenin Alanı:", daire_alan_hesapla_v1, "br2'dir")


# V2
kenar_1 = int(input("Hesaplamak istediğiniz alanın 1. kenar değerini tamsayı olarak giriniz: "))
kenar_2 = int(input("Hesaplamak istediğiniz alanın 2. kenar değerini tamsayı olarak giriniz: "))
kenar_1 *= kenar_1
kenar_2 *= kenar_2
dortgen_alan_hesapla_v2 = kenar_1*kenar_2
print("Dörtgenin Alanı:", dortgen_alan_hesapla_v2, "br2'dir")

yarıcap = float(input("Hesaplamak istediğiniz alanın yarıçap değerini olarak giriniz: "))
yarıcap *= yarıcap  
daire_alan_hesapla_v2 = pi * yarıcap**2 
print("Darirenin Alanı:", daire_alan_hesapla_v2, "br2'dir")



