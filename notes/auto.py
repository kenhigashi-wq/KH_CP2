import threading
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener

# Initialize tools
mouse = Controller()
clicking = True

def clicker():
    """Background task that clicks at maximum speed."""
    while clicking:
        mouse.click(Button.left)

def on_press(key):
    """Stops the script when any key is pressed."""
    global clicking
    clicking = False
    return False

# 5-second countdown warning
print("Get ready...")
for i in range(5, 0, -1):
    print(f"Starting in {i}...")
    time.sleep(1)

# Start the clicker thread
click_thread = threading.Thread(target=clicker)
click_thread.start()


print("!!! AUTO CLICKER ACTIVE !!!")
print("Press ANY key to stop.")

# Start the listener
with Listener(on_press=on_press) as listener:
    listener.join()

print("Auto clicker stopped.")
