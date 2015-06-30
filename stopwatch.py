#CopyRight PavanSuta
#June 28th 2015

# define global variables
import simplegui
interval = 100
count = 0
hit_counts = 0 # Milisecond value(D value)
stop_counts = 0 # Count number of times stopped.
win_counts = 0 #count the sucess rate.



# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(value):
    global hit_counts
    ValueA = value//600  # logic to get minutes A
    seconds = value//10 # Logic to get seconds 
    ValueBC = seconds%60 #Logic to get BC
    ValueB =  ValueBC//10 #Logic to get B
    ValueC = ValueBC%10 #Logic to get C
    ValueD = value%10 #Logic to get D
    hit_counts = ValueD
    
    return str(ValueA) + ":" + str(ValueB) + str(ValueC) + "." + str(ValueD)
    
    
    



# define event handler for timer with 0.1 sec interval
def time_handler():
    global count
    count = count + 1
    



# define draw handler
def draw(canvas):
    global count
    global stop_counts
    global win_counts
    text = format(count)
    no_of_stop = str(stop_counts)
    no_of_win = str(win_counts)
    canvas.draw_text(text, (80, 100), 24, 'Red')
    canvas.draw_text("Chances : ", (20, 25), 24, 'Red')
    canvas.draw_text(no_of_stop, (115, 26), 24, 'Red')
    canvas.draw_text("Won : ", (20, 55), 24, 'Red')
    canvas.draw_text(no_of_win, (80, 56), 24, 'Red')
    

# define start handler    
def start_handler():
    timer.start()

# define stop handler    
def stop_handler():
    global hit_counts
    global stop_counts
    global win_counts
    timer.stop()
    stop_counts = stop_counts + 1 
    if hit_counts == 0:
        win_counts = win_counts + 1
    #else: win_counts = win_counts - 1    
        
        
    
# define reset handler        
def reset_handler():
    global count
    count = 0
    timer.stop()
     
    
    
# start frame
frame = simplegui.create_frame("Stop Watch", 200, 200) 
frame.set_draw_handler(draw)

# register event handlers
timer = simplegui.create_timer(interval, time_handler) #Interval of timer 0.1 sec
Startbutton = frame.add_button('Start', start_handler, 100) # To start the timer
Stopbutton = frame.add_button('Stop', stop_handler, 100) # To stop the timer
Resetbutton = frame.add_button('Reset', reset_handler, 100)#To reset the timer






frame.start()

