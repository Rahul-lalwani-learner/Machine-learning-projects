from ultralytics import YOLO
import cv2
import cvzone
import math
# cap = cv2.VideoCapture(0) # for default webcam
# cap.set(3, 1240) # width
# cap.set(4, 720) # Height
cap = cv2.VideoCapture("../Videos/ppe-2.mp4")


model = YOLO("best.pt")
classNames =['Excavator', 'Gloves', 'Hardhat', 'Ladder', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'SUV', 'Safety Cone', 'Safety Vest', 'bus', 'dump truck', 'fire hydrant', 'machinery', 'mini-van', 'sedan', 'semi', 'trailer', 'truck and trailer', 'truck', 'van', 'vehicle', 'wheel loader']


while True:
    success, img = cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:

            #bounding  box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # print(x1, y1, x2, y2)
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0,255), 3)
            # box.xywh
            w, h = x2-x1, y2-y1
            # cvzone.cornerRect(img,(x1, y1, w, h) )
            #Find class
            clsid = box.cls[0]
            cls = classNames[int(clsid)]
            #Find out confidence
            conf = (math.ceil(box.conf[0]*100))/100
            # print(conf)

            if cls == 'Hardhat' or cls == 'Safety Vest' or cls == 'Mask' or cls == 'Gloves':
                myColor = (0,255, 0)
            elif cls == 'Person':
                myColor = (255, 0, 0)
            else:
                myColor = (0, 0, 255)
            cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 3)
            cvzone.putTextRect(img, f"{cls} {conf}", (max(0,x1), max(35,y1)),
                               scale=1.5,
                               thickness=2,
                               colorB=myColor,
                               colorT=(255, 255, 255),
                               colorR=myColor)

    cv2.imshow("image", img)
    cv2.waitKey(1) # to run live webcam if 0 then runs static image
