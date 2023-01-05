import pygame as pg
import random

class Body:
    def __init__(self, window):
        self.x = 0
        self.y = 0
        self.dir = 0
        self.window = window
    
    def draw(self):
        pg.draw.rect(self.window, (255, 255, 255), (self.x, self.y, 10, 10))

    def move(self):
        if self.dir == 0:
            self.x += 10
        elif self.dir == 1:
            self.x -= 10
        elif self.dir == 2:
            self.y -= 10
        elif self.dir == 3:
            self.y += 10

class Food:
    def __init__(self, window):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10
        self.window = window
    
    def draw(self):
        pg.draw.rect(self.window, (200, 0, 0), (self.x, self.y, 10, 10))

    def newFood(self):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10

def refresh(window):
    window.fill((0, 0, 0))
    food.draw()
    for i in range(len(snake)):
        snake[i].draw()
        
def follow_head():
    for i in range(len(snake) -1):
        snake[len(snake) - i - 1].x = snake[len(snake) - i - 2].x
        snake[len(snake) - i - 1].y = snake[len(snake) - i - 2].y


def main():
    global snake, food
    window = pg.display.set_mode((400, 400))
    window.fill((0,0,0))
    food = Food(window)
    snake = [Body(window)]
    run = True
    while run:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                run = False
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_RIGHT or e.key == pg.K_d:
                    snake[0].dir = 0
                if e.key == pg.K_LEFT or e.key == pg.K_a:
                    snake[0].dir = 1
                if e.key == pg.K_UP or e.key == pg.K_w:
                    snake[0].dir = 2
                if e.key == pg.K_DOWN or e.key == pg.K_s:
                    snake[0].dir = 3
                
        snake[0].move()
        refresh(window)
        pg.display.update()
        pg.time.delay(200)
        if snake[0].x == food.x and snake[0].y == food.y:
            food.newFood()
            snake.append(Body(window))
        follow_head()
        if snake[0].x >= 400 :
            snake[0].x = -1
        elif snake[0].x < 0 :
            snake[0].x = 400
        if snake[0].y >= 400 :
            snake[0].y = 0
        elif snake[0].y < 0 :
            snake[0].y = 400


if __name__ == '__main__':
    main()
    pg.quit()