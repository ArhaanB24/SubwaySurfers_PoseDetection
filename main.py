import cv2
import mediapipe as mp
import pyautogui 
import webbrowser
# import threading
cam = cv2.VideoCapture(0)
mppose = mp.solutions.pose
pose = mppose.Pose()
mpdraw = mp.solutions.drawing_utils
x_pos = 0
y_pos = 0
webbrowser.open("https://poki.com/en/g/subway-surfers")
while True:
    img,frame = cam.read()
    desired_width = 720
    aspect_ratio = frame.shape[1] / frame.shape[0]
    desired_height = int(desired_width / aspect_ratio)
    frame = cv2.resize(frame, (desired_width, desired_height))
    height,width = frame.shape[:2]
    frame = cv2.flip(frame,1) #1080 1920
    # print(height,width)
    x,y = int(width/2),int(height/2)
    cv2.line(frame,(x,y*2),(x,0),(0,255,0),3)
    cv2.line(frame,(0,int(y/2)),(x*2,int(y/2)),(0,255,255),3)
    cv2.line(frame,(0,int(y*0.75)),(x*2,int(y*0.75)),(255,255,0),3)
    results = pose.process(frame)
    if results.pose_landmarks:
        for id,lm in enumerate(results.pose_landmarks.landmark[11:13]):
            start_x,start_y = int(results.pose_landmarks.landmark[11].x*width),int(results.pose_landmarks.landmark[11].y*height)
            end_x,end_y = int(results.pose_landmarks.landmark[12].x*width),int(results.pose_landmarks.landmark[12].y*height)
            cv2.line(frame,(start_x,start_y),(end_x,end_y),(0,255,0),3)
            cv2.circle(frame,(int(lm.x*width),int(lm.y*height)),3,(0,255,0),-1)
            if (start_y < y/2 and end_y < y/2) and (y_pos == 0 or y_pos == -1):
                pyautogui.press('up')
                print("Up")
                y_pos += 1
            elif (start_y > y*0.75 and end_y > y*0.75) and (y_pos == 0 or y_pos == 1):
                pyautogui.press('down')
                print("Down")
                y_pos -= 1
            elif (start_x > x and end_x < x) and (start_y < y*0.75 and end_y < y*0.75) and (start_y > y/2 and end_y > y/2):
                if x_pos == 1:
                    pyautogui.press('left')
                    print("Center Left")
                    x_pos = 0 
                    y_pos = 0
                elif x_pos == -1:
                    pyautogui.press('right')
                    print("Center Right")
                    y_pos = 0
                    x_pos = 0 
                else:
                    # print("Center")
                    x_pos = 0 
                    y_pos = 0
            elif (end_x<x and start_x<x) and (x_pos == 0 or x_pos == 1):
                pyautogui.press('left')
                print("Left")
                x_pos -= 1
            elif (end_x>x and start_x>x) and (x_pos == 0 or x_pos == -1):
                pyautogui.press('right')
                print("Right")
                x_pos += 1
    cv2.imshow("Taqneeq",frame)
    cv2.waitKey(1)  
cam.release()
cv2.destroyAllWindows()
