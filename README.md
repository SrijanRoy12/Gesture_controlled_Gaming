# 🖐 Gesture-Controlled Gaming 🎮  
Control Games with Your Hand — No Keyboard, No Controller!

## 📌 Overview  
This project uses **AI-powered hand gesture recognition** to control games like **Subway Surfers**, **Temple Run**, or any **PC/Android game** that responds to keyboard arrow keys — all using just a webcam.

Built with **Python**, **OpenCV**, and **MediaPipe**, it detects your hand movements in real-time and translates them into game actions.

---

## 🎮 Supported Gestures & Game Actions

| Gesture        | Action         | Key Press Sent |
|----------------|----------------|----------------|
| ✋ Hand Up      | Jump           | `↑`            |
| 👇 Hand Down    | Slide/Roll     | `↓`            |
| ⬅️ Swipe Left   | Move Left      | `←`            |
| ➡️ Swipe Right  | Move Right     | `→`            |
| 🤏 Pinch (optional) | Special/Boost | Customizable  |

---

## 🕹️ Types of Games You Can Play

This system works with any game that uses **keyboard inputs** like `↑ ↓ ← →`. Here are some examples:

### ✅ PC Games:
- **Temple Run 2**
- **Hill Climb Racing**
- **Browser-based endless runners** (with keyboard support)

### ✅ Android Games (via Emulator):
- **Subway Surfers** (in BlueStacks or LDPlayer)
- **Car Racing Games**
- **Action runners and obstacle dodgers**

---

## 💻 Tech Stack

- 🧠 **Python**
- 🖼️ **OpenCV** – Video feed processing
- 🖐️ **MediaPipe** – Hand landmark detection
- 🖱️ **PyAutoGUI** – Simulates keyboard inputs
- (Optional) 📱 **Android Emulator** – For mobile game compatibility

---

## 🚀 How to Run

```bash
git clone https://github.com/yourusername/Gesture_controlled_Gaming.git
cd Gesture_controlled_Gaming
pip install -r requirements.txt
python main.py
Make sure:

Your webcam is on

The game is open and focused

For emulators, configure arrow key mappings

🛠️ Folder Structure
bash
Copy
Edit
Gesture_controlled_Gaming/
├── main.py                # Main script
├── gesture_controller.py  # Gesture detection logic
├── utils.py               # Utility functions
├── README.md
├── requirements.txt
🌟 Features
Real-time gesture tracking (under 30ms latency)

High-precision hand landmark detection

Fully customizable gesture-action mappings

Cross-platform (Windows/Linux)

Works with both emulators and desktop games

🧠 Future Scope
🗣️ Voice + Gesture hybrid control

🖼️ On-screen gesture preview overlay

🎯 Game-specific control profiles

🤖 AI gesture learning mode

🙌 Contributing
Pull requests are welcome! If you find a bug or want to suggest a new feature, feel free to open an issue.
