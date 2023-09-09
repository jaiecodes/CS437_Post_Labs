from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
x, y = 3, 5
colours = [[255,0,0], [0,255,0], [0,0,255], [255,255,0], [255,0,255], [0,255,255]]
colour = 0

sense.set_pixel(x,y, [colours[0]])

while True:
    for event in sense.stick.get_events():
        sense.set_pixel(x, y, colours[colour])
        if event.action == 'pressed' and event.direction == 'up':
            sense.clear()
            if y > 0:
                y -= 1
        if event.action == 'pressed' and event.direction == 'down':
            sense.clear()
            if y < 7:
                y += 1
        if event.action == 'pressed' and event.direction == 'right':
            sense.clear()
            if x < 7:
                x += 1
        if event.action == 'pressed' and event.direction == 'left':
            sense.clear()
            if x > 0:
                x -= 1
        if event.action == 'pressed' and event.direction == 'middle':
            sense.clear()
            break