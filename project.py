import random
import keyboard

keybd_list_1 = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','shift','ctrl','alt','tab','space','0','1','2','3','4','5','6','7','8','9','0']
keybd_list_2 = keybd_list_1.copy()

random.shuffle(keybd_list_2)

for a, b in zip(keybd_list_1, keybd_list_2):
    keyboard.remap_key(a, b)

print("Keys remapped. Press 'Esc' to stop.")

keyboard.wait('esc')