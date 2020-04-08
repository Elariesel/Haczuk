def setup():
    size(600,600)
    global x, y, i, lista_k, x_kierunek, y_kierunek
   
    x = 1
    y = height / 2
    i = 0
    x_kierunek = 1
    y_kierunek = 1
    lista_k = ["#00FF00", "#FF0000", "#0000FF"]
 
def draw():
    global x, y, i, lista_k, x_kierunek, y_kierunek
    szer_prost = width/10
    wys_prost = height/10
    rect(x, y, szer_prost, wys_prost)
   
    fill(255, 0, 0)
    textSize(30)
    text("WYJSCIE", width - 200, height - 50)
   
    x += x_kierunek
    y += y_kierunek
    fill(lista_k[i])
   
    if x == 0 or x == width - szer_prost:
        x_kierunek = x_kierunek * -1
        i = (i + 1) % 3
    if y == 0 or y == height - wys_prost:
        y_kierunek = y_kierunek * -1
        i = (i + 1) % 3
       
def mousePressed():
    if (mouseX >= width - 200 and mouseX <= width - 200 + 120) and (mouseY >= height - 50 - 30 and mouseY <= height - 50):
        exit()
        
# właściwie nic dodać nic ująć, zgrabnie napisane
# 2 pkt
