class Luas_Trapesium :
    def luas(self, a, b, t):
        return 0.5 * (a + b) * t

operasi = Luas_Trapesium()
print("Luas Trapesium dengan panjang 7 lebar 5 dan tinggi 14 adalah: "+ str(operasi.luas(7, 5, 14)))