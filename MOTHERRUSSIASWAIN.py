import keyboard  # using module keyboard
from playsound import playsound


stop = False
def onkeypress(event):
    global stop
    if event.name == 'r':
        stop = True

# ---------> hook event handler
keyboard.on_press(onkeypress)
# --------->

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown

        if stop:  # if key 'q' is pressed 
            print('You Pressed A Key!')
            playsound('SWAIN.mp3')
            stop = False
              # finishing the loop
    except:
        print("#######")
        



