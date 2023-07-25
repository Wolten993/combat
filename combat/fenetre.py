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
        self.couldownbouledefeu = 0
        self.x =50
        self.y =10
        self.vitesseX =0
        self.vitesseY =0
        self.verification_saut =0
        self.imageperso()
        
    def imageperso(self):
        self.persofeu = Image.open("flamedefence.png")
        self.perso1 = ImageTk.PhotoImage(self.persofeu)
        self.persofeu1 = Image.open("droit.png")
        self.perso11 = ImageTk.PhotoImage(self.persofeu1)
        self.persofeu10 = Image.open("boulfeu.jfif")
        self.perso110 = ImageTk.PhotoImage(self.persofeu10)
        self.imageperso1 =self.toile3.create_image(self.x, self.y, anchor="s", image=self.perso1)
        self.graviter()
        self.bind("<d>", self.droite)
        self.bind("<q>", self.gauche)
        self.bind("<z>", self.saut)
        self.bind("<g>",self.boul_de_feu)
    def graviter(self):
        if self.verification_saut==0:
            if self.toile3.coords(self.imageperso1)[1]>700:
                if self.verification_saut==0:
                    self.vitesseY= (-0.1)
            else:
                if self.verification_saut==0:
                    self.vitesseY= 0.1
        self.after(1,self.mouvement)
    def mouvement(self):
        if self.verification_saut==0:
            self.toile3.move(self.imageperso1,self.vitesseX,self.vitesseY)
            self.after(1,self.graviter)
        else:
            self.toile3.move(self.imageperso1,self.vitesseX,self.vitesseY)
            self.after(1,self.mouvement)
    def droite(self,evt):
        self.vitesseX= 0.3
        self.animation_droit()
        self.after (2000,self.droitestop)
    def droitestop(self):
        self.vitesseX= 0

    def gauche(self,evt):
        self.vitesseX= -0.3
        self.animation_gauche()
        self.after (2000,self.gauchestop)
    def gauchestop(self):
        self.vitesseX= 0

    def saut(self,evt):
        self.verification_saut= 1
        self.vitesseY= -0.3
        self.after (200,self.sautstop)
    def sautstop(self):
        self.verification_saut= 0
        self.vitesseY= 0
    


    def boul_de_feu(self,evt):
        if self.couldownbouledefeu ==0:
            self.couldownbouledefeu= 1
            self.x= self.toile3.coords(self.imageperso1)[0]+70
            self.y= self.toile3.coords(self.imageperso1)[1]-70
            self.vitessebouledefeu= 0.2
            self.imagebouldefeu= self.toile3.create_image(self.x, self.y, anchor="w", image=self.perso110)
            self.deplacementbouledefeu()
            self.after(2000, self.boul_de_feu_stop)


    def boul_de_feu_stop(self):
        self.couldownbouledefeu=0
        self.vitessebouledefeu=0
        self.toile3.delete(self.imagebouldefeu)
    def deplacementbouledefeu(self):
        if self.k!= 0:
            self.toile3.move(self.imagebouldefeu,self.vitessebouledefeu,0)
            self.after(1, self.deplacementbouledefeu)




    def animation_droit(self):
        self.x= self.toile3.coords(self.imageperso1)[0]
        self.y= self.toile3.coords(self.imageperso1)[1]
        self.toile3.delete(self.imageperso1)
        self.imageperso1 =self.toile3.create_image(self.x, self.y, anchor="s", image=self.perso11)
    
    def animation_gauche(self):
        self.x= self.toile3.coords(self.imageperso1)[0]
        self.y= self.toile3.coords(self.imageperso1)[1]
        self.toile3.delete(self.imageperso1)
        self.imageperso1 =self.toile3.create_image(self.x, self.y, anchor="s", image=self.perso1)
    
    
    def ResetInterface(self):
        
        for item in self.winfo_children():
            try:
                item.destroy()
            except TclError as e:
                pass

      
MenuPrincipal()
        
