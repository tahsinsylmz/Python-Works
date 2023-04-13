sayi1 = int(input("Başlangıç sayısı:"))
while sayi1 != 0:
    sayi2 = sayi1
    toplamsal_devamlılık = 0
    carpımsal_devamlılık = 0
    while sayi1 >= 10:
        toplamsal_devamlılık += 1
        basamak_list = [int(x) for x in str(sayi1)]
        toplam = 0
        toplam_ifade = ""
        for number in basamak_list:
            toplam += number
            toplam_ifade += str(number) + " + "
        print("Rakamlar Toplmaı  " + str(toplam_ifade[:-2]) + " = " + str(toplam))
        sayi1 = toplam
        print("Yeni sayı : " + str(sayi1))
    print("Toplamsal devamlılık = " + str(toplamsal_devamlılık) + ", Toplamsal devamlılık kökü = " + str(sayi1))

    while sayi2 >= 10:
        carpımsal_devamlılık += 1
        basamak_list2 = [int(x) for x in str(sayi2)]
        carpım = 1
        carpım_ifade = ""
        for number in basamak_list2:
            carpım *= number
            carpım_ifade += str(number) + " * "
        print("Rakamlar Çarpımı  " + str(carpım_ifade[:-2]) + " = " + str(carpım))
        sayi2 = carpım
        print("Yeni sayı : " + str(sayi2))
    print("Çarpımsal devamlılık = " + str(carpımsal_devamlılık) + ", Çarpımsal devamlılık kökü = " + str(sayi2))
    sayi1 = int(input("Yeni sayı giriniz :"))


