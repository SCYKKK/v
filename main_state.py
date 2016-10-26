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

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3



    def handle_left_run(self):
        self.x -= 1
        self.run_frames += 0.5
        if self.x < 0:
            self.state = self.RIGHT_RUN
            self.x = 0
        if self.run_frames == 500:
            self.state = self.LEFT_STAND
            self.stand_frames = 0


    def handle_left_stand(self):
        self.stand_frames += 0.5
        if self.stand_frames == 100:
            self.state = self.LEFT_RUN
            self.run_frames = 0



    def handle_right_run(self):
        self.x += 1
        self.run_frames += 0.5
        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800
        if self.run_frames == 500:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0


    def handle_right_stand(self):
        self.stand_frames += 0.5
        if self.stand_frames == 100:
            self.state = self.RIGHT_RUN
            self.run_frames = 0


    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand
    }






    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 5)
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.RIGHT_RUN
        if Boy.image == None:
            Boy.image = load_image('animation_sheet2.png')



    def update(self):
        self.frame = (self.frame + 1) % 6
        self.handle_state[self.state](self)


    def draw(self):
        self.image.clip_draw(self.frame * 65, self.state * 75, 64, 75, self.x, self.y)


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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            boy.stand_frames = 0
            boy.run_frames = 0
            if boy.state == Boy.LEFT_RUN:
                boy.state = Boy.RIGHT_RUN
            elif boy.state == Boy.RIGHT_RUN:
                boy. state = Boy.LEFT_RUN
            elif boy.state == Boy.LEFT_STAND:
                boy.state = Boy.LEFT_RUN
            elif boy.state == Boy.RIGHT_STAND:
                boy.state = Boy.RIGHT_RUN


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

        delay(0.04)

    close_canvas()



if __name__ == '__main__':
    main()


##############################################################

