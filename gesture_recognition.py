import cv2
import mediapipe as mp
from collections import deque

class HandGestureDetector:
    def __init__(self, max_num_hands=1):
        self.hands = mp.solutions.hands.Hands(
            max_num_hands=max_num_hands,
            model_complexity=0,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.6,
            static_image_mode=False
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.history = deque(maxlen=5)

    def detect(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        landmarks = []

        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                h, w, _ = frame.shape
                temp_landmarks = []
                for lm in hand.landmark:
                    temp_landmarks.append((int(lm.x * w), int(lm.y * h)))
                self.history.append(temp_landmarks)
                self.mp_draw.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)

        if len(self.history) > 0:
            smoothed = []
            for i in range(len(self.history[0])):
                avg_x = int(sum([frame[i][0] for frame in self.history]) / len(self.history))
                avg_y = int(sum([frame[i][1] for frame in self.history]) / len(self.history))
                smoothed.append((avg_x, avg_y))
            return frame, smoothed

        return frame, landmarks
