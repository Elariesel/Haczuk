def setup():
    size(400, 400)
    textSize(80)
    
    
def draw():
    clear()
    
    fill(255)
    if ((mouseX < 120) and (mouseY < 270) and
       (mouseX > 30) and (mouseY > 180)):
        fill("#ff00ff")
    else:
        fill(255)
    if keyPressed:
        if key == CODED:
            if keyCode == LEFT:
                fill("#ff00ff")
            if keyCode == RIGHT:
                fill(255)
    text('F', 50, 200)
    
    fill(255)
    if keyPressed:
        if key == "h":
            fill("#40ff00")
    if keyPressed:
        if key == CODED:
            if keyCode == RIGHT:
                fill("#40ff00")
            if keyCode == LEFT:
                fill(255)
    text('H', 300, 200)
    
    s = createShape()
    s.beginShape()
    s.fill(0, 0, 255)
    s.stroke(255, 0, 0)
    s.vertex(25, 160)
    s.vertex(200, 13)
    s.vertex(375, 160)
    s.endShape(CLOSE)
    shape(s, 10, 190)
