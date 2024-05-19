# Drawing Olympic Symbol

from ezgraphics import GraphicsWindow

new_width  = 500
new_height = 500

window = GraphicsWindow(new_width, new_height)
canvas = window.canvas()

canvas.setLineWidth(5)
canvas.setOutline("blue")
canvas.drawOval(75, 150, 100, 100)

canvas.setLineWidth(5)
canvas.setOutline("black")
canvas.drawOval(179, 150, 100, 100)

canvas.setLineWidth(5)
canvas.setOutline("red")
canvas.drawOval(283, 150, 100, 100)

canvas.setLineWidth(5)
canvas.setOutline("yellow")
canvas.drawOval(120, 200, 100, 100)

canvas.setLineWidth(5)
canvas.setOutline("green")
canvas.drawOval(224, 200, 100, 100)

window.wait()
