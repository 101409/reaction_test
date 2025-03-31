import pyautogui

screenWidth, screenHeight = pyautogui.size()

print("Checking color..")

while True:
    currentMouseX, currentMouseY = pyautogui.position()
    r,g,b = pyautogui.pixel(currentMouseX, currentMouseY)

    if(r,g,b) == (75, 219, 106):
        pyautogui.click()
        print("Clicked!")