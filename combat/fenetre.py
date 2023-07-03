from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
from pynput import keyboard

class MenuPrincipal(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.initinterface()
        self.mainloop()

    
    def initinterface(self):
        self.geometry("1500x700+10+10")
        self.title("la fureur des combattant")
        self.resizable(width=False, height=False)
        self.configure(bg="black")
        self.mainmenu()
    def mainmenu(self):
        
        self.image = Image.open('menu1.png')
        self.python_image = ImageTk.PhotoImage(self.image)
        self.toile= Canvas(self, width=1500, height=700)
        self.toile.create_image(0, 0,anchor="nw", image=self.python_image)
        self.font=Font(family="helvitica",size=20)
        self.font2=Font(family="helvitica",size=15)
        self.boutonquitte=Button(self.toile,text="quitter",bg="red",width=7, height=2,command=self.destroy)
        self.boutonquitte.place(x=1400,y=650)
        self.play = Image.open("play.png")
        self.imageplays = ImageTk.PhotoImage(self.play)
        self.toile.create_image(740, 350,anchor="nw", image=self.imageplays)
        self.toile.bind("<Button-1>",self.détection)
        self.toile.pack()    
    def détection(self,evt):
        if evt.x>740 and evt.x<838:
            if evt.y>351 and evt.y<397:
                self.choisdupersonnage()
    def choisdupersonnage(self):
        self.ResetInterface()
        self.imagemenu2 = Image.open('menu2.png')
        self.python_image10 = ImageTk.PhotoImage(self.imagemenu2)
        self.toile2= Canvas(self, width=1500, height=700)
        self.toile2.create_image(0, 0,anchor="nw", image=self.python_image10)
        self.toile2.pack()
        self.imagePERSO1 = Image.open('personage 1.jfif')
        self.python_image1 = ImageTk.PhotoImage(self.imagePERSO1)
        self.MenuPersonnage1=Canvas(self,bg="grey", bd=0, width=1500, height=700)
        self.MenuPersonnage1.create_image(20, 50,anchor="nw", image=self.python_image1)
        
        self.titrepersonnage= Label(self.MenuPersonnage1,font=self.font,text="combat des guerrier",bg="grey")
        self.titrepersonnage.place(x=600,y=20) 
        self.play2 = Image.open("play.png")
        self.imageplays2 = ImageTk.PhotoImage(self.play2)
        self.toile2.create_image(700, 590,anchor="nw", image=self.imageplays2)
        self.toile2.bind("<Button-1>",self.détection2) 
        self.MenuPersonnage1.pack()
       # self.ResetInterface()

    def détection2(self,evt):
       if evt.x>703 and evt.x<797:
            if evt.y>591 and evt.y<638:
    
    def ResetInterface(self):
        
        for item in self.winfo_children():
            try:
                item.destroy()
            except TclError as e:
                pass
    
MenuPrincipal()
        
