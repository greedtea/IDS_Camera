import cv2
import imutils #調整size

print(cv2.__version__)
print(imutils.__version__)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
cap.set(cv2.CAP_PROP_FPS, 20)

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=1920)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()