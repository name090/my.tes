class Title():
    #конструктор
    def __init__(self,text,x,y,vid):
        self.text = text
        self.x = x
        self.y = y
        self.vid = vid
    #методи
    def print(self):
        print("text=",self.text)
        print("vid=",self.vid)


    def hide(self):
        self.vid= False

    def hide(self):
        self.vid= True

text1 = Title("text",1,1,True)
text1.print()
text1.hide()
text1.print()

#створи два написи
#приховай другий напис