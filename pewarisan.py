class Ayah:
    def methodAyah(self):
        print("ini adalah method ayah")
class Anak(Ayah):
    def methodAnak(self):
        print("ini adalah method anak")

#deklarasi objek kelas ayah
p = Ayah()
p.methodAyah()

#deklarasi objek kelas anak
c=Anak()
c.methodAnak()
c.methodAyah()
