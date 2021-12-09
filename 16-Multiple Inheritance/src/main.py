class A:
    def method_A(self):
        print("Ini adalah method A")


class B:
    def method_B(self):
        print("Ini adalah method B")


# inherit dari 'class A' dan 'class B'
class Sesuatu(A,B):
    pass


objek = Sesuatu()
objek.method_A()
objek.method_B()