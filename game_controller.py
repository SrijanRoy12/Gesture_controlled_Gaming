import pyautogui
import time
import math

last_action_time = 0
cooldown = 0.5  # seconds

def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def interpret_gesture(landmarks):
    global last_action_time
    now = time.time()

    if not landmarks or len(landmarks) < 12:
        return

    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]

    dx = index_tip[0] - thumb_tip[0]
    dy = index_tip[1] - thumb_tip[1]

    if now - last_action_time > cooldown:
        # Pinch (Index and Thumb) -> Hoverboard
        if distance(index_tip, thumb_tip) < 30:
            pyautogui.press('space')
            print("Gesture: Hoverboard")
        # Swipe Up
        elif dy < -60:
            pyautogui.press('up')
            print("Gesture: Jump")
        # Swipe Down
        elif dy > 60:
            pyautogui.press('down')
            print("Gesture: Roll")
        # Swipe Right
        elif dx > 60:
            pyautogui.press('right')
            print("Gesture: Right")
        # Swipe Left
        elif dx < -60:
            pyautogui.press('left')
            print("Gesture: Left")

        last_action_time = now
