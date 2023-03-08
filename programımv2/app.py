from tkinter import *

def save_info():
    scode_info = scode.get()
    print(scode_info)

    file = open("codes.txt","a")
    file.write(scode_info + "\n")
    file.close()


pencere = Tk()
pencere.geometry("250x100")
pencere.title("Kaydedici")

scode = StringVar()
scode_entry = Entry(textvariable = scode)
scode_entry.place(x=10,y=10)

kayit = Button(pencere,text = "Kayıt",width=5,height=2,bg="#0000ff",command=pencere.destroy and save_info)
kayit.place(x=30,y=30)


pencere.mainloop()
