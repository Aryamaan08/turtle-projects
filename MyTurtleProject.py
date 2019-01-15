import turtle
import time
t = turtle.Turtle()
for i in range(0, 10):
	t.forward(100)
	t.left(108)
time.sleep(1)
t.clear()
for c in range(0, 20):
	t.forward(50)
	t.right(18) # The formula is 360 / no. of sides
time.sleep(1)
t.clear()
