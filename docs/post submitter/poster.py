from eztk import *

app = Window()
app.set_size(600, 750)
app.set_title("Lukes programming log submitter")
app.set_background(0, 0, 0)

app.createLabel()
titleInp = app.createInput(20, 20, 50, 1)

app.launch()