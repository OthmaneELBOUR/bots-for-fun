import pyautogui as pag
import time


size_res = pag.size()
pag.FAILSAFE = False
X = size_res[0]
Y = size_res[1]

# Automate the way you delete GPT old conversations
print(X, Y)
pag.click(0, 0, duration=1) # This click is to ensure you select the window in the background which is the browser. May need some update to a better flexibility

pag.shortcut(['ctrl', 't'])
pag.typewrite("chatgpt", 0.1)
pag.press('enter')
pag.moveTo(160, 350, 2, tween=pag.easeInQuad)
for i in range(3):
    time.sleep(2)
    pag.scroll(-15000)
for i in range(7):
    pag.moveTo(278, 870, duration=0.5, tween=pag.easeInQuad)
    time.sleep(0.5)
    pag.click()
    pag.click(317, 813, duration=0.2, tween=pag.easeInQuad)
    pag.click(1148, 686, duration=0.5, tween=pag.easeInQuad)
    time.sleep(6)






