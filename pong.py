"""
An empty Arcade project
"""
import arcade

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Pong :D"
WINDOW_BACKGROUND_COLOR = arcade.color.BLACK

class bats():
    def __init__(self, x, y, width, height):
        """ constructor. """
        self.x              = x
        self.y              = y
        self.deltay         = 0
        self.color          = arcade.color.WHITE
        self.width          = 10
        self.height         = 100
        self.movementspeed  = 10
        self.score          = 0 

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)

    def update(self):
        self.movement()
        self.nietdoorschermhoogtegaan()

    def movement(self):
        self.y += self.deltay

    def nietdoorschermhoogtegaan(self):
        if self.y >= WINDOW_HEIGHT - self.height//2:
            self.deltay = 0
            self.y = WINDOW_HEIGHT - self.height//2
        
        if self.y <= 0 + self.height//2:
            self.deltay = 0
            self.y = 0 + self.height//2
        
class Balletje():
    def __init__(self, x, y, radius):
        """ Constructor. """
        self.x          = x
        self.y          = y
        self.color      = arcade.color.GREEN_YELLOW
        self.deltax     = 6
        self.deltay     = 6
        self.radius     = radius

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

    def update(self, bats_list):
        self.score(bats_list)
        self.checkCol(bats_list)
        self.stuiter()
        self.movement()
    
    def checkCol(self, bats_list):
        for bat in bats_list:
            if self.x + self.radius > bat.x and self.x - self.radius < bat.x and self.y + self.radius < bat.y + bat.height and self.y - self.radius > bat.y - bat.height:
                self.deltax *= -1.05

    def stuiter(self):
        if self.y - self.radius <= 0 or self.y + self.radius >= WINDOW_HEIGHT:
            self.deltay *= -1

    def movement(self):
        self.x += self.deltax
        self.y += self.deltay
    
    def score(self, bats_list):
        if self.x - self.radius >= WINDOW_WIDTH:
            bats_list[0].score += 1
            self.reset()
            self.deltax *= -1
        elif self.x + self.radius <= 0:
            bats_list[1].score += 1
            self.reset()

    def reset(self):
        self.x = WINDOW_WIDTH//2
        self.y = WINDOW_HEIGHT//2
        self.deltax = 6

class MyGame(arcade.Window):
    """ An Arcade game. """

    def __init__(self, width, height, title):
        """ Constructor. """
        super().__init__(width, height, title)
        arcade.set_background_color(WINDOW_BACKGROUND_COLOR)
        self.ball_list = []
        self.ball_list.append(Balletje(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, 20))

        self.bats_list = []
        self.bats_list.append(bats(WINDOW_WIDTH - 790, WINDOW_HEIGHT // 2, self.width, self.height))
        self.bats_list.append(bats(WINDOW_WIDTH - 10, WINDOW_HEIGHT // 2, self.width, self.height))

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        for ball in self.ball_list:
            ball.draw()
        
        for bat in self.bats_list:
            bat.draw()
        
        arcade.draw_text(str(self.bats_list[0].score), WINDOW_WIDTH//2 - 40, WINDOW_HEIGHT - 80, arcade.color.RED, 50)
        arcade.draw_text(str(self.bats_list[1].score), WINDOW_WIDTH//2 + 40, WINDOW_HEIGHT - 80, arcade.color.RED, 50)
        arcade.draw_text('-', WINDOW_WIDTH//2 + 7.5, WINDOW_HEIGHT - 80, arcade.color.RED, 50)

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second. """
        for ball in self.ball_list:
            ball.update(self.bats_list)

        for bat in self.bats_list:
            bat.update()         

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.bats_list[0].deltay = self.bats_list[0].movementspeed
        elif key == arcade.key.S:
            self.bats_list[0].deltay = -self.bats_list[0].movementspeed

        if key == arcade.key.UP:
            self.bats_list[1].deltay = self.bats_list[1].movementspeed
        elif key == arcade.key.DOWN:
            self.bats_list[1].deltay = -self.bats_list[1].movementspeed

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
             self.bats_list[1].deltay = 0
        if key == arcade.key.W or key == arcade.key.S:
            self.bats_list[0].deltay = 0

def main():
    """ Create an instance of our game window and start the Arcade game loop. """
    window = MyGame(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    arcade.run()
if __name__ == "__main__":
    main()
