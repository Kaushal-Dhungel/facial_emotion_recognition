import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('facial_recognition.h5')

emotions = ['Angry','Disgust','Fear','Happy','Sad','Surprise','Neutral']
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while True:
    ret, frame = cap.read()

    if not ret:
        continue

    cv2.rectangle(frame, (500, 100), (850, 450), (255, 255, 255), 2)
    roi = frame[100:450, 500:850]
    img = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (48, 48))
    img = np.array([img])
    # new_img = np.expand_dims(img, axis= 0) # adding one more dims kinaki 4 dims khojyo model le
     
    img = img/255      #normalise
         
    new_img = np.reshape(img,(1,48,48,1)) # making four dimensional
    pred = model.predict(new_img)
    pred = np.argmax(pred)
    text = emotions[pred]
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,text,(100,100),font,1.2,(255,255,0),2)

    cv2.imshow("emotion", frame)

    # print(pred)
    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
