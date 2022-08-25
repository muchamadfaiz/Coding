import tkinter as tink

main_Window = tink.Tk()

label1 = tink.Label(main_Window, text="label1")  # Label = "Class"
label2 = tink.Label(main_Window, text="label2")  # Label = "Class"

tombol1 = tink.Button(main_Window, text="tombol1")  # Button = "Class"
tombol2 = tink.Button(main_Window, text="tombol2")  # Button = "Class"

# method positioning
label1.pack()  # pack = method/fungsi
label2.pack()  # pack = method/fungsi
tombol1.pack()  # pack = method/fungsi
tombol2.pack()  # pack = method/fungsi

# method menampilkan GUI
main_Window.mainloop()
