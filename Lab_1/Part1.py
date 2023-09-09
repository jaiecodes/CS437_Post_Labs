from sense_hat import SenseHat
sense = SenseHat()

x, y = 3, 5
colours = [[255,0,0], [0,255,0], [0,0,255], [255,255,0], [255,0,255], [0,255,255]]
colour = 0

sense.set_pixel(x,y, [colours[0]])

while True:
    for event in sense.stick.get_events():
        sense.set_pixel(x, y, colours[colour])
        if event.action == 'pressed' and event.direction == 'up':
            sense.set_pixel(x,y,[0,0,0])
            if y > 0:
                y -= 1
        if event.action == 'pressed' and event.direction == 'down':
            sense.set_pixel(x,y,[0,0,0])
            if y < 7:
                y += 1
        if event.action == 'pressed' and event.direction == 'right':
            sense.set_pixel(x,y,[0,0,0])
            if x < 7:
                x += 1
        if event.action == 'pressed' and event.direction == 'left':
            sense.set_pixel(x,y,[0,0,0])
            if x > 0:
                x -= 1
        if event.action == 'pressed' and event.direction == 'middle':
            sense.clear()
            break