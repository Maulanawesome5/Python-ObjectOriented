"""
    Membuat class + method pada file terpisah
    Lalu membuat instance / object pada file terpisah
    Dan membuat menu utama pada file 'Main.py'
"""

from objectBarang import *
from classBarang import *

print("\n==== Aplikasi Toko Retail ====")
sabun.displayBarang()
# shampo.displayBarang()
# pastaGigi.displayBarang()
# sabunPiring.displayBarang()
# sikatGigi.displayBarang()
# deterjen.displayBarang()


# print("Jumlah object dibuat", Barang.jumlahObject())
sabun.getSisaStok()
sabun.setTambahStok(5)
sabun.getSisaStok()
sabun.kurangiStok(6)
sabun.getSisaStok()
# Barang.totalPembelian(sabun)
# Barang.totalPembelian(shampo)
# Barang.totalPembelian(pastaGigi)

