import json
import random
# girdi.txt isimli metin dosyasını açıp içerisindeki sözlükten satır ve sütun bilgisini alır.
f = open("girdi.txt", "r")
sat_sut = json.load(f)
satirlar = sat_sut["Satir"]
sutunlar = sat_sut["Sutun"]

# Satır ve sütun sayısına göre rastgele sayılardan oluşan bir oyun tahtası oluştur
oyun_tahta = [[random.randint(0, 9) for _ in range(sutunlar)] for _ in range(satirlar)]


def fibonacci_hesap(n):
    # Fibonacci değerini hesaplayan fonksiyon
    if n < 2:
        return n
    else:
        return fibonacci_hesap(n - 1) + fibonacci_hesap(n - 2)


def hamle_puani_hesapla(silinen_hucreler, secilen_sayi):
    # Puan hesabı yapan fonksiyon
    return fibonacci_hesap(silinen_hucreler) * secilen_sayi


def tahta_yazdir(tahta):
    print(" ")
    # Oyun tahtasını ekrana yazdırır
    for satir1 in tahta:
        print(' '.join(map(str, satir1)))


def hamle_kontrol(tahta, satir, sutun, sayi):
    # Seçilen numaranın komşularında aynı sayı varsa True dönüşü yapar.
    if satir > 0 and tahta[satir - 1][sutun] == sayi:
        return True
    if sutun > 0 and tahta[satir][sutun - 1] == sayi:
        return True
    if satir < len(tahta)-1 and tahta[satir + 1][sutun] == sayi:
        return True
    if sutun < len(tahta[0])-1 and tahta[satir][sutun + 1] == sayi:
        return True
    return False


def oyun_bitimi(tahta):
    # Tahtanın her hücresinin etrafındaki hücreleri kontrol et
    for satir in range(len(tahta)):
        for sutun in range(len(tahta[0])):
            sayi = tahta[satir][sutun]
            # Hücre boş değilse ve yanındaki hücrelerle eş değilse, oyun biter.
            if sayi != " ":
                if satir > 0 and tahta[satir - 1][sutun] == sayi:
                    continue
                if sutun > 0 and tahta[satir][sutun - 1] == sayi:
                    continue
                if satir < len(tahta)-1 and tahta[satir + 1][sutun] == sayi:
                    continue
                if sutun < len(tahta[0])-1 and tahta[satir][sutun + 1] == sayi:
                    continue
                return True
    return False


def tahta_durum(tahta):
    # Oyun tahtasındaki tüm konumları kontrol eder
    for satir in range(len(tahta)):
        for sutun in range(len(tahta[0])):
            # Eğer herhangi bir hücrede değer varsa False dönüş yapar.
            if isinstance(tahta[satir][sutun], int):
                return False
    # Eğer hiçbir hücrede sayı yoksa True döndür
    return True


def tahta_yenile(tahta):
    # Bitişik sayılar kalmayana veya herhangi bir hücrenin etrafındaki hücrelerle
    # aynı sayıda olmamasına kadar oyun devam eder
    sayi_secim = []  # her hamlede seçilen sayı değerleri için bir liste oluşturuldu
    puan1 = 0  # puan için değişken oluşturuldu

    while not (oyun_bitimi(tahta) and tahta_durum(tahta)):
        silinen_hucre = 0
        satir = int(input('Satır seçin (1-{}): '.format(len(tahta)))) - 1
        sutun = int(input('Sütun seçin (1-{}): '.format(len(tahta[0])))) - 1
        sayi = tahta[satir][sutun]
        sayi_secim.append(sayi)  # her hamlede seçilen sayı değeri listeye eklenir

        if not hamle_kontrol(tahta, satir, sutun, sayi):
            print('Seçilen sayı, komşularında yok. Lütfen tekrar seçin.')
            tahta_yazdir(oyun_tahta)
            continue
        # Bitişik sayıları sil
        hucre_sec = [(satir, sutun)]
        while hucre_sec:
            silinen_hucre += 1
            sat, sut = hucre_sec.pop(0)

            if tahta[sat][sut] == sayi:
                tahta[sat][sut] = " "

                if sat > 0 and tahta[sat - 1][sut] == sayi:
                    hucre_sec.append((sat-1, sut))
                    hucre_sec.append((sat, sut))
                    silinen_hucre -= 1

                if sut > 0 and tahta[sat][sut - 1] == sayi:
                    hucre_sec.append((sat, sut-1))

                if sat < len(tahta)-1 and tahta[sat + 1][sut] == sayi:
                    hucre_sec.append((sat+1, sut))

                if sut < len(tahta[0])-1 and tahta[sat][sut + 1] == sayi:
                    hucre_sec.append((sat, sut+1))

            # Sayılar aşşağıya düzenli bir biçimde iner
            for sutun in range(len(tahta[0])):
                # Boşlukların altındaki sayıların yerlerini değiştir
                for satir in range(len(tahta) - 1, -1, -1):
                    if tahta[satir][sutun] == " ":
                        for sat in range(satir - 1, -1, -1):
                            if tahta[sat][sutun] != " ":
                                tahta[satir][sutun], tahta[sat][sutun] = tahta[sat][sutun], tahta[satir][sutun]
                                break
        # Yeniden tahtayı yazdır
        puan1 += hamle_puani_hesapla(silinen_hucre, sayi)
        print("\n-----------------------------")
        print(f"Toplam Puan : {puan1}")
        tahta_yazdir(oyun_tahta)

        # Oyunun devam edip etmediğini kontrol eder
        hamle_var = False
        for satir in range(len(tahta)):
            for sutun in range(len(tahta[0])):
                if tahta[satir][sutun] != " " and hamle_kontrol(tahta, satir, sutun, tahta[satir][sutun]):
                    hamle_var = True
                    break
            if hamle_var:
                break

        # Oyunun devam edip etmediğine göre dögüyü bitirir veya devam ettirir.
        if not hamle_var:
            # oyunun son hali için çıktı dosyası yoksa oluştur ve tahtayı  ve puan değerini ekler
            # çıktı dosyası varsa içeriğini temizleyip tahtanın son halini ve puan değerini ekler
            with open("cıktı.txt", "w") as dosya:
                dosya.seek(0)
                dosya.write("Son tahta durumu:\n")
                for i in range(satirlar):
                    dosya.write(" ".join(str(x) for x in tahta[i]) + "\n")
                dosya.write(f"\nToplam Puan : {puan1}")

            print('Oyun bitti!')
            break


tahta_yazdir(oyun_tahta)
tahta_yenile(oyun_tahta)
