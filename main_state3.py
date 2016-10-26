from pico2d import *

def handle_events():

    global running
    global x

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x = x + 15
            elif event.key == SDLK_LEFT:
                x = x - 15
            elif event.key == SDLK_ESCAPE:
                running = False





open_canvas()
grass = load_image('background_1-1.png')
character = load_image('boy_running.png')

running = True
x = 0
frame = 0
while (x < 800 and running):
    clear_canvas()
    grass.draw(400, 300)
    character.clip_draw(frame * 63, 0, 64, 75, x, 90)
    update_canvas()
    frame = (frame + 1) % 6

    delay(0.03)
    handle_events()

close_canvas()

