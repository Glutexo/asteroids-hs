import pyglet, math
window = pyglet.window.Window()

objects=[]
image = pyglet.image.load('rocket.png')
class Spaceship:

    def __init__(self):
        self.x = 150
        self.y = 150
        self.x_speed= 5
        self.y_speed = 5
        self.rotation = 0
        self.rotation_speed = 10
        self.sprite = pyglet.sprite.Sprite(image, self.x, self.y, self.rotation)
        sprite1 = self.sprite

    def vykresli(self):
        self.vykreslit = window.clear()
        sprite.draw()

    def klik(self,x, y, tlacitko, mod):
        print(tlacitko, mod)
        self.x = x
        self.y = y


    def movement(self):
        self.x = self.x + dt * self.x_speed
        self.y = self.y + dt * self.y_speed
        self.rotation = self.rotation + dt * self.rotation_speed
        def tick(t):
            movement()
        pyglet.clock.schedule_interval(tick, 1/30)

    window.push_handlers(
        on_text=movement,
        on_draw=vykresli,
        on_mouse_press=klik,
    )
# def center_image(image):
#         image.anchor_x = image.width/2
#         image.anchor_y = image.height/2
# center_image(image)
# picture = pyglet.image.load('rocket.png')
# rocket = pyglet.sprite.Sprite(picture, , )
ship = Spaceship()
pyglet.app.run()
