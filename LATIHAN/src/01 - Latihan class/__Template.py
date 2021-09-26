# Membuat program aplikasi toko retail

# 1. Membuat class barang
class Barang:
    __jumlahObject = 0

    # 2. Membuat constructor
    def __init__(self, namaBarang = "<none>", jumlahStok = 0, hargaSatuan = 0):
        self.namaBarang = namaBarang
        self.jumlahStok = jumlahStok
        self.hargaSatuan = hargaSatuan
        Barang.__jumlahObject += 1

    # 3. Membuat method
    def displayBarang(self): #Method display list barang
        print("Nama  Barang :" , self.namaBarang)
        print("Stok  Barang :" , self.jumlahStok)
        print("Harga Barang :" , "Rp." , self.hargaSatuan)
        print() # indentasi

    def getSisaStok(self): #Method display nama dan sisa stok
        print("=== SISA STOK ===")
        print("Nama Barang : ", self.namaBarang)
        print("Stok tersedia : ", self.jumlahStok)
        print()

    def setTambahStok(self, jumlah): #Method tambah stok
        self.jumlahStok += jumlah
        print("=== STOK DITAMBAHKAN ===")
        print("Stok ", self.namaBarang, " ditambah ", jumlah)
        print()
        return jumlah

    @staticmethod
    def totalPembelian(self):
        total = self.hargaSatuan * self.jumlahStok
        print("Total pembelian " + self.namaBarang)
        print("Rp.", total)
        print()
        return total

    def jumlahObject():
        return Barang.__jumlahObject


# 4. Membuat instance / object
sabun = Barang("Sabun", 20, 5000)
shampo = Barang("Shampo", 40, 2000)
pastaGigi = Barang("Pasta Gigi", 20, 7500)
sabunPiring = Barang("Sabun Cuci Piring", 10, 3500)
sikatGigi = Barang("Sikat Gigi", 15, 5600)
deterjen = Barang("Deterjen Baju", 12, 7500)

# Display program
print("\n==== Aplikasi Toko Retail ====")
sabun.displayBarang()
shampo.displayBarang()
pastaGigi.displayBarang()
# sabunPiring.displayBarang()
# sikatGigi.displayBarang()
# deterjen.displayBarang()


# print("Jumlah object dibuat", Barang.jumlahObject())
# sabun.getSisaStok()
# sabun.setTambahStok(5)
# sabun.getSisaStok()
Barang.totalPembelian(sabun)
Barang.totalPembelian(shampo)
Barang.totalPembelian(pastaGigi)
