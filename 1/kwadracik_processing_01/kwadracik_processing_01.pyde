def setup():
    size(600,600)
    point(40,100)
def draw():
    print(height, width, mouseX, mouseY, mousePressed)
    rectMode(CENTER)
    rect(300,300,300,300)
    fill(100,100,100,100)
    if mousePressed:
        rect(mouseX,mouseY,mouseX,mouseY)
        
