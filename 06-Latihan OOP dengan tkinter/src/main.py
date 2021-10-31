import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text="Label 1")
label2 = tkinter.Label(main_window, text="Label 2")
tombol1 = tkinter.Button(main_window, text="Tombol 1")
tombol2 = tkinter.Button(main_window, text="Tombol 2")

# Method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# Method untuk menampilkan window GUI
main_window.mainloop()