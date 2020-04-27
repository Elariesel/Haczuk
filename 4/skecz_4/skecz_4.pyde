add_library('pdf')

def setup():
    global img1, img2, img3
    size(400, 520)
    img1 = loadImage("dowod.jpg")
    img2 = loadImage("mlg.png")
    img3 = loadImage("wasy.png")
    beginRecord(PDF, 'outpdfik.pdf')
        
def draw():
    global img1, img2, img3
    image(img1, 0, 0, width, height)
    
    if keyPressed:
        if key == CODED: # wartoby napisać dla użytkownika, że tak to działa
            if keyCode == LEFT:
                image(img2, 0, height/2-130, width, height/2)
            if keyCode == RIGHT:
                image(img3, width-260, height/2+30, width/3, height/3)
            if keyCode == UP:
                image(img2, 0, height/2-130, width, height/2)
                image(img3, width-260, height/2+30, width/3, height/3)
                
def mousePressed(): # lepiej to uwzględnić wyżej w kodzie draw, bo obecnie zanim się nie kliknie, będzie zapisywało wklatki jako warstwy... im dłużej program odpalony a nie kliknięto tym cięższy będzie pdfik
    endRecord()
    exit()
    
# 1,75p
