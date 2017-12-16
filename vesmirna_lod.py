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
        self.sprite = pyglet.sprite.Sprite(image)

    def vykresli(self):
        window.clear()

        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.rotation = self.rotation
        self.sprite.draw()

    def klik(self,x, y, tlacitko, mod):
        print(tlacitko, mod)
        self.x = x
        self.y = y


    def movement(self):
        self.x = self.x + dt * self.x_speed
        self.y = self.y + dt * self.y_speed
        self.rotation = self.rotation + dt * self.rotation_speed

# def center_image(image):
#         image.anchor_x = image.width/2
#         image.anchor_y = image.height/2
# center_image(image)
# picture = pyglet.image.load('rocket.png')
# rocket = pyglet.sprite.Sprite(picture, , )

ship = Spaceship()

def tick(t):
    ship.movement()

pyglet.clock.schedule_interval(tick, 1/30)

window.push_handlers(
    on_text=ship.movement,
    on_draw=ship.vykresli,
    on_mouse_press=ship.klik,
)

pyglet.app.run()
