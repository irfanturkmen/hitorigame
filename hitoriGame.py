def oyun_olustur(file):
    rfile = open(file, "r")
    satirlar = rfile.readline()
    oyun_dizisi = []

    while satirlar !="":
        satir = []
        for i in satirlar.split():
            satir.append('-'+i+'-')
        oyun_dizisi.append(satir)
        satirlar = rfile.readline()
    return oyun_dizisi

def oyun_alanini_goster(oyun_dizisi):
    print(end="   ")
    for i in range(len(oyun_dizisi)):
        print(i + 1, end="  ")

    print()
    for i in range(len(oyun_dizisi)):
        print(i + 1, sep="", end=" ")
        for j in range(len(oyun_dizisi[i])):
            print(oyun_dizisi[i][j], end="")

        print()

def hamle_al(oyun_dizisi):
    print()
    print("Satır numarasını (1-",len(oyun_dizisi),"), sütun numarasını (1-",len(oyun_dizisi),") ve işlem kodunu (B:boş,"
                              "D:dolu, N:normal/işaretsiz) aralarında boşluk bırakarak giriniz:",sep="",end="")
    kullanici_girdisi = input()
    hamle = kullanici_girdisi.split()
    def hamle_hata_kontrol(hamle):

        while len(hamle) != 3 or hamle[2] not in "BDN":
            print("HATALI HAMLE! TEKRAR GIRIS YAPINIZ.")
            print("Satır numarasını (1-", len(oyun_dizisi), "), sütun numarasını (1-", len(oyun_dizisi),
                  ") ve işlem kodunu "
                  "(B:boş,D:dolu, N:normal/işaretsiz) aralarında boşluk bırakarak giriniz:", sep="", end="")
            kullanici_girdisi = input()
            hamle = kullanici_girdisi.split()

        return hamle

    while True:
        try:
            hamle = hamle_hata_kontrol(hamle)
            while int(hamle[0]) not in range(1,len(oyun_dizisi)+1) or int(hamle[1]) not in range(1,len(oyun_dizisi)+1):
                print(end="")
                kullanici_girdisi = input("Lutfen oyun alani icinde gecerli olan hamle yapiniz: ")
                hamle = kullanici_girdisi.split()
                hamle = hamle_hata_kontrol(hamle)
            break
        except ValueError:
            print(end="")
            print("Lütfen girdiye uygun sayısal bir değer giriniz!:")
            kullanici_girdisi = input()
            hamle = kullanici_girdisi.split()
    return hamle

def oyun_tahtasi_duzenle(oyun_dizisi,oyun_dizisi_kopya):

    hamle = hamle_al(oyun_dizisi)
    satir = int(hamle[0]) - 1
    sutun = int(hamle[1]) - 1
    if (hamle[2] == 'B'):
        oyun_dizisi[satir][sutun] = '-x-'

    if (hamle[2] == 'D'):
        if (oyun_dizisi[satir][sutun][1] == 'x'):
            oyun_dizisi[satir][sutun] = '(' + oyun_dizisi_kopya[satir][sutun][1] + ')'
        else:
            oyun_dizisi[satir][sutun] = '(' + oyun_dizisi[satir][sutun][1] + ')'

    if (hamle[2] == 'N'):
        if (oyun_dizisi[satir][sutun][1] == 'x'):
            oyun_dizisi[satir][sutun] = '-' + oyun_dizisi_kopya[satir][sutun][1] + '-'
        else:
            oyun_dizisi[satir][sutun] = '-' + oyun_dizisi[satir][sutun][1] + '-'

    oyun_alanini_goster(oyun_dizisi)

def satir_sutun_ayni_sayi_kontrol_satir(oyun_dizisi):
    for i in range(len(oyun_dizisi)):
        for j in range(len(oyun_dizisi)):
            for k in range(len(oyun_dizisi)):
                if(oyun_dizisi[i][j][1]==oyun_dizisi[i][k][1] and j!=k):#Kendisiyle karsilastirma yapmaz!
                    if (oyun_dizisi[i][j][1] != 'x'):
                        return False
    return True

def satir_sutun_ayni_sayi_kontrol_sutun(oyun_dizisi):
    for i in range(len(oyun_dizisi)):
        for j in range(len(oyun_dizisi)):
            for k in range(len(oyun_dizisi)):
                if(oyun_dizisi[i][j][1]==oyun_dizisi[k][j][1] and k!=i):#Kendisiyle karsilastirma yapmaz!
                    if(oyun_dizisi[i][j][1]!='x'):
                        return False
    return True

def ayni_sayi_kontrol(oyun_dizisi):
    if (satir_sutun_ayni_sayi_kontrol_satir(oyun_dizisi) or satir_sutun_ayni_sayi_kontrol_sutun(oyun_dizisi)):
        return  True
    return False

def dolu_kare_komsu_kontrol(oyun_dizisi):
    oyun_dizisi_dolu_say = []
    dolu_say=0

    for i in range(len(oyun_dizisi)):
        for j in range(len(oyun_dizisi)):
            if(oyun_dizisi[i][j][0]=='(' and oyun_dizisi[i][j][2]==')'):
                dolu_say+=1
                if(i+1>=len(oyun_dizisi) or j+1>=len(oyun_dizisi)):
                    kucuk_kontrol = i-1>=0 and j-1>=0
                    if (oyun_dizisi[i][j][0] == oyun_dizisi[i][j-1][0]) and kucuk_kontrol:
                        if str(i)+""+str(j)+str(i)+""+str(j-1) and str(i)+""+str(j-1)+str(i)+""+str(j) not in oyun_dizisi_dolu_say :
                            oyun_dizisi_dolu_say.append(str(i)+""+str(j)+str(i)+""+str(j-1))
                    if(oyun_dizisi[i][j][2] ==oyun_dizisi[i-1][j][2]) and kucuk_kontrol:
                        if str(i)+""+str(j)+str(i-1)+""+str(j) and str(i-1)+""+str(j)+str(i)+""+str(j) not in oyun_dizisi_dolu_say:
                            oyun_dizisi_dolu_say.append(str(i)+""+str(j)+str(i-1)+""+str(j))
                elif(i-1<0 or j-1<0):
                    buyuk_kontrol = i+1<=len(oyun_dizisi) and j+1<=len(oyun_dizisi)
                    if (oyun_dizisi[i][j][0] == oyun_dizisi[i][j+1][0]) and buyuk_kontrol:
                        if str(i)+""+str(j)+str(i)+""+str(j+1) and str(i)+""+str(j+1)+str(i)+""+str(j) not in oyun_dizisi_dolu_say:
                            oyun_dizisi_dolu_say.append(str(i)+""+str(j)+str(i)+""+str(j+1))
                    if(oyun_dizisi[i][j][2] == oyun_dizisi[i+1][j][2]) and buyuk_kontrol:
                        if str(i)+""+str(j)+str(i+1)+""+str(j) and str(i+1)+""+str(j)+str(i)+""+str(j) not in oyun_dizisi_dolu_say:
                            oyun_dizisi_dolu_say.append(str(i)+""+str(j)+str(i+1)+""+str(j))
                elif(oyun_dizisi[i][j][0]==oyun_dizisi[i][j+1][0] or oyun_dizisi[i][j][2]==oyun_dizisi[i+1][j][2]
                   or oyun_dizisi[i][j][0]==oyun_dizisi[i][j-1][0] or oyun_dizisi[i][j][2]==oyun_dizisi[i-1][j][2]):
                    if(oyun_dizisi[i][j][0]==oyun_dizisi[i][j+1][0]):
                        if str(i)+""+str(j)+str(i)+""+str(j+1) and str(i)+""+str(j+1)+str(i)+""+str(j) not in oyun_dizisi_dolu_say:
                            oyun_dizisi_dolu_say.append(str(i)+""+str(j)+str(i)+""+str(j+1))
                    elif (oyun_dizisi[i][j][0] == oyun_dizisi[i+1][j][0]):
                        if str(i)+""+str(j)+str(i+1)+""+str(j) and str(i+1)+""+str(j)+str(i)+""+str(j) not in oyun_dizisi_dolu_say:
                            oyun_dizisi_dolu_say.append(str(i)+""+str(j)+str(i+1)+""+str(j))

                    elif (oyun_dizisi[i][j][0] == oyun_dizisi[i + 1][j-1][0]):
                        if str(i) + "" + str(j) + str(i) + "" + str(j-1) and str(i) + "" + str(j-1) + str(
                                i) + "" + str(j) not in oyun_dizisi_dolu_say:
                            oyun_dizisi_dolu_say.append(str(i) + "" + str(j) + str(i) + "" + str(j - 1))
                    elif (oyun_dizisi[i][j][0] == oyun_dizisi[i-1][j][0]):
                        if str(i) + "" + str(j) + str(i-1) + "" + str(j) and str(i-1) + "" + str(j) + str(
                                i) + "" + str(j) not in oyun_dizisi_dolu_say:
                            oyun_dizisi_dolu_say.append(str(i) + "" + str(j) + str(i-1) + "" + str(j))

    sifira_esitler_mi = len(oyun_dizisi_dolu_say)==0 and dolu_say==0
    if(len(oyun_dizisi_dolu_say)+1==dolu_say or sifira_esitler_mi ):#Butun elemanlar bagliysa ya da hic dolu eleman yoksa true doner
        if(len(oyun_dizisi_dolu_say)!=0):
            return True
    return False

def bos_kare_komsu_kontrol(oyun_dizisi):
    for i in range(len(oyun_dizisi)):
        for j in range(len(oyun_dizisi)):
            if(oyun_dizisi[i][j][1]=='x'):
                if(i+1>=len(oyun_dizisi) or j+1>=len(oyun_dizisi)):
                    continue
                if('x'==oyun_dizisi[i][j+1][1] or 'x'==oyun_dizisi[i+1][j][1]):
                    return False
    return True

def oyna():
    oyun_dizisi = oyun_olustur("hitori_bulmaca.txt")
    oyun_dizisi_kopya = oyun_olustur("hitori_bulmaca.txt") #oyun dizisinin bir kopyasi, x olan yerlerin tekrardan eski
                                                           #degerine dondurebilmek icin
    oyun_alanini_goster(oyun_dizisi)

    while True:
        oyun_tahtasi_duzenle(oyun_dizisi,oyun_dizisi_kopya)
        dolu_kare_komsu_kontrol(oyun_dizisi)
        if(ayni_sayi_kontrol(oyun_dizisi) and bos_kare_komsu_kontrol(oyun_dizisi) and dolu_kare_komsu_kontrol(oyun_dizisi)):
            print("Tebrikler, Bulmacayi Cozdunuz!")
            return
oyna()

