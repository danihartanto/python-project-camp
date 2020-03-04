class Pegawai:
    def __init__(self,nama,gaji=0):
        self.nama=nama
        self.gaji=gaji
    def tunjangan(self,persen):
        self.gaji = self.gaji+(self.gaji*persen)
    def kerja(self):
        print(self.nama, "pekerjaannya")
    def __repr__(self):
        return"Pegawai: nama= %s,gaji=Rp.%s"%(self.nama,self.gaji)
class Koki(Pegawai):
    def __init__(self,nama):
        Pegawai.__init__(self,nama,100000)
    def kerja(self):
        print(self.nama,"membuat makanan")
class Pelayan(Pegawai):
    def __init__(self,nama):
        Pegawai.__init__(self,nama,50000)
    def kerja(self):
        print(self.nama,"melayani costumer")
class Pizzarobot(Koki):
    def __init__(self,nama):
        Koki.__init__(self,nama)
    def kerja(self):
        print(self.nama,"membuat pizza")

#program utama
if __name__=="__main__":
    agus=Pizzarobot("Agus")
    print(agus)
    agus.kerja()
    agus.tunjangan(0.20)
    print(agus)
    print()
    for kelas in Pegawai,Koki,Pelayan,Pizzarobot:
        objek=kelas(kelas.__name__)
        objek.kerja()
