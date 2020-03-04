class rumus:
    def menu(self):
        print("\n1. persegi","\n2. persegi panjang","\n3. Jajar Genjang","\n4. Trapesium","\n5. Layang-Layang","\n6. Segitiga","\n7. Belah Ketupat","\n8. Lingkaran")
        pil=input("\nmasukkan pilihan anda: ")
        
        if (pil=="1"):
            print("")
            bangun.persegi()
            bangun.ulang()
        if (pil=="2"):
            print("")
            bangun.persegipanjang()
            bangun.ulang()
        if (pil=="3"):
            print("")
            bangun.jajargenjang()
            bangun.ulang()
        if (pil=="4"):
            print("")
            bangun.trapesium()
            bangun.ulang()
        if (pil=="5"):
            print("")
            bangun.layang()
            bangun.ulang()
        if (pil=="6"):
            print("")
            bangun.segitiga()
            bangun.ulang()
        if (pil=="7"):
            print("")
            bangun.belahketupat()
            bangun.ulang()
        if (pil=="8"):
            print("")
            bangun.lingkaran()
            bangun.ulang()
        else:
              print("pilihan tidak ditemukan")
              bangun.menu()

    def persegi(self):
        s=int(input("masukkan nilai sisi persegi: "))
        luaspersegi=s*s
        print("luas persegi: ",luaspersegi)
        
    def persegipanjang(self):
        p=int(input("masukkan nilai panjang: "))
        l=int(input("masukkan nilai lebar: "))
        luaspersegipanjang=p*l
        print("luas persegi panjang adalah: ",luaspersegipanjang)
        
    def jajargenjang(self):
        a=int(input("masukkan nilai alas: "))
        t=int(input("masukkan nilai tinggi: "))
        luasjajargenjang=a*t
        print("luas jajar genjang adalah: ", luasjajargenjang)
        
    def trapesium(self):
        sisiA=int(input("masukkan nilai sisi pertama: "))
        sisiB=int(input("masukkan nilai sisi kedua: "))
        t=int(input("masukkan nilai tinggi: "))
        luastrapesium=((sisiA+sisiB)*t)/2
        print("luas jajar genjang adalah: ", luastrapesium)
        
    def layang(self):
        diagonalA=int(input("masukkan nilai Diagonal pertama: "))
        diagonalB=int(input("masukkan nilai Diagonal kedua: "))
        luaslayang=(diagonalA*diagonalB)/2
        print("luas jajar genjang adalah: ", luaslayang)

    def segitiga(self):
        alas=int(input("masukkan nilai Alas: "))
        tinggi=int(input("masukkan nilai Tinggi: "))
        luassegitiga=(alas*tinggi)/2
        print("luas jajar genjang adalah: ", luassegitiga)

    def belahketupat(self):
        diagonalA=int(input("masukkan nilai diagonal pertama: "))
        diagonalB=int(input("masukkan nilai diagonal kedua: "))
        luasbelahketupat=(diagonalA*diagonalB)/2
        print("luas jajar genjang adalah: ", luasbelahketupat)
        
    def lingkaran(self):
        jari=int(input("masukkan nilai jari-jari: "))
        phi=3.14
        luaslingkaran=(jari*jari)*phi
        print("luas jajar genjang adalah: ", luaslingkaran)
        

    def ulang(self):
        ulang = input("mau coba lagi?(Y/N)")
        if (ulang == "Y"):
            bangun.menu()
        elif(ulang == "N"):
            print("terima kasih")
            quit()
        else:
            print("pilih (Y/N)")
            bangun.ulang()

bangun=rumus()
bangun.menu()
bangun.persegi()
bangun.persegipanjang()
bangun.jajargenjang()
bangun.trapesium()
bangun.layang()
bangun.segitiga()
bangun.belahketupat()
bangun.lingkaran()
