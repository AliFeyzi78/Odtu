
yas = int(input("Lütfen yaşınızı giriniz: "))

if yas <= 100:
    if yas < 50:
        print ("Girdiğiniz değer 0-49 arasındadır.")
    else: 
        print ("Girdiğiniz değer 50-100 arasındadır.")
else:
    print("Lütfen 0-100 arası bir değer girin!")