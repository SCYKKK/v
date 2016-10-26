
import random
import json
import os

from pico2d import *


import game_framework
import title_state


name = "MainState"

Boy = None
Back = None
font = None


running = None

class Back:
    def __init__(self):
        self.image = load_image('background_1-1.png')

    def draw(self):
        self.image.draw(400, 300)

class Boy:

    image = None

    LEFT_CRAWL, RIGHT_CRAWL, LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND, = 0, 1, 2, 3, 4, 5




    def handle_left_run(self):
        self.x -= 10
        self.run_frames += 0.5
        if self.x < 0:
            self.x = 0
        if self.run_frames == 500:
            self.state = self.LEFT_STAND
            self.stand_frames = 0


    def handle_left_stand(self):
        self.stand_frames += 0.5
        if self.stand_frames == 100000:
            self.state = self.LEFT_RUN
            self.run_frames = 0



    def handle_right_run(self):
        self.x += 10
        self.run_frames += 0.5
        if self.x > 800:
            self.x = 800
        if self.run_frames == 500:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0


    def handle_right_stand(self):
        self.stand_frames += 0.5
        if self.stand_frames == 100000:
            self.state = self.RIGHT_RUN
            self.run_frames = 0

    def handle_left_crawl(self):
        self.crawl_frames += 0.5
        if self.crawl_frames == 100000:
            self.state = self.LEFT_RUN
        elif self.crawl_frames < 100000:
            self.state = self.LEFT_CRAWL
        self.x += 0


    def handle_right_crawl(self):
        self.crawl_frames += 0.5
        if self.crawl_frames == 100000:
            self.state = self.RIGHT_RUN
        elif self.crawl_frames < 100000:
            self.state = self.RIGHT_CRAWL
        self.x += 0

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand,
        LEFT_CRAWL: handle_left_crawl,
        RIGHT_CRAWL: handle_right_crawl
    }






    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = random.randint(0, 8)
        self.run_frames = 0
        self.stand_frames = 0
        self.crawl_frames = 0
        self.state = self.RIGHT_STAND
        if Boy.image == None:
            Boy.image = load_image('animation_sheet2.png')



    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)
        delay(0.05)


    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)


def enter():
    global boy, back
    boy = Boy()
    back = Back()


def exit():
    global boy, back
    del(boy)
    del(back)


def pause():
    pass


def resume():
    pass



def handle_events():
    global running
    global boy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_RIGHT:
                boy.state = boy.RIGHT_RUN
            elif event.key == SDLK_LEFT:
                boy.state = boy.LEFT_RUN
            elif event.key == SDLK_DOWN:
                if boy.state == boy.RIGHT_STAND:
                    boy.state = boy.RIGHT_CRAWL
                elif boy.state == boy.LEFT_STAND:
                    boy.state = boy.LEFT_CRAWL

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                boy.state = boy.RIGHT_STAND
            elif event.key == SDLK_LEFT:
                boy.state = boy.LEFT_STAND
            elif event.key == SDLK_DOWN:
                if boy.state == boy.RIGHT_CRAWL:
                    boy.state = boy.RIGHT_STAND
                elif boy.state == boy.LEFT_CRAWL:
                    boy.state = boy.LEFT_STAND



def update():
    boy.update()


def draw():
    clear_canvas()
    back.draw()
    boy.draw()
    update_canvas()


def main():

    open_canvas()


    global back

    back = Back()

    global boy
    boy = Boy()

    global running
    running = True


    while running:
        handle_events()

        boy.update()

        clear_canvas()
        back.draw()
        boy.draw()
        update_canvas()

        delay(0.1)

    close_canvas()



if __name__ == '__main__':
    main()