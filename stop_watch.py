import simplegui

# define global variables

time_elapsed = 0
position = [110,110]
ms = 0
sec = 0
numTried = 0
numSucc = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global ms, sec
    
    minute = 0
    sec = 0
    ms = 0
    
    ms = t%10
    sec = (t/10) % 60
    minute = t/600
    
    if(sec >= 10):
        return str(minute) + ":" + str(sec) + ":" + str(ms)
    else:
        return str(minute) + ":0" + str(sec) + ":" + str(ms)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_event():
    global timer
    timer.start()
    
def stop_event():
    global timer, numTried, numSucc, sec, ms
    timer.stop()
    numTried += 1
    if(ms == 0 and sec%5 == 0):
        numSucc += 1
    
def reset_event():
    global timer, time_elapsed, numTried, numSucc
    timer.stop()
    time_elapsed = 0
    numTried = 0
    numSucc = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time_elapsed
    time_elapsed += 1

# define draw handler
def draw_handler(canvas):
    global time_elapsed
    canvas.draw_text(format(time_elapsed), position, 30, "White")
    canvas.draw_text(str(numSucc) + "/" + str(numTried), [250, 30], 22, "Green")
    
# create frame
frame = simplegui.create_frame("Stop Watch", 300, 200)

# register event handlers
startButton = frame.add_button("Start", start_event, 100)
stopButton = frame.add_button("Stop", stop_event, 100)
resetButton = frame.add_button("Reset", reset_event, 100)

frame.set_draw_handler(draw_handler)

timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
