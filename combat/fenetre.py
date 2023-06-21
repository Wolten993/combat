from tkinter import *
from tkinter.font import Font

class MenuPrincipal(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.initinterface()
        self.mainloop()

    
    def initinterface(self):
        self.geometry("1500x700+10+10")
        self.title("Rund1")
        self.resizable(width=False, height=False)
        self.configure(bg="black")
        self.mainmenu()
    def mainmenu(self):
        
        self.toile= Canvas(self,width=1500, height=700, bg="grey", bd=0)
        self.font=Font(family="helvitica",size=20)
        self.font2=Font(family="helvitica",size=15)
        self.titre= Label(self.toile,font=self.font,text="combat des guerrier",bg="grey")
        self.titre.place(x=600,y=20)
        self.boutonquitte=Button(self.toile,text="quitter",bg="red",width=7, height=2,command=self.destroy)
        self.boutonquitte.place(x=1400,y=650)
        self.boutonplays=Button(self.toile,text="play",bg="red",width=30, height=4,font=self.font2,command=self.choisdupersonnage)
        self.boutonplays.place(x=600,y=200)
        self.toile.pack()
        
    def choisdupersonnage(self):
        self.ResetInterface()
        self.MenuPersonnage=Canvas(self,width=1500, height=700, bg="grey", bd=0)
        self.MenuPersonnage.pack()
        self.titrepersonnage= Label(self.MenuPersonnage,font=self.font,text="combat des guerrier",bg="grey")
        self.titrepersonnage.place(x=600,y=20) 
        self.boutonplays2=Button(self.MenuPersonnage,text="play",bg="red",width=30, height=4,font=self.font2)
        self.boutonplays2.place(x=600,y=500)
       # self.ResetInterface()
    def ResetInterface(self):
        
        for item in self.winfo_children():
            try:
                item.destroy()
            except TclError as e:
                pass
    
MenuPrincipal()
        
