def setup():
    size(600,600)
    point(40,100)
    # poniższe dwie linie - lepiej żeby wykonało się raz na początku, nie co klatkę
    rectMode(CENTER)
    fill(100,100,100,100)
def draw():
    print(height, width, mouseX, mouseY, mousePressed)
    if mousePressed:
        rect(mouseX,mouseY,mouseX,mouseY)
    else: # lepiej rysować to nie co klatkę, a gdy nie rysujemy kliknięciem
        rect(height/2,width/2,height/2,width/2) #lepiej używać wartości zależnnych niż szstywnych
#1,5pkt
