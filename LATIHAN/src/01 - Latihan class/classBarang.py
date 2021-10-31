class Barang:
    __jumlahObject = 0

    # Constructor
    def __init__(self, namaBarang = "<none>", jumlahStok = 0, hargaSatuan = 0):
        self.namaBarang = namaBarang
        self.jumlahStok = jumlahStok
        self.hargaSatuan = hargaSatuan
        Barang.__jumlahObject += 1

    # Class Method
    # Method display list barang
    def displayBarang(self):
        print("Nama  Barang :" , self.namaBarang)
        print("Stok  Barang :" , self.jumlahStok)
        print("Harga Barang :" , "Rp." , self.hargaSatuan)
        print() # indentasi

    # Method display nama dan sisa stok
    def getSisaStok(self):
        print("=== STOK TERSEDIA ===")
        print("Nama Barang : ", self.namaBarang)
        print("Stok tersedia : ", self.jumlahStok)
        print()

    # Method tambah stok
    def setTambahStok(self, jumlah):
        self.jumlahStok += jumlah
        print("=== STOK DITAMBAHKAN ===")
        print("Stok ", self.namaBarang, " ditambah ", jumlah)
        print()
        return jumlah

    def kurangiStok(self, jumlah):
        self.jumlahStok -= jumlah
        print("=== STOK DIKURANGI ===")
        print("Stok ", self.namaBarang, " dikurangi ", jumlah)
        print()
        return jumlah

    @staticmethod
    def totalPembelian(self):
        total = self.hargaSatuan * self.jumlahStok
        print("Total pembelian " + self.namaBarang)
        print("Rp.", total)
        print()
        return total

    @classmethod
    def jumlahObject():
        return Barang.__jumlahObject