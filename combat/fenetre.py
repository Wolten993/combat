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
        self.titre= Label(self.toile,font=self.font,text="combat des guerrier",bg="grey")
        self.titre.place(x=600,y=20)
        self.boutonquitte=Button(self.toile,text="quitter",bg="red",width=7, height=2,command=self.destroy)
        self.boutonquitte.place(x=1400,y=650)
        self.toile.pack()
        
       # self.ResetInterface()
    def ResetInterface(self):
        
        for item in self.winfo_children():
            try:
                item.destroy()
            except TclError as e:
                pass
    
MenuPrincipal()
        