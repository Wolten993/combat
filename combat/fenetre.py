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
        self.ResetInterface()
        self.image = Image.open('menu1.png')
        self.python_image = ImageTk.PhotoImage(self.image)
        self.toile= Canvas(self, width=1500, height=700)
        self.toile.create_image(0, 0,anchor="nw", image=self.python_image)
        self.font=Font(family="helvitica",size=20)
        self.font2=Font(family="helvitica",size=15)
        self.quitte = Image.open("quitte.jfif")
        self.imagequite = ImageTk.PhotoImage(self.quitte)
        self.toile.create_image(840, 450,anchor="nw", image=self.imagequite)
        self.play = Image.open("play.png")
        self.imageplays = ImageTk.PhotoImage(self.play)
        self.toile.create_image(740, 350,anchor="nw", image=self.imageplays)
        self.toile.bind("<Button-1>",self.détection)
        self.toile.pack()    
    def détection(self,evt):
        if evt.x>839 and evt.x<1020:
            if evt.y>449 and evt.y<628:
                self.quit()
        
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
        self.retour = Image.open("retour.jfif")
        self.imageretour = ImageTk.PhotoImage(self.retour)
        self.toile2.create_image(100, 190,anchor="nw", image=self.imageretour)  
        self.play2 = Image.open("play.png")
        self.imageplays2 = ImageTk.PhotoImage(self.play2)
        self.toile2.create_image(700, 590,anchor="nw", image=self.imageplays2)
        self.toile2.bind("<Button-1>",self.détection2) 
        self.MenuPersonnage1.pack()
       # self.ResetInterface()

    def détection2(self,evt):
        if evt.x>100 and evt.x<209:
            if evt.y>192 and evt.y<298:
                self.mainmenu()
        if evt.x>703 and evt.x<797:
            if evt.y>591 and evt.y<638:
                
                self.déplacement()
    


    def déplacement(self):
        print("rrrrrrrrrrrrrrrrrrrrrr")
        self.ResetInterface()
        self.toile3= Canvas(self, width=1500, height=700, bg="red")
        self.toile3.pack()
        self.x =0
        self.y =0
        self.vitesseX =0
        self.vitesseY =0
        self.image()
        
    def image(self):
        self.persofeu = Image.open("play.png")
        self.perso1 = ImageTk.PhotoImage(self.persofeu)
        self.imageperso1 =self.toile3.create_image(0, 0,anchor="nw", image=self.perso1)

    def ResetInterface(self):
        
        for item in self.winfo_children():
            try:
                item.destroy()
            except TclError as e:
                pass

      
MenuPrincipal()
        
