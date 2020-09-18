import keyboard, time

#change this!!!
NUMBER_OF_WEEKS = 24

#change this if you want to start at a week which isn't 1
week = 1


time.sleep(5)
while week <= NUMBER_OF_WEEKS:
    keyboard.press_and_release('ctrl+l')
    time.sleep(0.1) #wait for browser to respond
    keyboard.write('https://artofproblemsolving.com/class/1809-maa-amc10/homework/' + str(week))#go to homework page
    keyboard.press_and_release('enter')
    time.sleep(5) #wait for page to fully load (5 seconds)
    keyboard.press_and_release('ctrl+p')
    time.sleep(1) #wait for printing menu to pop up (1 second)
    keyboard.press_and_release('enter')
    time.sleep(5) #wait for printing job to finish (5 seconds)
    keyboard.write('Week ' + str(week) + ' HW')
    keyboard.press_and_release('enter')
    time.sleep(0.5) #wait for file to get saved
    week += 1
