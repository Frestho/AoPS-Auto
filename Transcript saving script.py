import keyboard, time
week = 2
time.sleep(5)
while week < 25:
    keyboard.press_and_release('ctrl+l')
    time.sleep(0.1) #wait for browser to respond
    
    
    
    #Go to your week 1 transcript and paste it in the url below, replacing the existing one. Then move the number at the end here:
    #                          |             |                                               |   
    #                          v             v                                               v 
    keyboard.write('https://artofproblemsolving.com/class/1809-maa-amc10/transcript/' + str(25244 + week-1))#go to homework page
    
    
    
    keyboard.press_and_release('enter')
    time.sleep(8) #wait for page to fully load (8 seconds)
    keyboard.press_and_release('ctrl+p')
    time.sleep(1) #wait for printing menu to pop up (1 second)
    keyboard.press_and_release('enter')
    time.sleep(14) #wait for printing job to finish (14 seconds)
    keyboard.write('Week ' + str(week) + ' Class')
    keyboard.press_and_release('enter')
    time.sleep(0.5) #wait for file to get saved
    week += 1
    
    
