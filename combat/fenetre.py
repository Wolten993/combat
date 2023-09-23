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
        self.stastitique()
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
        
        self.imagemenu20 = Image.open('eau.png')
        self.image_eau = ImageTk.PhotoImage(self.imagemenu20)
        self.imagemenu200 = Image.open('flamme.png')
        self.image_flamme = ImageTk.PhotoImage(self.imagemenu200)
        self.imagemenu20000 = Image.open('ninjat.png')
        self.image_ninjat = ImageTk.PhotoImage(self.imagemenu20000)
        self.imagemenu2100 = Image.open('sacamoto.png')
        self.image_sacamoto = ImageTk.PhotoImage(self.imagemenu2100)
        self.imagemenu24300 = Image.open('samourail.png')
        self.image_samourail = ImageTk.PhotoImage(self.imagemenu24300)
        self.imagemenu243000 = Image.open('terre.png')
        self.image_terre = ImageTk.PhotoImage(self.imagemenu243000)
        self.imagemenu240300 = Image.open('Zelda.png')
        self.image_Zelda = ImageTk.PhotoImage(self.imagemenu240300)
        self.imagemenu24031000 = Image.open('glass.png')
        self.image_glass = ImageTk.PhotoImage(self.imagemenu24031000)
        self.imagemenu204031000 = Image.open('téléporte.png')
        self.image_téléporte = ImageTk.PhotoImage(self.imagemenu204031000)
        self.imagemenu2004031000 = Image.open('naruto.png')
        self.image_naruto = ImageTk.PhotoImage(self.imagemenu2004031000)
        

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
        self.image_flamme1=self.toile2.create_image(400, 300,anchor="center", image=self.image_flamme)
        
        self.image_flamme10=self.toile2.create_image(400, 400,anchor="center", image=self.image_sacamoto)
        self.image_flamme100=self.toile2.create_image(400, 600,anchor="center", image=self.image_ninjat)
        self.image_flamme1000=self.toile2.create_image(500, 200,anchor="center", image=self.image_eau)
        self.image_flamme1000000=self.toile2.create_image(500, 300,anchor="center", image=self.image_samourail)
        self.image_flamme11650=self.toile2.create_image(500, 400,anchor="center", image=self.image_terre)
        
        
        self.image_flamme11650=self.toile2.create_image(400, 200,anchor="center", image=self.image_Zelda)
        self.image_flamme11650=self.toile2.create_image(400, 500,anchor="center", image=self.image_glass)
        self.image_flamme11650=self.toile2.create_image(500, 500,anchor="center", image=self.image_naruto)
        self.image_flamme11650=self.toile2.create_image(500, 600,anchor="center", image=self.image_téléporte)
        


        self.image_flamme1=self.toile2.create_image(900, 300,anchor="center", image=self.image_flamme)
        
        self.image_flamme100090=self.toile2.create_image(900, 400,anchor="center", image=self.image_sacamoto)
        self.image_flamme100=self.toile2.create_image(900, 600,anchor="center", image=self.image_ninjat)
        self.image_flamme1000=self.toile2.create_image(1000, 200,anchor="center", image=self.image_eau)
        self.image_flamme1000000=self.toile2.create_image(1000, 300,anchor="center", image=self.image_samourail)
        self.image_flamme11650=self.toile2.create_image(1000, 400,anchor="center", image=self.image_terre)
        
        
        self.image_flamme1160950=self.toile2.create_image(900, 200,anchor="center", image=self.image_Zelda)
        self.image_flamme1160850=self.toile2.create_image(900, 500,anchor="center", image=self.image_glass)
        self.image_flamme116587540=self.toile2.create_image(1000, 500,anchor="center", image=self.image_naruto)
        self.image_flamme117865650=self.toile2.create_image(1000, 600,anchor="center", image=self.image_téléporte)


        self.MenuPersonnage1.pack()
       # self.ResetInterface()

    def détection2(self,evt):
        if evt.x>380 and evt.x<420:
            if evt.y>180 and evt.y<220:
                self.choix_perso1= 0
                print(self.list_stastitique[self.choix_perso1])

        if evt.x>380 and evt.x<420:
            if evt.y>280 and evt.y<320:
                self.choix_perso1= 1
                print(self.list_stastitique[self.choix_perso1])

        if evt.x>380 and evt.x<420:
            if evt.y>380 and evt.y<420:
                self.choix_perso1= 2
                print(self.list_stastitique[self.choix_perso1])

        if evt.x>380 and evt.x<420:
            if evt.y>480 and evt.y<520:
                self.choix_perso1= 3
                print(self.list_stastitique[self.choix_perso1])

        if evt.x>380 and evt.x<420:
            if evt.y>580 and evt.y<620:
                self.choix_perso1= 4
                print(self.list_stastitique[self.choix_perso1])

        if evt.x>480 and evt.x<520:
            if evt.y>180 and evt.y<220:
                self.choix_perso1= 5
                print(self.list_stastitique[self.choix_perso1])

        if evt.x>480 and evt.x<520:
            if evt.y>280 and evt.y<320:
                self.choix_perso1= 6
                print(self.list_stastitique[self.choix_perso1])
        
        if evt.x>480 and evt.x<520:
            if evt.y>380 and evt.y<420:
                self.choix_perso1= 7
                print(self.list_stastitique[self.choix_perso1])
        
        if evt.x>480 and evt.x<520:
            if evt.y>480 and evt.y<520:
                self.choix_perso1= 8
                print(self.list_stastitique[self.choix_perso1])
        
        if evt.x>480 and evt.x<520:
            if evt.y>580 and evt.y<620:
                self.choix_perso1= 9
                print(self.list_stastitique[self.choix_perso1])
        
        if evt.x>100 and evt.x<209:
            if evt.y>192 and evt.y<298:
                self.mainmenu()
        if evt.x>703 and evt.x<797:
            if evt.y>591 and evt.y<638:
                
                self.déplacement()
    
    
        if evt.x>880 and evt.x<920:
            if evt.y>180 and evt.y<220:
                self.choix_perso2= 0
                print(self.list_stastitique[self.choix_perso2])

        if evt.x>880 and evt.x<920:
            if evt.y>280 and evt.y<320:
                self.choix_perso2= 1
                print(self.list_stastitique[self.choix_perso2])

        if evt.x>880 and evt.x<920:
            if evt.y>380 and evt.y<420:
                self.choix_perso2= 2
                print(self.list_stastitique[self.choix_perso2])

        if evt.x>880 and evt.x<920:
            if evt.y>480 and evt.y<520:
                self.choix_perso2= 3
                print(self.list_stastitique[self.choix_perso2])

        if evt.x>880 and evt.x<920:
            if evt.y>580 and evt.y<620:
                self.choix_perso2= 4
                print(self.list_stastitique[self.choix_perso2])

        if evt.x>980 and evt.x<1020:
            if evt.y>180 and evt.y<220:
                self.choix_perso2= 5
                print(self.list_stastitique[self.choix_perso2])

        if evt.x>980 and evt.x<1020:
            if evt.y>280 and evt.y<320:
                self.choix_perso2= 6
                print(self.list_stastitique[self.choix_perso2])
        
        if evt.x>980 and evt.x<1020:
            if evt.y>380 and evt.y<420:
                self.choix_perso2= 7
                print(self.list_stastitique[self.choix_perso2])
        
        if evt.x>980 and evt.x<1020:
            if evt.y>480 and evt.y<520:
                self.choix_perso2= 8
                print(self.list_stastitique[self.choix_perso2])
        
        if evt.x>980 and evt.x<1020:
            if evt.y>580 and evt.y<620:
                self.choix_perso2= 9
                print(self.list_stastitique[self.choix_perso2])
        
        
                
                self.déplacement()
    
    
    
    
    
    
    
    
    
    
    def stastitique(self):
        fichier =open("statistique.txt","r")
        self.list_stastitique =[]
        for i in range (10):
            self.list_stastitique.append(fichier.readline().split())
        print(self.list_stastitique)

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
        self.cote =0
       
        self.nomperso =StringVar()
        self.nomperso.set(self.list_stastitique[self.choix_perso1][1])
        self.point_de_vie=self.toile3.create_rectangle(20,30,220,50, fill="green")
        self.nom_du_perso=Label(self.toile3,textvariable=self.nomperso)
        self.nom_du_perso.place(x=20,y=10)
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
        self.cote= 1
        self.animation_droit()
        self.after (2000,self.droitestop)
    def droitestop(self):
        self.vitesseX= 0

    def gauche(self,evt):
        self.vitesseX= -0.3
        self.cote= 0
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
            if self.cote ==1:
                self.x= self.toile3.coords(self.imageperso1)[0]+70
            else:
                self.x= self.toile3.coords(self.imageperso1)[0]-70
            self.y= self.toile3.coords(self.imageperso1)[1]-70
            if self.cote ==1:
                self.vitessebouledefeu= 0.2
            else:
                self.vitessebouledefeu= -0.2
            self.imagebouldefeu= self.toile3.create_image(self.x, self.y, anchor="w", image=self.perso110)
            self.deplacementbouledefeu()
            self.after(2000, self.boul_de_feu_stop)


    def boul_de_feu_stop(self):
        self.couldownbouledefeu=0
        self.vitessebouledefeu=0
        self.toile3.delete(self.imagebouldefeu)
    def deplacementbouledefeu(self):
        if self.vitessebouledefeu!= 0:
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
        
