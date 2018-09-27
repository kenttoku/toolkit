import pyautogui
import time

# Settings
MOD = 'winleft'
PROJECT_DIRECTORY = '~/Desktop/projects/ei24'

# Basic Commands
NEW_TERMINAL = {'command': 'enter', 'useShift': False}
NEW_BROWSER = {'command': 'f2', 'useShift': False}
FOCUS_LEFT = {'command': 'j', 'useShift': False}
FOCUS_DOWN = {'command': 'k', 'useShift': False}
FOCUS_UP = {'command': 'l', 'useShift': False}
FOCUS_RIGHT = {'command': ';', 'useShift': False}
FOCUS_PARENT = {'command': 'a', 'useShift': False}
TOGGLE_FOCUS = {'command': 'space', 'useShift': False}

# Moving Windows
MOVE_LEFT = {'command': 'j', 'useShift': True}
MOVE_DOWN = {'command': 'k', 'useShift': True}
MOVE_UP = {'command': 'l', 'useShift': True}
MOVE_RIGHT = {'command': ';', 'useShift': True}

# Modifying Windows
TOGGLE_FULL = {'command': 'f', 'useShift': False}
SPLIT_VERT = {'command': 'v', 'useShift': False}
SPLIT_HOR = {'command': 'h', 'useShift': False}
RESIZE_MODE = {'command': 'r', 'useShift': False}

# Kill Window
KILL = {'command': 'k', 'useShift': True}

# Modes
DEFAULT_MODE = {'command': 'e', 'useShift': False}
TABBED_MODE = {'command': 'w', 'useShift': False}
STACKED_MODE = {'command': 's', 'useShift': False}

def modCommand(command):
    pyautogui.keyDown(MOD)
    pyautogui.press(command)
    pyautogui.keyUp(MOD)

def modShiftCommand(command):
    pyautogui.keyDown(MOD)
    pyautogui.keyDown('shiftleft')
    pyautogui.press(command)
    pyautogui.keyUp(MOD)
    pyautogui.keyUp('shiftleft')

def runCommand(action):
    if action['useShift']:
        modShiftCommand(action['command'])
    else:
        modCommand(action['command'])

def holdModCommand(command, sleep):
    pyautogui.keyDown(MOD)
    pyautogui.keyDown(command)
    time.sleep(2)
    pyautogui.keyUp(MOD)
    pyautogui.keyUp(command)

def holdModShiftCommand(command, sleep):
    pyautogui.keyDown(MOD)
    pyautogui.keyDown('shiftleft')
    pyautogui.keyDown(command)
    time.sleep(2)
    pyautogui.keyUp(MOD)
    pyautogui.keyUp('shiftleft')
    pyautogui.keyUp(command)

def holdCommand(action):
    if action['useShift']:
        holdModShiftCommand(action['command'], 2)
    else:
        holdModCommand(action['command'], 2)

def main():
    runCommand(SPLIT_HOR)
    runCommand(NEW_TERMINAL)
    runCommand(SPLIT_VERT)
    runCommand(NEW_TERMINAL)
    runCommand(TABBED_MODE)
    runCommand(FOCUS_LEFT)
    runCommand(FOCUS_LEFT)
    runCommand(SPLIT_VERT)
    runCommand(NEW_BROWSER)
    runCommand(TABBED_MODE)

if __name__ == "__main__":
    main()