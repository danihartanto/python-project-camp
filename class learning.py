class latihan_class():
    #Deklarasi Variabel
    var_nama = ""
    var_alamat = ""
    var_judul = ""
    get_luas = ""

    #Membuat Constructor
    def __init__ (self, judul):
        self.var_judul = judul

    #fungsi untuk input data variabel
    def get_nama (self, nama):
        self.var_nama = nama

    #fungsi untuk input alamat
    def get_alamat(self, alamat):
        self.var_alamat = alamat

    def get_luas(self,luas):
        self.get_panjang = panjang
        self.get_lebar = lebar
        self.get_luas = panjang*lebar

    #fungsi menampilkan output
    def get_output(self):
        print ("\n\n",self.var_judul)
        print ("Nama : ",self.var_nama)
        print ("Alamat : ", self.var_alamat)

obj = latihan_class("Tutor-All Programming")
var_nama = input("Nama Anda : ")
var_alamat = input ("Alamat : ")
obj.get_nama(var_nama)
obj.get_alamat(var_alamat)
obj.get_output()
