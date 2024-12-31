from tkinter import *
root=Tk()
root.title("IIC")
root.geometry("500x778")
root.minsize(500,774)
root.maxsize(500,774)
root.config(background="black")
#root.wm_iconbitmap("--")
sv=StringVar()
sv.set("")
#click function
def click(event):
    global sv
    text=event.widget.cget("text")
    if text=="=":
        if sv.get().isdigit():
         sv.set(sv.get())
         screen.update()
        else:
         try:
           value=eval(screen.get())
           sv.set(str(value))
           screen.update()
         except Exception as e:
            r="Error"
            sv.set(r)
            screen.update()
    elif text=="AC":
        sv.set("")
        screen.update()
    else:
        sv.set(sv.get()+text)
        screen.update()
#design of Label before screen
#Label(root,text="",font="Roboto 40 bold",borderwidth=1,relief="solid",bg="black",fg="white").pack(padx=15,fill="x")
#design of screen
screen=Entry(root,textvariable=sv,borderwidth=1,relief="solid",font="Roboto 40 ")
screen.pack(fill="x",padx=15,pady=38)

#design of frame and button set 1
f=Frame(root,bg="black",borderwidth=1,relief="solid")
b=Button(f,text="9",padx=5,pady=3,font="Roboto 28 bold",relief="solid",bg="black",fg="white",borderwidth=1)
b.pack(side="left",padx=45)
b.bind('<Button-1>',click)

b=Button(f,text="8",padx=5,pady=3,font="Roboto 28 bold",relief="solid",bg="black",fg="white",borderwidth=1)
b.pack(side="left",padx=45)
b.bind('<Button-1>',click)

b=Button(f,text="7",padx=5,pady=3,font="Roboto 28 bold",relief="solid",bg="black",fg="white",borderwidth=1)
b.pack(side="left",padx=45)
b.bind('<Button-1>',click)

f.pack(fill="x",padx=15,pady=11)

#design of frame and button set 2
f=Frame(root,bg="black",borderwidth=1,relief="solid")
b=Button(f,text="6",padx=5,pady=3,font="Roboto 28 bold",relief="solid",bg="black",fg="white",borderwidth=1)
b.pack(side="left",padx=45)
b.bind('<Button-1>',click)

b=Button(f,text="5",padx=5,pady=3,font="Roboto 28 bold",relief="solid",bg="black",fg="white",borderwidth=1)
b.pack(side="left",padx=45)
b.bind('<Button-1>',click)

b=Button(f,text="4",padx=5,pady=3,font="Roboto 28 bold",relief="solid",bg="black",fg="white",borderwidth=1)
b.pack(side="left",padx=45)
b.bind('<Button-1>',click)

f.pack(fill="x",padx=15,pady=11)

#design of frame and button set 3
f=Frame(root,bg="black",borderwidth=1,relief="solid")
b=Button(f,text="3",padx=5,pady=3,font="Roboto 28 bold",relief="solid",bg="black",fg="white",borderwidth=1)
b.pack(side="left",padx=45)
b.bind('<Button-1>',click)

b=Button(f,text="2",padx=5,pady=3,font="Roboto 28 bold",relief="solid",bg="black",fg="white",borderwidth=1)
b.pack(side="left",padx=45)
b.bind('<Button-1>',click)

b=Button(f,text="1",padx=5,pady=3,font="Roboto 28 bold",relief="solid",bg="black",fg="white",borderwidth=1)
b.pack(side="left",padx=45)
b.bind('<Button-1>',click)

f.pack(fill="x",padx=15,pady=11)

#design of frame and button set 4
f=Frame(root,bg="black",borderwidth=1,relief="solid")
b=Button(f,text="+",padx=5,pady=3,font="Roboto 28 bold",relief="solid",bg="black",fg="white",borderwidth=1)
b.pack(side="left",padx=45)
b.bind('<Button-1>',click)

b=Button(f,text="-",padx=5,pady=3,font="Roboto 28 bold",relief="solid",bg="black",fg="white",borderwidth=1)
b.pack(side="left",padx=45)
b.bind('<Button-1>',click)

b=Button(f,text=" *",padx=5,pady=3,font="Roboto 28 bold",relief="solid",bg="black",fg="white",borderwidth=1)
b.pack(side="left",padx=45)
b.bind('<Button-1>',click)

f.pack(fill="x",padx=15,pady=11)

#design of frame and button set 5
f=Frame(root,bg="black",borderwidth=1,relief="solid")
b=Button(f,text="/",padx=5,pady=3,font="Roboto 28 bold",relief="solid",bg="black",fg="white",borderwidth=1)
b.pack(side="left",padx=45)
b.bind('<Button-1>',click)

b=Button(f,text="%",padx=5,pady=3,font="Roboto 28 bold",relief="solid",bg="black",fg="white",borderwidth=1)
b.pack(side="left",padx=45)
b.bind('<Button-1>',click)

b=Button(f,text="=",padx=5,pady=3,font="Roboto 28 bold",relief="solid",bg="black",fg="white",borderwidth=1)
b.pack(side="left",padx=45)
b.bind('<Button-1>',click)

f.pack(fill="x",padx=15,pady=11)

#design of frame and button set 6
f=Frame(root,bg="black",borderwidth=1,relief="solid")
b=Button(f,text="0",pady=3,font="Roboto 28 bold",relief="solid",bg="black",fg="white",borderwidth=1)
b.pack(side="left",padx=42)
b.bind('<Button-1>',click)

b=Button(f,text="AC",padx=1,pady=3,font="Roboto 28 bold",relief="solid",bg="black",fg="white",borderwidth=1)
b.pack(side="left",padx=45)
b.bind('<Button-1>',click)

f.pack(fill="x",padx=15,pady=11)

root.mainloop()