add_library('pdf')

def setup():
    global img1, img2, img3
    size(400, 520)
    img1 = loadImage("zdjecie.jpg")
    img2 = loadImage("mlg.png")
    img3 = loadImage("wasy.png")
    beginRecord(PDF, 'outpdfik.pdf')
        
def draw():
    global img1, img2, img3
    image(img1, 0, 0, width, height)
    
    if keyPressed:
        if key == CODED:
            if keyCode == LEFT:
                image(img2, 0, height/2-130, width, height/2)
            if keyCode == RIGHT:
                image(img3, width-260, height/2+30, width/3, height/3)
            if keyCode == UP:
                image(img2, 0, height/2-130, width, height/2)
                image(img3, width-260, height/2+30, width/3, height/3)
                
def mousePressed():
    endRecord()
    exit()
