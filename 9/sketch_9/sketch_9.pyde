def setup():
    global img
    size(700, 700)
    img = loadImage("obrazek.jpg")
    noFill()

def draw():
    try:
        image(img, 200, 200, 400, 400) # tylko to chcemy testować pod kątem wystąpienia błędu
            
    except:
        stroke("#FF0000")
        text("blad z obrazem", 100, 25)
    else:
        stroke("#0000FF")
    finally:
        rect(199, 199, 401, 401)

#1,5pkt
