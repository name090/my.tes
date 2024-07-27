class Widget():
    #властивості класа (в конструкторі)
    def __init__(self, text ,x ,y):
        self.text = text
        self.x = x
        self.y = y
    #методи
    def info(self):
        print(self.text)
        

class Button(Widget):
    #доповнені властивості класа (в конструкторі)
    def __init__(self, text ,x, y, is_clicked):
        super().__init__(text ,x, y)
        self.is_clicked = is_clicked
    #нові методи
    def click(self):
        self.is_clicked = True
        print("ви зариістровані")

#створи екземпляр класа Button
button = Button("Натисни",1,1, False)
#якщо на питання «Хочете зареєструватися?» користувач відповів «так», то застосуйте метод click
answer = input("Хочете зареєструватися?")
if answer == 'так':
    button.click()

button.info()