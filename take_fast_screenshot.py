import keyboard  # using module keyboard
import pyscreenshot as ImageGrab
import random
counter = 200

while True:  
    im=ImageGrab.grab()
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('up'):  # if key 'q' is pressed 
            counter+= 1
            fpath = f'imgs/train/up/myphoto_{counter}.jpg'
            im.save(fpath, 'JPEG')
        
        elif keyboard.is_pressed('down'):  # if key 'q' is pressed 
            counter+= 1
            fpath = f'imgs/train/down/myphoto_{counter}.jpg'
            im.save(fpath, 'JPEG')
        
        elif keyboard.is_pressed('q'):  # if key 'q' is pressed 
            break
        
        elif random.random() < 0.1:
            counter+= 1
            im.save(f'imgs/train/nothing/myphoto_{counter}.jpg', 'JPEG')

    except Exception as e:
        print(e)
        break  # if user pressed a key other than the given key the loop will break