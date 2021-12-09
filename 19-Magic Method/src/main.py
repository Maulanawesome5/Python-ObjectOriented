# Magic method - Fungsi atau method bawaan dari python yang
# memiliki kegunaan khusus

class Mangga:
    
    # __init__ merupakan satu contoh magic method
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    # __repr__ juga merupakan satu lagi magic method. Dipakai saat debug
    def __repr__(self):
        return f"Mangga {self.nama} sebanyak {self.jumlah} buah."
    
    # __str__ juga merupakan satu lagi magic method. Dipakai saat production
    def __str__(self):
        return f"Mangga {self.nama} sebanyak {self.jumlah} buah."

    # __add__ magic method untuk aritmatika
    def __add__(self, objek):
        return self.jumlah + objek.jumlah


belanja1 = Mangga('Arumanis', 10)
belanja2 = Mangga('Cempedak', 15)
print(repr(belanja1))
print(belanja2)
print(belanja1 + belanja2) # implementasi magic method __add__

