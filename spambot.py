import pyautogui, time

time.sleep(5)

message = open("message.txt", "r")
time.sleep(10)
for line in message:
    for word in line.split():
        if word:
            pyautogui.typewrite(word)
            pyautogui.press("enter")