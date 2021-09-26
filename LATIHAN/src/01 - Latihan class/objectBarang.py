"""
    Membuat class + method pada file terpisah
    Lalu membuat instance / object pada file terpisah
    Dan membuat menu utama pada file 'Main.py'
"""
from classBarang import *

sabun = Barang("Sabun", 20, 5000)
shampo = Barang("Shampo", 40, 2000)
pastaGigi = Barang("Pasta Gigi", 20, 7500)
sabunPiring = Barang("Sabun Cuci Piring", 10, 3500)
sikatGigi = Barang("Sikat Gigi", 15, 5600)
deterjen = Barang("Deterjen Baju", 12, 7500)
porselain = Barang("Porcelen Toilet", 2, 22500);
mieInstan = Barang("Mie Instan", 30, 3200);
parfumRuangan = Barang("Parfum Ruangan", 2, 10000);
sarden = Barang("Sarden Kaleng", 5, 15000);
tehCelup = Barang("Teh Celup", 25, 3000);
kecapBotol = Barang("Kecap Botol", 10, 5000);
saosBotol = Barang("Saos Botol", 10, 5000);
handbody = Barang("Handbody Sachet", 10, 5000);
kondisioner = Barang("Kondisioner Sachet", 10, 1000);

# sabun.displayBarang() # Methods display dari file classBarang.py