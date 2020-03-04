class mahasiswa:
    def __init__(self,nama,nim):
        self.var_nama=nama
        self.var_nim=nim
    def set_nama(self,new_nama):
        self.var_nama=new_nama
    def set_nim(self,new_nim):
        self.var_nim=new_nim
    def get_nama(self):
        return self.var_nama
    def get_nim(self):
        return self.var_nim
    def tampil(self):
        print("nama: ",self.var_nama)
        print("nim: ",self.var_nim)
nama=input("masukkan nama: ")
nim=int(input("masukkan nim: "))
p=mahasiswa(nama,nim)
p.tampil()
p.set_nama("budiono")
p.set_nim("1788")
p.tampil()
p.get_nama()
print(p.get_nama())
print(p.get_nim())

