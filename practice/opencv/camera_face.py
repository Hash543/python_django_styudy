import cv2 
import numpy as np
from PIL import Image, ImageDraw, ImageFont

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)
mode = 0
label = ["正常", "模糊", "負片", "素描"]

def put_chinese_text(img, text, position, color=(0,255,0)):
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    # windows 內建字體
    font = ImageFont.truetype('c:/windows/fonts/msjh.ttc', 32)
    draw.text(position, text, font=font, fill=color)
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

while True:
    # 讀取每一幀
    ret, frame = cap.read()

    if not ret:
        break

    # 轉換為灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 偵測人臉
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # 負片
    # negative = cv2.bitwise_not(frame)
    # effetct_frame = cv2.GaussianBlur(frame, (15,15), 0)
    match mode:
        case 0:
            effetct_frame = cv2.divide(gray, cv2.GaussianBlur(gray, (21, 21), 0), scale=256)
        case 1:
            effetct_frame = cv2.GaussianBlur(frame, (15,15), 0)
        case 2:
            effetct_frame = cv2.bitwise_not(frame)
        case 3:
            # sharpness
            effetct_frame = cv2.filter2D(frame, -1, np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]))
    # 畫人臉框
    for(x, y, w, h) in faces:
        cv2.rectangle(effetct_frame, (x, y), (x+w, y+h), (255,0,255), 2)
        # cv2.putText(effetct_frame, 'Detected Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,255), 2)

    cv2.putText(effetct_frame, f'Faces: {len(faces)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    cv2.putText(effetct_frame, f'Mode: {label[mode]}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    effetct_frame = put_chinese_text(effetct_frame, f'模式: {label[mode]}', (10, 90))
    cv2.imshow('Face detection', effetct_frame)
    key = cv2.waitKey(1) & 0xFF
    # 按 Q 離開
    if key == ord('q'):
        break
    # 按空白切換模式
    elif key == ord(' '):
        mode = (mode + 1) % 4
cap.release()
cv2.destroyAllWindows()