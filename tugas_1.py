class bilPrima:
    def __init__(self):
        self.awal=0
        self.akhir=0
    def mainPrima(self):
        self.awal=int(input("masukkan angka pertama: "))
        self.akhir=int(input("masukkan batas prima: "))
        self.data=[]
        if self.awal >= 1 and self.akhir > 1:
            for x in range(self.awal,self.akhir):
                xprima = True
                for i in range (2,x):
                    if(x%i == 0):
                        xprima = False
                if xprima == True:
                    self.data.append(x)
        else:
            print("inputan salah")
        return self.data
    def jumlahPrima(self):
        z=len(self.data)
        print("bilangan prima ditampilkan: ",self.awal,"sampai",self.akhir,"adalah: ",z)
    def display(self):
        print(self.data)
tes=bilPrima()
tes.mainPrima()
tes.display()
tes.jumlahPrima()
