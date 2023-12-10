# SubwaySurfers_PoseDetection
This program utilizes OpenCV, Mediapipe, and PyAutoGUI to control the game Subway Surfers based on body position detected by a webcam.

## Instructions:
- Position yourself: Ensure you are centered between the three lines on the screen before starting.
- Move right: Shift your entire body to the right of the green line if you are in the center lane, if you are the in the left lane then align yourself with the green line to move right.
- Move left: Shift your entire body to the left of the green line if you are in the center lane, if you are the in the right lane then align yourself with the green line to move left.
- Jump: Jump over the yellow line.
- Duck: Duck below the blue line.
  
## Tabs Format
Keep the browser and camera tab open side-by-side, you can continuously monitor your body position, actions triggered, and the corresponding gameplay effects. This setup provides a clear and immediate understanding of the interaction between your physical movements and the game, leading to a more immersive and enjoyable experience.
![image](https://github.com/ArhaanB24/SubwaySurfers_PoseDetection/assets/94664693/1942006f-979c-43e2-987f-15b8f65a51cf)

## Key features:
- Shoulder detection to control character movement.
- Jump and duck functionality based on body position.
- Automatic game launch through web browser.

## Requirements:
Python 3
OpenCV
Mediapipe
PyAutoGUI
Web browser
```
pip install opencv-python mediapipe pyautogui webbrowser
```
## Code breakdown:
- The code imports necessary libraries and opens the webcam.
- It defines lines on the screen for visual reference and shoulder detection.
- It uses Mediapipe to detect the user's pose and extract shoulder landmarks.
- Based on the shoulder position, the code sends appropriate keystrokes to control the game.
- It displays the video feed with lines and detected landmarks.

## Disclaimer:
This program is for educational purposes only and is not affiliated with Subway Surfers or Kiloo Games. The program may not work perfectly due to variations in webcam quality and lighting.
