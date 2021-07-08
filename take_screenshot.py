
from pynput.keyboard import Key, Listener, Controller
import random
import os
counter = 0



im=ImageGrab.grab()

def show(key):
    global counter,im    
    if key == Key.up:
        counter+= 1
        fpath = f'imgs/up/myphoto_{counter}.jpg'
        os.system(f"gnome-screenshot --file={fpath}")

    elif key == Key.down:
        counter+= 1
        im.save(f'imgs/down/myphoto_{counter}.jpg', 'JPEG')

    elif key == Key.delete:
        return False
    
    elif random.random() < 0.1:
        counter+= 1
        im.save(f'imgs/nothing/myphoto_{counter}.jpg', 'JPEG')


if __name__ == '__main__':
    print('adding ')
    with Listener(  on_press = show) as listener:   
        print('before any')
        listener.join()

