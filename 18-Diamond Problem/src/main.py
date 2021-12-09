# Diamond problem - masalah yang muncul saat melakukan
# multiple inheritance. Disebut diamond karena alurnya
# akan dieksekusi seperti 4 arah

class A:
    def show(self):
        print("Ini adalah show A")


class B(A):
    def show(self):
        print("Ini adalah show B")


class C(A):
    def show(self):
        print("Ini adalah show C")


class D(B,C):
    pass


obyek = D()
obyek.show()
help(obyek) #Ini adalah method resolution order