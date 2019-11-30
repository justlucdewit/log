from eztk import *

app = Window()
app.set_size(600, 750)
app.set_title("Lukes programming log submitter")
app.set_background(0, 0, 0)
app.set_foreground(0, 255, 0)
app.set_cursorColor(0, 255, 0)

def submit():
    title = title_input.retrieveInput()
    content = body_input.retrieveInput()
    print(title)
    print(content)

title_label = app.createLabel(20, 20, "Title: ")
title_input = app.createInput(title_label.width+title_label.x + 20, 20, 50, 1)

body_label = app.createLabel(20, title_input.y+title_input.height+20, "Content: ")
body_input = app.createInput(20, body_label.y+body_label.height+20, 70, 30)

submit_button = app.createButton(20, body_input.y+body_input.height+20, "Submit", submit)

app.launch()