# template for "Stopwatch: The Game"
# http://www.codeskulptor.org/#user40_uaTk86e9Vx2Pf7A.py

import simplegui
import time

# define global variables
time1 = time.time()
output = int(time1 - time.time())
a = 0
b = 0
c = 0
d = 0
stops = 0
successes = 0

print "Simple timer reflex game", '\n', "The object of the game is to", '\n', \
"press the [STOP] button on a whole second", '\n', "Score is represented as X/Y", '\n', \
"where X = successful stops and Y = total stops"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global a, b, c, d
    a = output // 600
    b = ((output / 10) % 60) // 10
    c = ((output / 10) % 60) % 10
    d = output % 10
    return

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    return

def stop():
    global stops, successes
    if not timer.is_running():
        return
    else:
        stops += 1
        if output % 10 == 0:
            successes += 1
    timer.stop()
    return

def reset():
    global a, b, c, d, stops, successes
    a = 0
    b = 0
    c = 0
    d = 0
    stops = 0
    successes = 0
    timer.stop()
    return a, b, c, d
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global output
    output += 1
    format(output)
    return

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(str(a) + ":" + str(b) + str(c) + "." + str(d), (50, 85), 40, "white")
    canvas.draw_text(str(successes) + "/" + str(stops), (135, 35), 30, "white")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 125, 60)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
start_button = frame.add_button("Start", start, 75)
stop_button = frame.add_button("Stop", stop, 75)
reset_button = frame.add_button("Reset", reset, 75)

# start frame
frame.start()
