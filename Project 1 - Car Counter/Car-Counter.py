from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import * #sort

cap = cv2.VideoCapture("../Videos/cars.mp4")


model = YOLO("../Yolo-Weights/yolov8n.pt")
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

mask = cv2.imread('mask.png')

# Tracking
tracker = Sort(max_age=20,
               min_hits=3,
               iou_threshold=0.3) # Tracker instance

limitingline = [300,350 , 673, 350]
totalCounts = []
while True:
    success, img = cap.read()
    # overlay the mask on image
    ImgRegion = cv2.bitwise_and(img, mask)
    imgGraphics = cv2.imread("graphics.png", cv2.IMREAD_UNCHANGED)
    img = cvzone.overlayPNG(img, imgGraphics, (0,0))
    results = model(ImgRegion, stream=True)
    detections = np.empty((0,5))
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
            #Find class
            clsid = box.cls[0]
            currentcls = classNames[int(clsid)]
            #Find out confidence
            conf = (math.ceil(box.conf[0]*100))/100
            # print(conf)
            if (currentcls in ['car', 'motorbike', 'truck', 'bus']) and conf > 0.3:
                # cvzone.cornerRect(img, (x1, y1, w, h), l=10, rt = 5)
                # cvzone.putTextRect(img, f"{currentcls} {conf}", (max(0,x1), max(35,y1)), scale=1.5, thickness=2,
                #                offset=4)
                currentArray = np.array([x1, y1, x2, y2, conf])
                detections = np.vstack((detections, currentArray))

    resultsTracker = tracker.update(detections) # format it needs is x1, y1, x2, y2, score
    cv2.line(img, (limitingline[0], limitingline[1]), (limitingline[2], limitingline[3]),
             (0,0,255), 5)

    for result in resultsTracker:
        x1, y1, x2, y2, id = result
        x1, y1, x2, y2 , id= int(x1), int(y1), int(x2), int(y2), int(id)
        print(result)
        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(img, (x1, y1, w, h), l=10, rt = 2, colorR=(255, 0, 255))
        cvzone.putTextRect(img, f"{id}", (max(0, x1), max(35, y1)), scale=1.5, thickness=2,
                       offset=4)
        cx, cy = x1+w//2, y1+h//2
        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        if limitingline[0]<cx<limitingline[2] and limitingline[1]- 30 <cy< limitingline[1]+30:
            if totalCounts.count(id) == 0:
                totalCounts.append(id)
                cv2.line(img, (limitingline[0], limitingline[1]), (limitingline[2], limitingline[3]),
                         (0, 255, 0), 5)

        # cvzone.putTextRect(img, f"count: {len(totalCounts)}", (50, 50), scale=2)
    cv2.putText(
        img,
        str(len(totalCounts)),
        (255, 100),
        cv2.FONT_HERSHEY_PLAIN,
        5,
        (50, 50, 255),
        8
    )

    cv2.imshow("image", img)
    # cv2.imshow('ImageRegion', ImgRegion)
    cv2.waitKey(1) # to run live webcam if 0 then runs static image
