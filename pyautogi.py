#Hi Jaswanth welcome"

import pyautogui,time
print("hello")
print("running spammer Script")
for i in range(1,10):
  if i == 1:
    print("Script starts in 10 sec........")
  if i >=5:
    print("script starts in "+str(10-i)+"sec..........")
  time.sleep(1)
print("started script")
f = open("lyr.txt" , "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
print("Executed succesfully,spammed the hell out of them :D")
