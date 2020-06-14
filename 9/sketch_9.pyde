def setup():
    global img
    size(700, 700)
    img = loadImage("obrazek.jpg")

def draw():
    rect(199, 199, 401, 401)
    try:
        stroke("#0000FF")
        image(img, 200, 200, 400, 400)
            
    except:
        stroke("#FF0000")
        text("blad z obrazem", 100, 25)
        
        
#polecenie 9 było szybkie i łatwe, więc pozwoliłem sobie szybko do niego przeskoczyć
