class Figure(object):
    def __init__(self, posX, posY, figureColor, figureSize, dir):
        self.posX = posX
        self.posY = posY
        self.figureColor = figureColor
        self.figureSize = figureSize
        self.moveX = 1
        self.moveY = 1
        self.direction(dir)
        
    def direction(self, d):
        if d == 1:
            self.moveY *= -1
        elif d == 2:
            self.moveX *= -1;
        elif d == 3:
            self.moveX *= -1; self.moveY *= -1

    def move(self):
        self.posX += self.moveX
        self.posY += self.moveY

class Square(Figure):
    def __init__(self, posX, posY, figureColor, figureSize, dir):
        super(Square, self).__init__(posX, posY, figureColor, figureSize, dir)
        fill(figureColor)
        rect(posX, posY, figureSize, figureSize)
    
    def drawFigure(self):
        fill(self.figureColor)
        rect(self.posX, self.posY, self.figureSize, self.figureSize)

class Circle(Figure):
    def __init__(self, posX, posY, figureColor, figureSize, dir):
        super(Circle, self).__init__(posX, posY, figureColor, figureSize, dir)
        fill(figureColor)
        ellipse(posX, posY, figureSize, figureSize)

    def drawFigure(self):
        fill(self.figureColor)
        ellipse(self.posX, self.posY, self.figureSize, self.figureSize)

def setup():
    global windowX, windowY
    windowX = 600
    windowY = 600
    size(600, 600)
    background(255)
    noStroke()
    
    global figureList, figureColor, colorArr
    figureList = []
    figureColor = 0
    colorArr = ["#CC0033", "#FF66FF", "#6600FF", "#00FF66"]
    
def mouseClicked():
    global figureList, figureColor
    for i in range(4):
        if figureColor % 2 == 0:
            figureList.append(Square(mouseX, mouseY, colorArr[(figureColor + i) % 4], 20, i))
        else:
            figureList.append(Circle(mouseX, mouseY, colorArr[(figureColor + i) % 4], 20, i))
    figureColor += 1

def draw():
    background(255)
    global figureList
    for i in figureList:
        i.move()
        i.drawFigure()
        if i.posX <= 0 or i.posX >= windowX or i.posY <= 0 or i.posY >= windowY:
            figureList.remove(i)
            
#Wreszcie odzyskałem laptopa i zabieram się za nadrabianie zaległości.
#Mój kod do zadania 5 już miał dziedziczenie, więc użyję go jeszcze raz - mniej czasu zajmie Pani sprawdzanie ;)
#zmieniłem jedynie na szybko kolory, aby nie był to dokładnie ten sam
#dziękuję za cierpliwość w kwestii mojego braku sprzętu

#2pkt
