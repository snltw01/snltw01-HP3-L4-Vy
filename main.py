import tkinter as tk
root=tk.Tk()

root.geometry("500x600+100+50")
root.configure(bg="black")

def Info():
    print(en1.get())

frame1=tk.Frame(root,background="green")
frame1.pack(expand=True)

label = tk.Label(frame1, text="Văn bản 1", font=("Arial",12,"bold"), fg="white", bg="blue")
label.pack()
#expand, fill, side

en1=tk.Entry(frame1, font=("Arial",12,"bold"))
en1.pack()

but1=tk.Button(frame1, text="Nhấn vào tôi",font=("Arial",12,"bold"), command=Info)
but1.pack()

root.mainloop()