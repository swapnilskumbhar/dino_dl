import keyboard
import pyscreenshot as ImageGrab
from pynput.keyboard import Controller, Key
from model import get_model
from torchvision import transforms
import torch
loader = transforms.Compose([ transforms.ToTensor() ])  

get_decision = get_model()

key_list = {
    0 :Key.down, 1 : 'nothing',2:Key.up
    }
dino_model = get_model()
dino_model = dino_model.to('cuda')
keyboard = Controller()
while True:  
    try:
        img=ImageGrab.grab()
        img = img.resize((384,216))
        img = loader(img)
        op = dino_model(img.unsqueeze(0).to('cuda'))
        _, idx = torch.max(op.detach(),1)
        if idx.item() == 1:
            continue
        keyboard.press(key_list[idx.item()])
        keyboard.release(key_list[idx.item()])
    except Exception as e:
        print(e)
        break  # if user pressed a key other than the given key the loop will break