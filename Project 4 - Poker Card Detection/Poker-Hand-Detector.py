from ultralytics import YOLO
import cv2
import cvzone
import math
from PokerHandFunction import findPokerHand

cap = cv2.VideoCapture(0) # for default webcam
cap.set(3, 1240) # width
cap.set(4, 720) # Height
# cap = cv2.VideoCapture("../Videos/people.mp4")


model = YOLO("best.pt")
classNames = ['10C', '10D', '10H', '10S',
              '2C', '2D', '2H', '2S',
              '3C', '3D', '3H', '3S',
              '4C', '4D', '4H', '4S',
              '5C', '5D', '5H', '5S',
              '6C', '6D', '6H', '6S',
              '7C', '7D', '7H', '7S',
              '8C', '8D', '8H', '8S',
              '9C', '9D', '9H', '9S',
              'AC', 'AD', 'AH', 'AS',
              'JC', 'JD', 'JH', 'JS',
              'KC', 'KD', 'KH', 'KS',
              'QC', 'QD', 'QH', 'QS']


while True:
    success, img = cap.read()
    results = model(img, stream=True)
    hand = []
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
            cvzone.cornerRect(img,(x1, y1, w, h) )
            #Find class
            clsid = box.cls[0]
            cls = classNames[int(clsid)]
            #Find out confidence
            conf = (math.ceil(box.conf[0]*100))/100
            # print(conf)
            cvzone.putTextRect(img, f"{cls} {conf}", (max(0,x1), max(35,y1)), scale=1.5, thickness=2)
            if conf>0.5:
                hand.append(cls)
    # print(hand)
    hand = list(set(hand))
    # print(hand)
    if len(hand) == 5:
        results = findPokerHand(hand)
        cvzone.putTextRect(img, f" Your Hand: {results}", (300, 75), scale=3, thickness=5)

        print(results)
    cv2.imshow("image", img)
    cv2.waitKey(1) # to run live webcam if 0 then runs static image
