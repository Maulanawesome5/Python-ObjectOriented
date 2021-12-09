# method resolution order // multiple inheritance

class A:
    def show(self):
        print("Ini adalah show A")


class B:
    def show(self):
        print("Ini adalah show B")


class C(A,B):
    # method akan dilakukan sesuai urutan inherit C-A-B
    # jika dibalik, maka yang terjadi adalah kebalikannya
    pass


obyek = C()
obyek.show()
# help(obyek) #Ini adalah method resolution order